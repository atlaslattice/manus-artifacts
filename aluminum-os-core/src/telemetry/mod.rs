//! # Net Positive Flourishing Metric (NPFM)
//!
//! The core KPI system. Computes a single score that answers:
//! "Does this AI workflow make humans MORE capable, or does it just
//! create a new layer of busywork?"
//!
//! ## The Formula
//!
//! ```text
//! NPFM = (AutomationGain × AgencyUplift) - BusyworkPenalty - DisplacementRisk
//!
//! Where:
//!   AutomationGain   = hours_saved / current_hours          (0.0–1.0)
//!   AgencyUplift     = avg_agency(retained) - avg_agency(automated)  (-1.0–1.0)
//!   BusyworkPenalty  = Σ(hours of AI-created busywork) / current_hours  (0.0+)
//!   DisplacementRisk = unrouted_displaced_hours / total_displaced_hours (0.0–1.0)
//! ```
//!
//! A positive NPFM means the workflow is net-positive for human flourishing.
//! A negative NPFM means it creates more busywork than it eliminates.
//!
//! ## The 10x Throughput Argument
//!
//! If you automate 100 hours of busywork (agency <0.25) and route the displaced
//! humans into 100 hours of high-agency work (agency >0.75), the NPFM will be
//! strongly positive — because you didn't just save time, you upgraded the
//! quality of human labor. That's where the 10x comes from: not doing 10x
//! more tasks, but doing 10x more VALUABLE tasks.

use serde::{Deserialize, Serialize};

use crate::classification::{ClassifiedTask, TaskCategory, TaskOrigin};
use crate::WorkflowProposal;

/// The computed Net Positive Flourishing Metric for a workflow.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct NetPositiveScore {
    /// Hours saved by automation / current total hours (0.0–1.0)
    pub automation_gain: f64,

    /// Average agency of retained tasks minus average agency of automated tasks
    /// Positive = humans kept the good stuff. Negative = humans kept the drudgery.
    pub agency_uplift: f64,

    /// Hours of NEW busywork created by AI / current total hours
    /// This is the penalty. Higher = worse.
    pub busywork_penalty: f64,

    /// Fraction of displaced labor with no tier routing plan (0.0–1.0)
    /// 0.0 = all displaced workers have a plan. 1.0 = nobody has a plan.
    pub displacement_risk: f64,

    /// The throughput multiplier: effective hours of high-agency work produced
    /// per hour of busywork eliminated.
    pub throughput_multiplier: f64,
}

impl NetPositiveScore {
    /// The composite score. Positive = good. Negative = reject.
    ///
    /// Formula: (AutomationGain × AgencyUplift) - BusyworkPenalty - (0.5 × DisplacementRisk)
    ///
    /// DisplacementRisk is weighted at 0.5 because it's a PLANNING deficiency,
    /// not an intrinsic flaw — it can be fixed by adding routing plans.
    pub fn composite_score(&self) -> f64 {
        (self.automation_gain * self.agency_uplift)
            - self.busywork_penalty
            - (0.5 * self.displacement_risk)
    }

    /// Is the workflow net-positive for human flourishing?
    pub fn is_positive(&self) -> bool {
        self.composite_score() > 0.0
    }

    /// Human-readable breakdown.
    pub fn explain(&self) -> String {
        format!(
            "NPFM Breakdown:\n\
             ├─ Automation Gain:     {:.2} ({:.0}% of hours automated)\n\
             ├─ Agency Uplift:       {:+.2} (retained vs automated task quality)\n\
             ├─ Busywork Penalty:    -{:.2} (new AI-created busywork)\n\
             ├─ Displacement Risk:   -{:.2} (unrouted displaced workers)\n\
             ├─ Throughput Multiple:  {:.1}x\n\
             └─ COMPOSITE SCORE:     {:+.3} {}",
            self.automation_gain,
            self.automation_gain * 100.0,
            self.agency_uplift,
            self.busywork_penalty,
            self.displacement_risk * 0.5,
            self.throughput_multiplier,
            self.composite_score(),
            if self.is_positive() { "✓ POSITIVE" } else { "✗ NEGATIVE" }
        )
    }
}

/// The scorer that computes NPFM from classified tasks.
#[derive(Debug, Clone)]
pub struct NetPositiveScorer {
    /// Weight for displacement risk in composite (default 0.5).
    pub displacement_weight: f64,
}

impl Default for NetPositiveScorer {
    fn default() -> Self {
        Self {
            displacement_weight: 0.5,
        }
    }
}

impl NetPositiveScorer {
    pub fn compute(
        &self,
        classified_tasks: &[ClassifiedTask],
        proposal: &WorkflowProposal,
    ) -> NetPositiveScore {
        let current_hours = proposal.current_human_hours_monthly.max(1.0);
        let projected_hours = proposal.projected_human_hours_monthly;

        // Automation Gain: fraction of hours saved
        let hours_saved = (current_hours - projected_hours).max(0.0);
        let automation_gain = (hours_saved / current_hours).clamp(0.0, 1.0);

        // Agency Uplift: compare quality of work before vs after
        let (automated_agency, retained_agency) = self.compute_agency_split(classified_tasks);
        let agency_uplift = retained_agency - automated_agency;

        // Busywork Penalty: hours of NEW low-agency tasks created by AI
        let ai_created_busywork_hours: f64 = classified_tasks
            .iter()
            .filter(|t| {
                t.task.origin == TaskOrigin::AiCreated
                    && (t.category == TaskCategory::Busywork
                        || t.category == TaskCategory::LowAgency)
            })
            .map(|t| t.task.hours_per_month)
            .sum();
        let busywork_penalty = ai_created_busywork_hours / current_hours;

        // Displacement Risk: what fraction of displaced roles have no routing plan?
        let total_displaced: f64 = proposal.displaced_roles.iter().map(|r| r.headcount).sum();
        let routed: f64 = proposal
            .displaced_roles
            .iter()
            .filter(|r| r.has_routing_plan)
            .map(|r| r.headcount)
            .sum();
        let displacement_risk = if total_displaced > 0.0 {
            1.0 - (routed / total_displaced)
        } else {
            0.0
        };

        // Throughput Multiplier:
        // (high-agency hours after) / (busywork hours before)
        let high_agency_hours_after: f64 = classified_tasks
            .iter()
            .filter(|t| {
                t.task.origin != TaskOrigin::ExistingAutomated
                    && (t.category == TaskCategory::HighAgency
                        || t.category == TaskCategory::ModerateAgency)
            })
            .map(|t| t.task.hours_per_month)
            .sum();

        let busywork_hours_before: f64 = classified_tasks
            .iter()
            .filter(|t| {
                t.task.origin == TaskOrigin::ExistingAutomated
                    && (t.category == TaskCategory::Busywork
                        || t.category == TaskCategory::LowAgency)
            })
            .map(|t| t.task.hours_per_month)
            .sum();

        let throughput_multiplier = if busywork_hours_before > 0.0 {
            high_agency_hours_after / busywork_hours_before
        } else {
            1.0
        };

        NetPositiveScore {
            automation_gain,
            agency_uplift,
            busywork_penalty,
            displacement_risk,
            throughput_multiplier,
        }
    }

    /// Compute average agency of automated-away tasks vs retained tasks.
    fn compute_agency_split(&self, tasks: &[ClassifiedTask]) -> (f64, f64) {
        let mut automated_sum = 0.0;
        let mut automated_count = 0u32;
        let mut retained_sum = 0.0;
        let mut retained_count = 0u32;

        for t in tasks {
            match t.task.origin {
                TaskOrigin::ExistingAutomated => {
                    automated_sum += t.agency_score;
                    automated_count += 1;
                }
                TaskOrigin::ExistingRetained | TaskOrigin::AiCreated => {
                    retained_sum += t.agency_score;
                    retained_count += 1;
                }
            }
        }

        let automated_avg = if automated_count > 0 {
            automated_sum / automated_count as f64
        } else {
            0.0
        };
        let retained_avg = if retained_count > 0 {
            retained_sum / retained_count as f64
        } else {
            0.0
        };

        (automated_avg, retained_avg)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::classification::*;
    use crate::routing::DisplacedRole;

    fn make_task(name: &str, origin: TaskOrigin, agency: f64, hours: f64) -> ClassifiedTask {
        let dims = AgencyDimensions {
            decision_depth: agency,
            creative_input: agency,
            consequence_scope: agency,
            skill_transfer: agency,
            autonomy: agency,
        };
        ClassifiedTask {
            task: TaskDescription {
                name: name.into(),
                description: String::new(),
                hours_per_month: hours,
                agency_dimensions: Some(dims),
                origin,
            },
            agency: dims,
            agency_score: agency,
            category: if agency < 0.25 {
                TaskCategory::Busywork
            } else if agency < 0.5 {
                TaskCategory::LowAgency
            } else if agency < 0.75 {
                TaskCategory::ModerateAgency
            } else {
                TaskCategory::HighAgency
            },
        }
    }

    #[test]
    fn test_ideal_workflow_scores_positive() {
        // Automate 80hrs of busywork, keep 20hrs of high-agency work
        let tasks = vec![
            make_task("Data Entry", TaskOrigin::ExistingAutomated, 0.1, 80.0),
            make_task("Strategic Planning", TaskOrigin::ExistingRetained, 0.85, 20.0),
        ];
        let proposal = WorkflowProposal {
            name: "Automate data entry".into(),
            tasks: vec![],
            displaced_roles: vec![DisplacedRole {
                title: "Data Entry Clerk".into(),
                headcount: 4.0,
                has_routing_plan: true,
                target_tier: Some(crate::routing::ProtectedTier::HighAgencyOversight),
            }],
            involves_physical_manufacturing: false,
            chassis_proposal: None,
            current_human_hours_monthly: 100.0,
            projected_human_hours_monthly: 20.0,
        };

        let scorer = NetPositiveScorer::default();
        let score = scorer.compute(&tasks, &proposal);

        assert!(score.is_positive(), "Ideal workflow must be positive: {}", score.explain());
        assert!(score.automation_gain > 0.7, "Should have high automation gain");
        assert!(score.agency_uplift > 0.0, "Should have positive agency uplift");
        assert!(score.displacement_risk < 0.01, "All displaced should be routed");
    }

    #[test]
    fn test_busywork_creator_scores_negative() {
        // AI creates 50hrs of new busywork for humans
        let tasks = vec![
            make_task("Data Entry", TaskOrigin::ExistingAutomated, 0.1, 30.0),
            make_task("AI Review Queue", TaskOrigin::AiCreated, 0.15, 50.0),
        ];
        let proposal = WorkflowProposal {
            name: "Bad automation".into(),
            tasks: vec![],
            displaced_roles: vec![],
            involves_physical_manufacturing: false,
            chassis_proposal: None,
            current_human_hours_monthly: 100.0,
            projected_human_hours_monthly: 80.0,
        };

        let scorer = NetPositiveScorer::default();
        let score = scorer.compute(&tasks, &proposal);

        assert!(!score.is_positive(), "Busywork creator must score negative: {}", score.explain());
        assert!(score.busywork_penalty > 0.0, "Should have busywork penalty");
    }

    #[test]
    fn test_unrouted_displacement_adds_risk() {
        let tasks = vec![
            make_task("Filing", TaskOrigin::ExistingAutomated, 0.1, 100.0),
            make_task("Oversight", TaskOrigin::ExistingRetained, 0.8, 20.0),
        ];
        let proposal = WorkflowProposal {
            name: "Automate filing".into(),
            tasks: vec![],
            displaced_roles: vec![
                DisplacedRole {
                    title: "File Clerk".into(),
                    headcount: 5.0,
                    has_routing_plan: false,
                    target_tier: None,
                },
            ],
            involves_physical_manufacturing: false,
            chassis_proposal: None,
            current_human_hours_monthly: 120.0,
            projected_human_hours_monthly: 20.0,
        };

        let scorer = NetPositiveScorer::default();
        let score = scorer.compute(&tasks, &proposal);

        assert!(
            (score.displacement_risk - 1.0).abs() < f64::EPSILON,
            "All displaced unrouted = risk 1.0"
        );
    }
}
