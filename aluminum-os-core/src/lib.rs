//! # Aluminum OS Core — Anti-Busywork Policy Engine
//!
//! A real, compilable implementation of the Fiduciary Duty Against Busywork.
//!
//! ## Architecture
//!
//! This is NOT a compiler. It is a **policy engine** — a system that evaluates
//! proposed AI workflows, classifies tasks by human agency level, scores them,
//! routes displaced labor capacity into protected tiers, and gates physical
//! embodiment behind simulation proof.
//!
//! ### Modules
//!
//! - `classification` — Task taxonomy and agency scoring
//! - `telemetry` — NetPositiveScore (NPFM) computation
//! - `routing` — Displaced labor capacity routing into protected tiers
//! - `embodiment` — Simulation fidelity gating for physical robotics
//! - `governance` — Audit trail and decision logging

pub mod classification;
pub mod telemetry;
pub mod routing;
pub mod embodiment;
pub mod governance;

/// The core engine that ties all modules together.
/// Evaluates a proposed AI workflow end-to-end.
pub struct AluminumEngine {
    pub classifier: classification::TaskClassifier,
    pub scorer: telemetry::NetPositiveScorer,
    pub router: routing::TierRouter,
    pub embodiment_gate: embodiment::EmbodimentGate,
    pub audit: governance::AuditLog,
}

impl AluminumEngine {
    pub fn new() -> Self {
        Self {
            classifier: classification::TaskClassifier::new(),
            scorer: telemetry::NetPositiveScorer::default(),
            router: routing::TierRouter::new(),
            embodiment_gate: embodiment::EmbodimentGate::default(),
            audit: governance::AuditLog::new(),
        }
    }

    /// Evaluate a proposed AI workflow.
    /// Returns an `EngineVerdict` — approve, reject, or conditionally approve.
    pub fn evaluate(&mut self, proposal: WorkflowProposal) -> EngineVerdict {
        // Step 1: Classify every task in the proposed workflow
        let classified_tasks: Vec<classification::ClassifiedTask> = proposal
            .tasks
            .iter()
            .map(|t| self.classifier.classify(t))
            .collect();

        // Step 2: Compute the Net Positive Flourishing Metric
        let npfm = self.scorer.compute(&classified_tasks, &proposal);

        // Step 3: Route displaced human capacity into protected tiers
        let routing_plan = self.router.route(&classified_tasks, &proposal.displaced_roles);

        // Step 4: Check embodiment gate if physical manufacturing is involved
        let embodiment_result = if proposal.involves_physical_manufacturing {
            Some(self.embodiment_gate.evaluate(&proposal.chassis_proposal))
        } else {
            None
        };

        // Step 5: Render verdict
        let verdict = self.render_verdict(&npfm, &routing_plan, &embodiment_result);

        // Step 6: Log everything
        self.audit.log_evaluation(governance::EvaluationRecord {
            id: uuid::Uuid::new_v4(),
            timestamp: chrono::Utc::now(),
            proposal_name: proposal.name.clone(),
            npfm_score: npfm.composite_score(),
            routing_coverage: routing_plan.coverage_ratio(),
            embodiment_passed: embodiment_result.as_ref().map(|r| r.passed),
            verdict: verdict.clone(),
        });

        verdict
    }

    fn render_verdict(
        &self,
        npfm: &telemetry::NetPositiveScore,
        routing: &routing::RoutingPlan,
        embodiment: &Option<embodiment::EmbodimentResult>,
    ) -> EngineVerdict {
        let score = npfm.composite_score();
        let coverage = routing.coverage_ratio();

        // Hard rejection: net-negative flourishing
        if score < 0.0 {
            return EngineVerdict::Rejected {
                reason: format!(
                    "Net-negative flourishing score ({:.2}). Workflow creates more \
                     low-agency busywork than it eliminates.",
                    score
                ),
            };
        }

        // Hard rejection: embodiment fails simulation gate
        if let Some(ref result) = embodiment {
            if !result.passed {
                return EngineVerdict::Rejected {
                    reason: format!(
                        "Embodiment gate failed. SimulationFidelityScore {:.2} < \
                         required {:.2}. Physical manufacturing not approved.",
                        result.fidelity_score,
                        self.embodiment_gate.minimum_fidelity
                    ),
                };
            }
        }

        // Conditional: positive score but poor tier routing
        if coverage < 0.6 {
            return EngineVerdict::Conditional {
                score,
                conditions: vec![format!(
                    "Only {:.0}% of displaced labor capacity has a tier routing plan. \
                     Must reach 60% minimum before approval.",
                    coverage * 100.0
                )],
            };
        }

        EngineVerdict::Approved { score }
    }
}

impl Default for AluminumEngine {
    fn default() -> Self {
        Self::new()
    }
}

/// A proposed AI workflow submitted for evaluation.
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct WorkflowProposal {
    pub name: String,
    /// The tasks this workflow will create or modify for humans.
    pub tasks: Vec<classification::TaskDescription>,
    /// Roles that will be displaced or reduced by this automation.
    pub displaced_roles: Vec<routing::DisplacedRole>,
    /// Does this workflow involve manufacturing a physical robot/device?
    pub involves_physical_manufacturing: bool,
    /// If physical manufacturing is involved, the chassis proposal.
    #[serde(default)]
    pub chassis_proposal: Option<embodiment::ChassisProposal>,
    /// Total human-hours currently spent on these tasks per month.
    pub current_human_hours_monthly: f64,
    /// Projected human-hours after automation per month.
    pub projected_human_hours_monthly: f64,
}

/// The engine's final decision on a workflow proposal.
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub enum EngineVerdict {
    Approved {
        score: f64,
    },
    Conditional {
        score: f64,
        conditions: Vec<String>,
    },
    Rejected {
        reason: String,
    },
}
