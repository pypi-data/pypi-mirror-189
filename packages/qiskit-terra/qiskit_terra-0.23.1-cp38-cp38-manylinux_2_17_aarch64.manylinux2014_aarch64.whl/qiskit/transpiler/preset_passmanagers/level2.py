# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Pass manager for optimization level 2, providing medium optimization.

Level 2 pass manager: medium optimization by noise adaptive qubit mapping and
gate cancellation using commutativity rules.
"""

from qiskit.transpiler.passmanager_config import PassManagerConfig
from qiskit.transpiler.timing_constraints import TimingConstraints
from qiskit.transpiler.passmanager import PassManager
from qiskit.transpiler.passmanager import StagedPassManager
from qiskit.transpiler import ConditionalController

from qiskit.transpiler.passes import SetLayout
from qiskit.transpiler.passes import VF2Layout
from qiskit.transpiler.passes import TrivialLayout
from qiskit.transpiler.passes import DenseLayout
from qiskit.transpiler.passes import NoiseAdaptiveLayout
from qiskit.transpiler.passes import SabreLayout
from qiskit.transpiler.passes import FixedPoint
from qiskit.transpiler.passes import Depth
from qiskit.transpiler.passes import Size
from qiskit.transpiler.passes import Optimize1qGatesDecomposition
from qiskit.transpiler.passes import CommutativeCancellation
from qiskit.transpiler.passes import GatesInBasis
from qiskit.transpiler.passes import BarrierBeforeFinalMeasurements
from qiskit.transpiler.preset_passmanagers import common
from qiskit.transpiler.passes.layout.vf2_layout import VF2LayoutStopReason

from qiskit.transpiler.preset_passmanagers.plugin import (
    PassManagerStagePluginManager,
)


def level_2_pass_manager(pass_manager_config: PassManagerConfig) -> StagedPassManager:
    """Level 2 pass manager: medium optimization by initial layout selection and
    gate cancellation using commutativity rules.

    This pass manager applies the user-given initial layout. If none is given, a search
    for a perfect layout (i.e. one that satisfies all 2-qubit interactions) is conducted.
    If no such layout is found, qubits are laid out on the most densely connected subset
    which also exhibits the best gate fidelities.

    The pass manager then transforms the circuit to match the coupling constraints.
    It is then unrolled to the basis, and any flipped cx directions are fixed.
    Finally, optimizations in the form of commutative gate cancellation and redundant
    reset removal are performed.

    Args:
        pass_manager_config: configuration of the pass manager.

    Returns:
        a level 2 pass manager.

    Raises:
        TranspilerError: if the passmanager config is invalid.
    """
    plugin_manager = PassManagerStagePluginManager()
    basis_gates = pass_manager_config.basis_gates
    inst_map = pass_manager_config.inst_map
    coupling_map = pass_manager_config.coupling_map
    initial_layout = pass_manager_config.initial_layout
    init_method = pass_manager_config.init_method
    layout_method = pass_manager_config.layout_method or "sabre"
    routing_method = pass_manager_config.routing_method or "sabre"
    translation_method = pass_manager_config.translation_method or "translator"
    optimization_method = pass_manager_config.optimization_method
    scheduling_method = pass_manager_config.scheduling_method
    instruction_durations = pass_manager_config.instruction_durations
    seed_transpiler = pass_manager_config.seed_transpiler
    backend_properties = pass_manager_config.backend_properties
    approximation_degree = pass_manager_config.approximation_degree
    unitary_synthesis_method = pass_manager_config.unitary_synthesis_method
    timing_constraints = pass_manager_config.timing_constraints or TimingConstraints()
    unitary_synthesis_plugin_config = pass_manager_config.unitary_synthesis_plugin_config
    target = pass_manager_config.target
    hls_config = pass_manager_config.hls_config

    # Search for a perfect layout, or choose a dense layout, if no layout given
    _given_layout = SetLayout(initial_layout)

    def _choose_layout_condition(property_set):
        # layout hasn't been set yet
        return not property_set["layout"]

    def _vf2_match_not_found(property_set):
        # If a layout hasn't been set by the time we run vf2 layout we need to
        # run layout
        if property_set["layout"] is None:
            return True
        # if VF2 layout stopped for any reason other than solution found we need
        # to run layout since VF2 didn't converge.
        if (
            property_set["VF2Layout_stop_reason"] is not None
            and property_set["VF2Layout_stop_reason"] is not VF2LayoutStopReason.SOLUTION_FOUND
        ):
            return True
        return False

    # Try using VF2 layout to find a perfect layout
    _choose_layout_0 = (
        []
        if pass_manager_config.layout_method
        else VF2Layout(
            coupling_map,
            seed=seed_transpiler,
            call_limit=int(5e6),  # Set call limit to ~10 sec with rustworkx 0.10.2
            properties=backend_properties,
            target=target,
        )
    )

    if layout_method == "trivial":
        _choose_layout_1 = TrivialLayout(coupling_map)
    elif layout_method == "dense":
        _choose_layout_1 = DenseLayout(coupling_map, backend_properties, target=target)
    elif layout_method == "noise_adaptive":
        _choose_layout_1 = NoiseAdaptiveLayout(backend_properties)
    elif layout_method == "sabre":
        _choose_layout_1 = SabreLayout(
            coupling_map,
            max_iterations=2,
            seed=seed_transpiler,
            swap_trials=10,
            layout_trials=10,
            skip_routing=pass_manager_config.routing_method is not None
            and routing_method != "sabre",
        )

    # Choose routing pass
    routing_pm = plugin_manager.get_passmanager_stage(
        "routing", routing_method, pass_manager_config, optimization_level=2
    )

    # Build optimization loop: 1q rotation merge and commutative cancellation iteratively until
    # no more change in depth
    _depth_check = [Depth(recurse=True), FixedPoint("depth")]
    _size_check = [Size(recurse=True), FixedPoint("size")]

    def _opt_control(property_set):
        return (not property_set["depth_fixed_point"]) or (not property_set["size_fixed_point"])

    _opt = [
        Optimize1qGatesDecomposition(basis=basis_gates, target=target),
        CommutativeCancellation(basis_gates=basis_gates),
    ]

    unroll_3q = None
    # Build pass manager
    if coupling_map or initial_layout:
        unroll_3q = common.generate_unroll_3q(
            target,
            basis_gates,
            approximation_degree,
            unitary_synthesis_method,
            unitary_synthesis_plugin_config,
            hls_config,
        )
        if layout_method not in {"trivial", "dense", "noise_adaptive", "sabre"}:
            layout = plugin_manager.get_passmanager_stage(
                "layout", layout_method, pass_manager_config, optimization_level=2
            )
        else:

            def _swap_mapped(property_set):
                return property_set["final_layout"] is None

            layout = PassManager()
            layout.append(_given_layout)
            layout.append(_choose_layout_0, condition=_choose_layout_condition)
            layout.append(
                [BarrierBeforeFinalMeasurements(), _choose_layout_1], condition=_vf2_match_not_found
            )
            embed = common.generate_embed_passmanager(coupling_map)
            layout.append(
                [pass_ for x in embed.passes() for pass_ in x["passes"]], condition=_swap_mapped
            )
        routing = routing_pm
    else:
        layout = None
        routing = None
    if translation_method not in {"translator", "synthesis", "unroller"}:
        translation = plugin_manager.get_passmanager_stage(
            "translation", translation_method, pass_manager_config, optimization_level=2
        )
    else:
        translation = common.generate_translation_passmanager(
            target,
            basis_gates,
            translation_method,
            approximation_degree,
            coupling_map,
            backend_properties,
            unitary_synthesis_method,
            unitary_synthesis_plugin_config,
            hls_config,
        )

    if (coupling_map and not coupling_map.is_symmetric) or (
        target is not None and target.get_non_global_operation_names(strict_direction=True)
    ):
        pre_optimization = common.generate_pre_op_passmanager(target, coupling_map, True)
    else:
        pre_optimization = common.generate_pre_op_passmanager(remove_reset_in_zero=True)
    if optimization_method is None:
        optimization = PassManager()
        unroll = [pass_ for x in translation.passes() for pass_ in x["passes"]]
        # Build nested Flow controllers
        def _unroll_condition(property_set):
            return not property_set["all_gates_in_basis"]

        # Check if any gate is not in the basis, and if so, run unroll passes
        _unroll_if_out_of_basis = [
            GatesInBasis(basis_gates, target=target),
            ConditionalController(unroll, condition=_unroll_condition),
        ]
        optimization.append(_depth_check + _size_check)
        opt_loop = _opt + _unroll_if_out_of_basis + _depth_check + _size_check
        optimization.append(opt_loop, do_while=_opt_control)
    else:
        optimization = plugin_manager.get_passmanager_stage(
            "optimization", optimization_method, pass_manager_config, optimization_level=2
        )
    if scheduling_method is None or scheduling_method in {"alap", "asap"}:
        sched = common.generate_scheduling(
            instruction_durations, scheduling_method, timing_constraints, inst_map
        )
    else:
        sched = plugin_manager.get_passmanager_stage(
            "scheduling", scheduling_method, pass_manager_config, optimization_level=2
        )
    init = common.generate_error_on_control_flow(
        "The optimizations in optimization_level=2 do not yet support control flow."
    )
    if init_method is not None:
        init += plugin_manager.get_passmanager_stage(
            "init", init_method, pass_manager_config, optimization_level=2
        )
    elif unroll_3q is not None:
        init += unroll_3q

    return StagedPassManager(
        init=init,
        layout=layout,
        routing=routing,
        translation=translation,
        pre_optimization=pre_optimization,
        optimization=optimization,
        scheduling=sched,
    )
