//! # Embodiment Gating Module
//!
//! Before any AI-designed physical system (robot, device, chassis) is
//! approved for human manufacturing, it must pass the **Simulation
//! Fidelity Gate** — proving functional superiority in simulation first.
//!
//! ## The Principle
//!
//! Physical manifestation isn't a toy. If an AI designs a robotic arm,
//! that design must be exhaustively tested in simulation before a single
//! dollar of human manufacturing capital is spent. This:
//!
//! 1. Eliminates wasted physical prototyping cycles
//! 2. Ensures human engineers build something proven to work
//! 3. Creates a sim-to-real pipeline that compounds over time
//!
//! ## Simulation Fidelity Score
//!
//! The score is computed across four axes:
//!
//! - **Task Completion Rate**: % of target tasks completed in sim
//! - **Physics Accuracy**: How closely sim physics match real-world
//! - **Failure Mode Coverage**: % of identified failure modes tested
//! - **Human Safety Margin**: Safety factor above minimum thresholds

use serde::{Deserialize, Serialize};

/// A proposal to manufacture a physical robotic system.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ChassisProposal {
    pub name: String,
    pub description: String,
    /// What tasks is this chassis designed to perform?
    pub target_tasks: Vec<String>,
    /// Simulation results (if available).
    pub simulation_results: Option<SimulationResults>,
}

impl Default for ChassisProposal {
    fn default() -> Self {
        Self {
            name: String::new(),
            description: String::new(),
            target_tasks: Vec::new(),
            simulation_results: None,
        }
    }
}

/// Results from simulation testing.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SimulationResults {
    /// What simulation environment was used?
    pub simulator: String,
    /// Total simulation hours run.
    pub total_sim_hours: f64,
    /// Number of simulation episodes/trials.
    pub episodes: u64,

    // --- The four scoring axes ---

    /// Tasks successfully completed / total target tasks (0.0–1.0)
    pub task_completion_rate: f64,

    /// Physics accuracy score (0.0–1.0)
    /// Measures: gravity, friction, collision, deformation accuracy
    /// relative to real-world validation data.
    pub physics_accuracy: f64,

    /// Failure modes tested / total identified failure modes (0.0–1.0)
    pub failure_mode_coverage: f64,

    /// Safety margin above minimum thresholds (0.0–1.0+)
    /// 1.0 = exactly at minimum safety. >1.0 = exceeds safety requirements.
    /// <1.0 = below safety threshold (will fail gate).
    pub human_safety_margin: f64,
}

/// The computed fidelity score and gate result.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EmbodimentResult {
    pub fidelity_score: f64,
    pub passed: bool,
    pub breakdown: FidelityBreakdown,
    pub recommendations: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FidelityBreakdown {
    pub task_completion_weighted: f64,
    pub physics_accuracy_weighted: f64,
    pub failure_coverage_weighted: f64,
    pub safety_margin_weighted: f64,
}

/// The gate that evaluates chassis proposals.
pub struct EmbodimentGate {
    /// Minimum composite fidelity score to pass (default 0.85).
    pub minimum_fidelity: f64,
    /// Minimum safety margin (hard floor, default 0.95).
    pub minimum_safety: f64,
    /// Minimum sim hours required (default 1000).
    pub minimum_sim_hours: f64,

    // Weights for composite score
    pub w_task_completion: f64,
    pub w_physics_accuracy: f64,
    pub w_failure_coverage: f64,
    pub w_safety_margin: f64,
}

impl Default for EmbodimentGate {
    fn default() -> Self {
        Self {
            minimum_fidelity: 0.85,
            minimum_safety: 0.95,
            minimum_sim_hours: 1000.0,
            w_task_completion: 0.30,
            w_physics_accuracy: 0.25,
            w_failure_coverage: 0.20,
            w_safety_margin: 0.25,
        }
    }
}

impl EmbodimentGate {
    pub fn evaluate(&self, proposal: &Option<ChassisProposal>) -> EmbodimentResult {
        let proposal = match proposal {
            Some(p) => p,
            None => {
                return EmbodimentResult {
                    fidelity_score: 0.0,
                    passed: false,
                    breakdown: FidelityBreakdown {
                        task_completion_weighted: 0.0,
                        physics_accuracy_weighted: 0.0,
                        failure_coverage_weighted: 0.0,
                        safety_margin_weighted: 0.0,
                    },
                    recommendations: vec![
                        "No chassis proposal provided.".into(),
                    ],
                };
            }
        };

        let sim = match &proposal.simulation_results {
            Some(s) => s,
            None => {
                return EmbodimentResult {
                    fidelity_score: 0.0,
                    passed: false,
                    breakdown: FidelityBreakdown {
                        task_completion_weighted: 0.0,
                        physics_accuracy_weighted: 0.0,
                        failure_coverage_weighted: 0.0,
                        safety_margin_weighted: 0.0,
                    },
                    recommendations: vec![
                        "No simulation results. Physical manufacturing requires \
                         simulation proof before approval."
                            .into(),
                        format!(
                            "Minimum {} sim hours required.",
                            self.minimum_sim_hours
                        ),
                    ],
                };
            }
        };

        let mut recommendations = Vec::new();

        // Check hard floors
        if sim.total_sim_hours < self.minimum_sim_hours {
            recommendations.push(format!(
                "Insufficient sim hours: {:.0} < {:.0} required.",
                sim.total_sim_hours, self.minimum_sim_hours
            ));
        }

        if sim.human_safety_margin < self.minimum_safety {
            recommendations.push(format!(
                "Safety margin {:.2} below hard minimum {:.2}. BLOCKING.",
                sim.human_safety_margin, self.minimum_safety
            ));
        }

        // Compute weighted composite
        let breakdown = FidelityBreakdown {
            task_completion_weighted: sim.task_completion_rate * self.w_task_completion,
            physics_accuracy_weighted: sim.physics_accuracy * self.w_physics_accuracy,
            failure_coverage_weighted: sim.failure_mode_coverage * self.w_failure_coverage,
            safety_margin_weighted: sim.human_safety_margin.min(1.0) * self.w_safety_margin,
        };

        let fidelity_score = breakdown.task_completion_weighted
            + breakdown.physics_accuracy_weighted
            + breakdown.failure_coverage_weighted
            + breakdown.safety_margin_weighted;

        // Pass conditions: composite above threshold AND safety above hard floor
        // AND sufficient sim hours
        let passed = fidelity_score >= self.minimum_fidelity
            && sim.human_safety_margin >= self.minimum_safety
            && sim.total_sim_hours >= self.minimum_sim_hours;

        if fidelity_score < self.minimum_fidelity {
            recommendations.push(format!(
                "Composite fidelity {:.3} below threshold {:.2}.",
                fidelity_score, self.minimum_fidelity
            ));
        }

        if passed {
            recommendations.push("All gates passed. Approved for physical manufacturing.".into());
        }

        EmbodimentResult {
            fidelity_score,
            passed,
            breakdown,
            recommendations,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_excellent_simulation_passes() {
        let gate = EmbodimentGate::default();
        let proposal = Some(ChassisProposal {
            name: "Robotic Arm v1".into(),
            description: "6-DOF industrial arm".into(),
            target_tasks: vec!["Pick and place".into(), "Assembly".into()],
            simulation_results: Some(SimulationResults {
                simulator: "Isaac Sim".into(),
                total_sim_hours: 5000.0,
                episodes: 100_000,
                task_completion_rate: 0.95,
                physics_accuracy: 0.92,
                failure_mode_coverage: 0.88,
                human_safety_margin: 1.15,
            }),
        });

        let result = gate.evaluate(&proposal);
        assert!(result.passed, "Excellent sim should pass: {:?}", result.recommendations);
        assert!(result.fidelity_score >= 0.85);
    }

    #[test]
    fn test_no_simulation_fails() {
        let gate = EmbodimentGate::default();
        let proposal = Some(ChassisProposal {
            name: "Untested Robot".into(),
            description: "No sim data".into(),
            target_tasks: vec![],
            simulation_results: None,
        });

        let result = gate.evaluate(&proposal);
        assert!(!result.passed);
        assert!(result.fidelity_score < 0.01);
    }

    #[test]
    fn test_unsafe_robot_fails_even_with_high_score() {
        let gate = EmbodimentGate::default();
        let proposal = Some(ChassisProposal {
            name: "Fast but Unsafe".into(),
            description: "Great at tasks, bad at safety".into(),
            target_tasks: vec!["Speed test".into()],
            simulation_results: Some(SimulationResults {
                simulator: "Gazebo".into(),
                total_sim_hours: 2000.0,
                episodes: 50_000,
                task_completion_rate: 0.99,
                physics_accuracy: 0.95,
                failure_mode_coverage: 0.90,
                human_safety_margin: 0.80, // Below 0.95 hard floor
            }),
        });

        let result = gate.evaluate(&proposal);
        assert!(!result.passed, "Unsafe robot must fail regardless of other scores");
    }

    #[test]
    fn test_insufficient_sim_hours_fails() {
        let gate = EmbodimentGate::default();
        let proposal = Some(ChassisProposal {
            name: "Quick Test".into(),
            description: "Not enough sim time".into(),
            target_tasks: vec!["Basic".into()],
            simulation_results: Some(SimulationResults {
                simulator: "Isaac Sim".into(),
                total_sim_hours: 100.0, // Below 1000 minimum
                episodes: 500,
                task_completion_rate: 0.95,
                physics_accuracy: 0.95,
                failure_mode_coverage: 0.95,
                human_safety_margin: 1.10,
            }),
        });

        let result = gate.evaluate(&proposal);
        assert!(!result.passed, "Insufficient sim hours must fail");
    }
}
