//! # Tier Routing System
//!
//! When automation displaces human labor, that capacity doesn't vanish —
//! it needs to go somewhere. The routing system maps displaced workers
//! into three **Protected Tiers** of high-value work.
//!
//! ## The Three Protected Tiers
//!
//! ### Tier 1: High-Agency Oversight (HITL Swarm Commanders)
//! Humans who supervise, audit, and correct AI systems at scale.
//! Skills: systems thinking, anomaly detection, ethical judgment.
//! Example: An AI monitors 10,000 transactions; a human reviews the
//! 50 flagged ones requiring judgment.
//!
//! ### Tier 2: Creative Genesis / IP Provenance
//! Humans who create original works, designs, inventions, and IP.
//! Skills: design, writing, invention, artistic expression.
//! Example: AI generates 100 layout options; a human art director
//! selects, refines, and signs the final design.
//!
//! ### Tier 3: Metaverse / Physical Engineering
//! Humans who design, test, and build in simulation and physical space.
//! Skills: CAD, simulation, manufacturing, robotics.
//! Example: AI proposes a robotic arm design; a human engineer
//! validates it in simulation, then oversees physical fabrication.
//!
//! ## The Economics
//!
//! The key insight: these tiers aren't "nice to have" categories.
//! They're **capacity sinks** that absorb displaced labor while
//! producing higher economic value per hour than the busywork
//! that was automated away.
//!
//! If a data entry clerk (agency 0.1, $18/hr value generated)
//! is retrained as a HITL swarm commander (agency 0.8, $65/hr
//! value generated), that's a 3.6x value multiplier per worker.
//! Across an organization, that's the 10x throughput claim.

use serde::{Deserialize, Serialize};

/// The three protected tiers for displaced human labor.
#[derive(Debug, Clone, Copy, Serialize, Deserialize, PartialEq)]
pub enum ProtectedTier {
    /// Tier 1: Human-in-the-loop oversight of AI swarms
    HighAgencyOversight,
    /// Tier 2: Creative work, original IP, provenance
    CreativeGenesis,
    /// Tier 3: Simulation engineering, physical robotics, manufacturing
    MetaverseEngineering,
}

impl ProtectedTier {
    /// Minimum agency score required for work in this tier.
    pub fn minimum_agency(&self) -> f64 {
        match self {
            ProtectedTier::HighAgencyOversight => 0.65,
            ProtectedTier::CreativeGenesis => 0.70,
            ProtectedTier::MetaverseEngineering => 0.60,
        }
    }

    /// Estimated value multiplier vs. median busywork role.
    /// Based on: BLS occupational wage data + productivity studies.
    pub fn value_multiplier(&self) -> f64 {
        match self {
            ProtectedTier::HighAgencyOversight => 3.2,
            ProtectedTier::CreativeGenesis => 4.1,
            ProtectedTier::MetaverseEngineering => 3.8,
        }
    }

    /// Estimated training investment (hours) to transition from
    /// low-agency busywork role into this tier.
    pub fn training_hours_estimate(&self) -> f64 {
        match self {
            ProtectedTier::HighAgencyOversight => 200.0,  // ~5 weeks full-time
            ProtectedTier::CreativeGenesis => 400.0,       // ~10 weeks
            ProtectedTier::MetaverseEngineering => 600.0,  // ~15 weeks
        }
    }

    pub fn name(&self) -> &'static str {
        match self {
            ProtectedTier::HighAgencyOversight => "High-Agency Oversight",
            ProtectedTier::CreativeGenesis => "Creative Genesis / IP Provenance",
            ProtectedTier::MetaverseEngineering => "Metaverse / Physical Engineering",
        }
    }
}

/// A role being displaced by automation.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DisplacedRole {
    pub title: String,
    /// Number of people in this role affected.
    pub headcount: f64,
    /// Has a routing plan been defined?
    pub has_routing_plan: bool,
    /// Target tier (if routed).
    pub target_tier: Option<ProtectedTier>,
}

/// A concrete plan for routing displaced workers into a tier.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RoutingAssignment {
    pub role: DisplacedRole,
    pub assigned_tier: ProtectedTier,
    /// Estimated training hours per person.
    pub training_hours: f64,
    /// Estimated total training cost (hours × headcount).
    pub total_training_investment: f64,
    /// Projected value multiplier once transitioned.
    pub projected_value_multiplier: f64,
    /// Estimated time to full productivity (months).
    pub months_to_productivity: f64,
}

/// The complete routing plan for a workflow's displaced workers.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RoutingPlan {
    pub assignments: Vec<RoutingAssignment>,
    pub unrouted: Vec<DisplacedRole>,
    pub total_displaced_headcount: f64,
    pub total_routed_headcount: f64,
    pub total_training_investment_hours: f64,
    /// Aggregate projected value multiplier across all routed workers.
    pub aggregate_value_multiplier: f64,
}

impl RoutingPlan {
    /// What fraction of displaced workers have routing plans? (0.0–1.0)
    pub fn coverage_ratio(&self) -> f64 {
        if self.total_displaced_headcount > 0.0 {
            self.total_routed_headcount / self.total_displaced_headcount
        } else {
            1.0 // No displacement = no risk
        }
    }

    /// Total estimated ROI: value multiplier × routed headcount.
    pub fn projected_roi_ratio(&self) -> f64 {
        if self.total_routed_headcount > 0.0 {
            self.aggregate_value_multiplier
        } else {
            0.0
        }
    }

    pub fn explain(&self) -> String {
        let mut out = format!(
            "Routing Plan:\n\
             ├─ Total Displaced: {:.0} workers\n\
             ├─ Routed:          {:.0} workers ({:.0}%)\n\
             ├─ Unrouted:        {:.0} workers\n\
             ├─ Training Invest: {:.0} total hours\n\
             └─ Projected Value: {:.1}x multiplier\n\n",
            self.total_displaced_headcount,
            self.total_routed_headcount,
            self.coverage_ratio() * 100.0,
            self.total_displaced_headcount - self.total_routed_headcount,
            self.total_training_investment_hours,
            self.aggregate_value_multiplier,
        );

        for a in &self.assignments {
            out.push_str(&format!(
                "  → {} ({:.0} people) → {} | {:.0}hrs training | {:.1}x value | {:.0} months\n",
                a.role.title,
                a.role.headcount,
                a.assigned_tier.name(),
                a.training_hours,
                a.projected_value_multiplier,
                a.months_to_productivity,
            ));
        }

        for u in &self.unrouted {
            out.push_str(&format!(
                "  ⚠ {} ({:.0} people) → NO ROUTING PLAN\n",
                u.title, u.headcount
            ));
        }

        out
    }
}

/// The router that generates routing plans.
pub struct TierRouter {
    /// Default tier when a displaced role has no explicit assignment.
    pub default_tier: ProtectedTier,
}

impl TierRouter {
    pub fn new() -> Self {
        Self {
            default_tier: ProtectedTier::HighAgencyOversight,
        }
    }

    /// Generate a routing plan from classified tasks and displaced roles.
    pub fn route(
        &self,
        _classified_tasks: &[crate::classification::ClassifiedTask],
        displaced_roles: &[DisplacedRole],
    ) -> RoutingPlan {
        let mut assignments = Vec::new();
        let mut unrouted = Vec::new();
        let mut total_displaced = 0.0;
        let mut total_routed = 0.0;
        let mut total_training = 0.0;
        let mut weighted_value_sum = 0.0;

        for role in displaced_roles {
            total_displaced += role.headcount;

            if role.has_routing_plan {
                let tier = role.target_tier.unwrap_or(self.default_tier);
                let training = tier.training_hours_estimate();
                let total_invest = training * role.headcount;
                let value_mult = tier.value_multiplier();
                let months = training / 160.0; // ~160 working hours/month

                assignments.push(RoutingAssignment {
                    role: role.clone(),
                    assigned_tier: tier,
                    training_hours: training,
                    total_training_investment: total_invest,
                    projected_value_multiplier: value_mult,
                    months_to_productivity: months,
                });

                total_routed += role.headcount;
                total_training += total_invest;
                weighted_value_sum += value_mult * role.headcount;
            } else {
                unrouted.push(role.clone());
            }
        }

        let aggregate_value = if total_routed > 0.0 {
            weighted_value_sum / total_routed
        } else {
            0.0
        };

        RoutingPlan {
            assignments,
            unrouted,
            total_displaced_headcount: total_displaced,
            total_routed_headcount: total_routed,
            total_training_investment_hours: total_training,
            aggregate_value_multiplier: aggregate_value,
        }
    }
}

impl Default for TierRouter {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_full_routing_coverage() {
        let router = TierRouter::new();
        let roles = vec![
            DisplacedRole {
                title: "Data Entry".into(),
                headcount: 5.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::HighAgencyOversight),
            },
            DisplacedRole {
                title: "File Clerk".into(),
                headcount: 3.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::CreativeGenesis),
            },
        ];

        let plan = router.route(&[], &roles);
        assert!((plan.coverage_ratio() - 1.0).abs() < f64::EPSILON);
        assert_eq!(plan.unrouted.len(), 0);
        assert_eq!(plan.assignments.len(), 2);
        assert!(plan.aggregate_value_multiplier > 3.0);
    }

    #[test]
    fn test_partial_routing_coverage() {
        let router = TierRouter::new();
        let roles = vec![
            DisplacedRole {
                title: "Routed".into(),
                headcount: 5.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::MetaverseEngineering),
            },
            DisplacedRole {
                title: "Unrouted".into(),
                headcount: 5.0,
                has_routing_plan: false,
                target_tier: None,
            },
        ];

        let plan = router.route(&[], &roles);
        assert!((plan.coverage_ratio() - 0.5).abs() < f64::EPSILON);
        assert_eq!(plan.unrouted.len(), 1);
    }

    #[test]
    fn test_tier_value_multipliers_are_positive() {
        assert!(ProtectedTier::HighAgencyOversight.value_multiplier() > 1.0);
        assert!(ProtectedTier::CreativeGenesis.value_multiplier() > 1.0);
        assert!(ProtectedTier::MetaverseEngineering.value_multiplier() > 1.0);
    }
}
