//! # Governance & Audit Trail
//!
//! Every decision the engine makes is logged immutably.
//! This is the fiduciary duty mechanism — if you claim your AI
//! workflow is net-positive for human flourishing, you need receipts.
//!
//! ## Why This Matters
//!
//! Without an audit trail, "anti-busywork" is just a slogan.
//! With an audit trail, it's a **provable claim** that regulators,
//! boards, and workers can verify.

use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use uuid::Uuid;

use crate::EngineVerdict;

/// A record of a single workflow evaluation.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EvaluationRecord {
    pub id: Uuid,
    pub timestamp: DateTime<Utc>,
    pub proposal_name: String,
    pub npfm_score: f64,
    pub routing_coverage: f64,
    pub embodiment_passed: Option<bool>,
    pub verdict: EngineVerdict,
}

impl EvaluationRecord {
    pub fn was_approved(&self) -> bool {
        matches!(self.verdict, EngineVerdict::Approved { .. })
    }

    pub fn was_rejected(&self) -> bool {
        matches!(self.verdict, EngineVerdict::Rejected { .. })
    }
}

/// The audit log. In production, this would be backed by an append-only
/// database or blockchain. For this implementation, it's an in-memory log.
pub struct AuditLog {
    records: Vec<EvaluationRecord>,
}

impl AuditLog {
    pub fn new() -> Self {
        Self {
            records: Vec::new(),
        }
    }

    pub fn log_evaluation(&mut self, record: EvaluationRecord) {
        log::info!(
            "AUDIT | {} | {} | NPFM={:.3} | Coverage={:.0}% | {:?}",
            record.id,
            record.proposal_name,
            record.npfm_score,
            record.routing_coverage * 100.0,
            record.verdict,
        );
        self.records.push(record);
    }

    /// Get all records.
    pub fn records(&self) -> &[EvaluationRecord] {
        &self.records
    }

    /// Get records for a specific proposal.
    pub fn records_for(&self, proposal_name: &str) -> Vec<&EvaluationRecord> {
        self.records
            .iter()
            .filter(|r| r.proposal_name == proposal_name)
            .collect()
    }

    /// Summary statistics.
    pub fn summary(&self) -> AuditSummary {
        let total = self.records.len();
        let approved = self.records.iter().filter(|r| r.was_approved()).count();
        let rejected = self.records.iter().filter(|r| r.was_rejected()).count();
        let conditional = total - approved - rejected;

        let avg_npfm = if total > 0 {
            self.records.iter().map(|r| r.npfm_score).sum::<f64>() / total as f64
        } else {
            0.0
        };

        let avg_coverage = if total > 0 {
            self.records.iter().map(|r| r.routing_coverage).sum::<f64>() / total as f64
        } else {
            0.0
        };

        AuditSummary {
            total_evaluations: total,
            approved,
            rejected,
            conditional,
            average_npfm: avg_npfm,
            average_routing_coverage: avg_coverage,
        }
    }

    /// Export the full log as JSON.
    pub fn export_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string_pretty(&self.records)
    }
}

impl Default for AuditLog {
    fn default() -> Self {
        Self::new()
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AuditSummary {
    pub total_evaluations: usize,
    pub approved: usize,
    pub rejected: usize,
    pub conditional: usize,
    pub average_npfm: f64,
    pub average_routing_coverage: f64,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_audit_log_records_and_retrieves() {
        let mut log = AuditLog::new();

        log.log_evaluation(EvaluationRecord {
            id: Uuid::new_v4(),
            timestamp: Utc::now(),
            proposal_name: "Test Workflow".into(),
            npfm_score: 0.75,
            routing_coverage: 0.9,
            embodiment_passed: None,
            verdict: EngineVerdict::Approved { score: 0.75 },
        });

        assert_eq!(log.records().len(), 1);
        assert_eq!(log.records_for("Test Workflow").len(), 1);
        assert_eq!(log.records_for("Other").len(), 0);

        let summary = log.summary();
        assert_eq!(summary.total_evaluations, 1);
        assert_eq!(summary.approved, 1);
    }

    #[test]
    fn test_export_json() {
        let mut log = AuditLog::new();
        log.log_evaluation(EvaluationRecord {
            id: Uuid::new_v4(),
            timestamp: Utc::now(),
            proposal_name: "JSON Test".into(),
            npfm_score: 0.5,
            routing_coverage: 1.0,
            embodiment_passed: Some(true),
            verdict: EngineVerdict::Approved { score: 0.5 },
        });

        let json = log.export_json().unwrap();
        assert!(json.contains("JSON Test"));
        assert!(json.contains("Approved"));
    }
}
