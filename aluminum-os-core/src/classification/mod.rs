//! # Task Classification Engine
//!
//! Classifies tasks by **agency level** — the degree of judgment, creativity,
//! and decision-making authority a human exercises when performing the task.

use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TaskDescription {
    pub name: String,
    pub description: String,
    pub hours_per_month: f64,
    pub agency_dimensions: Option<AgencyDimensions>,
    pub origin: TaskOrigin,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize, PartialEq)]
pub enum TaskOrigin {
    ExistingAutomated,
    ExistingRetained,
    AiCreated,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub struct AgencyDimensions {
    pub decision_depth: f64,
    pub creative_input: f64,
    pub consequence_scope: f64,
    pub skill_transfer: f64,
    pub autonomy: f64,
}

impl AgencyDimensions {
    pub fn composite_score(&self) -> f64 {
        const W_DECISION: f64 = 0.25;
        const W_CREATIVE: f64 = 0.25;
        const W_CONSEQUENCE: f64 = 0.20;
        const W_SKILL: f64 = 0.15;
        const W_AUTONOMY: f64 = 0.15;
        (self.decision_depth * W_DECISION)
            + (self.creative_input * W_CREATIVE)
            + (self.consequence_scope * W_CONSEQUENCE)
            + (self.skill_transfer * W_SKILL)
            + (self.autonomy * W_AUTONOMY)
    }

    pub fn is_busywork(&self, threshold: f64) -> bool {
        self.composite_score() < threshold
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ClassifiedTask {
    pub task: TaskDescription,
    pub agency: AgencyDimensions,
    pub agency_score: f64,
    pub category: TaskCategory,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize, PartialEq)]
pub enum TaskCategory {
    Busywork,
    LowAgency,
    ModerateAgency,
    HighAgency,
}

pub struct TaskClassifier {
    pub busywork_threshold: f64,
}

impl TaskClassifier {
    pub fn new() -> Self {
        Self { busywork_threshold: 0.25 }
    }

    pub fn classify(&self, task: &TaskDescription) -> ClassifiedTask {
        let agency = match &task.agency_dimensions {
            Some(dims) => *dims,
            None => self.estimate_agency(task),
        };
        let score = agency.composite_score();
        let category = self.categorize(score);
        ClassifiedTask { task: task.clone(), agency, agency_score: score, category }
    }

    fn categorize(&self, score: f64) -> TaskCategory {
        if score < self.busywork_threshold { TaskCategory::Busywork }
        else if score < 0.50 { TaskCategory::LowAgency }
        else if score < 0.75 { TaskCategory::ModerateAgency }
        else { TaskCategory::HighAgency }
    }

    fn estimate_agency(&self, task: &TaskDescription) -> AgencyDimensions {
        let desc = task.description.to_lowercase();
        let low_signals = ["copy", "paste", "enter data", "fill form", "forward", "file", "sort", "rename", "move to folder", "approve routine", "stamp", "template", "boilerplate", "standard", "repetitive"];
        let high_signals = ["design", "architect", "decide", "negotiate", "diagnose", "create", "invent", "strategy", "analyze", "judge", "lead", "mentor", "research", "innovate", "solve"];
        let low_count = low_signals.iter().filter(|k| desc.contains(**k)).count() as f64;
        let high_count = high_signals.iter().filter(|k| desc.contains(**k)).count() as f64;
        let total = (low_count + high_count).max(1.0);
        let base = high_count / total;
        AgencyDimensions {
            decision_depth: (base * 1.1).min(1.0),
            creative_input: (base * 0.9).min(1.0),
            consequence_scope: (base * 0.8).min(1.0),
            skill_transfer: (base * 1.0).min(1.0),
            autonomy: (base * 0.95).min(1.0),
        }
    }
}

impl Default for TaskClassifier {
    fn default() -> Self { Self::new() }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pure_busywork_scores_low() {
        let classifier = TaskClassifier::new();
        let task = TaskDescription { name: "Data Entry".into(), description: "Copy data from email, paste into spreadsheet, file in folder".into(), hours_per_month: 40.0, agency_dimensions: None, origin: TaskOrigin::ExistingAutomated };
        let result = classifier.classify(&task);
        assert!(result.agency_score < 0.25);
        assert_eq!(result.category, TaskCategory::Busywork);
    }

    #[test]
    fn test_high_agency_scores_high() {
        let classifier = TaskClassifier::new();
        let task = TaskDescription { name: "System Architecture".into(), description: "Design and architect the new platform, analyze tradeoffs, decide on strategy, lead the research effort".into(), hours_per_month: 60.0, agency_dimensions: None, origin: TaskOrigin::ExistingRetained };
        let result = classifier.classify(&task);
        assert!(result.agency_score > 0.5);
    }

    #[test]
    fn test_explicit_dimensions_used_when_provided() {
        let classifier = TaskClassifier::new();
        let dims = AgencyDimensions { decision_depth: 0.9, creative_input: 0.8, consequence_scope: 0.7, skill_transfer: 0.6, autonomy: 0.85 };
        let task = TaskDescription { name: "Strategic Planning".into(), description: "Whatever".into(), hours_per_month: 20.0, agency_dimensions: Some(dims), origin: TaskOrigin::ExistingRetained };
        let result = classifier.classify(&task);
        assert!((result.agency_score - dims.composite_score()).abs() < f64::EPSILON);
        assert_eq!(result.category, TaskCategory::HighAgency);
    }

    #[test]
    fn test_agency_dimensions_composite() {
        let dims = AgencyDimensions { decision_depth: 1.0, creative_input: 1.0, consequence_scope: 1.0, skill_transfer: 1.0, autonomy: 1.0 };
        assert!((dims.composite_score() - 1.0).abs() < f64::EPSILON);
        let zero = AgencyDimensions { decision_depth: 0.0, creative_input: 0.0, consequence_scope: 0.0, skill_transfer: 0.0, autonomy: 0.0 };
        assert!((zero.composite_score() - 0.0).abs() < f64::EPSILON);
    }
}
