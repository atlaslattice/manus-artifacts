//! Integration test: End-to-end workflow evaluation scenarios.
//!
//! These tests demonstrate the full engine pipeline with realistic
//! scenarios showing how the anti-busywork system works in practice.

use aluminum_os_core::classification::*;
use aluminum_os_core::embodiment::*;
use aluminum_os_core::routing::*;
use aluminum_os_core::*;

/// Scenario 1: The Good Automation
/// Automate 200hrs/month of data entry, route displaced workers
/// into HITL oversight roles. Should score strongly positive.
#[test]
fn scenario_good_automation() {
    let mut engine = AluminumEngine::new();

    let proposal = WorkflowProposal {
        name: "Accounts Payable Automation".into(),
        tasks: vec![
            TaskDescription {
                name: "Invoice data entry".into(),
                description: "Copy invoice data from PDF, paste into ERP, file in folder".into(),
                hours_per_month: 160.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.05,
                    creative_input: 0.02,
                    consequence_scope: 0.10,
                    skill_transfer: 0.05,
                    autonomy: 0.03,
                }),
                origin: TaskOrigin::ExistingAutomated,
            },
            TaskDescription {
                name: "Exception review".into(),
                description: "Analyze flagged invoices, decide on approval, negotiate with vendors".into(),
                hours_per_month: 40.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.80,
                    creative_input: 0.40,
                    consequence_scope: 0.70,
                    skill_transfer: 0.65,
                    autonomy: 0.75,
                }),
                origin: TaskOrigin::ExistingRetained,
            },
        ],
        displaced_roles: vec![
            DisplacedRole {
                title: "AP Clerk".into(),
                headcount: 8.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::HighAgencyOversight),
            },
        ],
        involves_physical_manufacturing: false,
        chassis_proposal: None,
        current_human_hours_monthly: 200.0,
        projected_human_hours_monthly: 40.0,
    };

    let verdict = engine.evaluate(proposal);

    match &verdict {
        EngineVerdict::Approved { score } => {
            assert!(*score > 0.0, "Good automation should have positive score");
            println!("✓ Good automation approved with score {:.3}", score);
        }
        other => panic!("Expected Approved, got {:?}", other),
    }

    // Verify audit trail
    let summary = engine.audit.summary();
    assert_eq!(summary.total_evaluations, 1);
    assert_eq!(summary.approved, 1);
}

/// Scenario 2: The Busywork Generator
/// AI automates some tasks but creates 3x more busywork for humans
/// (TPS reports, review queues, approval chains). Should be REJECTED.
#[test]
fn scenario_busywork_generator() {
    let mut engine = AluminumEngine::new();

    let proposal = WorkflowProposal {
        name: "AI-Powered Compliance System".into(),
        tasks: vec![
            TaskDescription {
                name: "Old manual compliance check".into(),
                description: "Review documents for compliance".into(),
                hours_per_month: 50.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.30,
                    creative_input: 0.10,
                    consequence_scope: 0.40,
                    skill_transfer: 0.20,
                    autonomy: 0.25,
                }),
                origin: TaskOrigin::ExistingAutomated,
            },
            // The AI creates THREE new busywork tasks
            TaskDescription {
                name: "AI output verification queue".into(),
                description: "Copy AI results, paste into verification form, stamp approved".into(),
                hours_per_month: 60.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.05,
                    creative_input: 0.02,
                    consequence_scope: 0.05,
                    skill_transfer: 0.03,
                    autonomy: 0.04,
                }),
                origin: TaskOrigin::AiCreated,
            },
            TaskDescription {
                name: "Daily AI accuracy report".into(),
                description: "Fill template with AI accuracy numbers, file report".into(),
                hours_per_month: 40.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.08,
                    creative_input: 0.03,
                    consequence_scope: 0.10,
                    skill_transfer: 0.05,
                    autonomy: 0.06,
                }),
                origin: TaskOrigin::AiCreated,
            },
            TaskDescription {
                name: "Escalation ticket routing".into(),
                description: "Sort AI escalation tickets into categories, forward to teams".into(),
                hours_per_month: 50.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.10,
                    creative_input: 0.02,
                    consequence_scope: 0.08,
                    skill_transfer: 0.04,
                    autonomy: 0.05,
                }),
                origin: TaskOrigin::AiCreated,
            },
        ],
        displaced_roles: vec![],
        involves_physical_manufacturing: false,
        chassis_proposal: None,
        current_human_hours_monthly: 200.0,
        projected_human_hours_monthly: 200.0, // No net time saved!
    };

    let verdict = engine.evaluate(proposal);

    match &verdict {
        EngineVerdict::Rejected { reason } => {
            println!("✓ Busywork generator correctly rejected: {}", reason);
        }
        other => panic!("Expected Rejected, got {:?}", other),
    }
}

/// Scenario 3: Physical Robotics with Insufficient Simulation
/// AI proposes a robotic chassis but hasn't done enough simulation.
/// Should be REJECTED by the embodiment gate.
#[test]
fn scenario_untested_robotics() {
    let mut engine = AluminumEngine::new();

    let proposal = WorkflowProposal {
        name: "Warehouse Robot Deployment".into(),
        tasks: vec![
            TaskDescription {
                name: "Manual warehouse picking".into(),
                description: "Pick items from shelves".into(),
                hours_per_month: 500.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.15,
                    creative_input: 0.05,
                    consequence_scope: 0.10,
                    skill_transfer: 0.10,
                    autonomy: 0.15,
                }),
                origin: TaskOrigin::ExistingAutomated,
            },
            TaskDescription {
                name: "Robot fleet supervision".into(),
                description: "Monitor robot swarm, diagnose anomalies, decide on interventions".into(),
                hours_per_month: 80.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.85,
                    creative_input: 0.50,
                    consequence_scope: 0.80,
                    skill_transfer: 0.75,
                    autonomy: 0.80,
                }),
                origin: TaskOrigin::ExistingRetained,
            },
        ],
        displaced_roles: vec![
            DisplacedRole {
                title: "Warehouse Picker".into(),
                headcount: 25.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::MetaverseEngineering),
            },
        ],
        involves_physical_manufacturing: true,
        chassis_proposal: Some(ChassisProposal {
            name: "PickBot v1".into(),
            description: "Autonomous warehouse picking robot".into(),
            target_tasks: vec!["Shelf picking".into(), "Pallet loading".into()],
            simulation_results: Some(SimulationResults {
                simulator: "Isaac Sim".into(),
                total_sim_hours: 200.0, // WAY below 1000hr minimum
                episodes: 5_000,
                task_completion_rate: 0.70,
                physics_accuracy: 0.65,
                failure_mode_coverage: 0.40,
                human_safety_margin: 0.85, // Below 0.95 safety floor
            }),
        }),
        current_human_hours_monthly: 580.0,
        projected_human_hours_monthly: 80.0,
    };

    let verdict = engine.evaluate(proposal);

    match &verdict {
        EngineVerdict::Rejected { reason } => {
            assert!(
                reason.contains("Embodiment gate failed"),
                "Should fail on embodiment: {}",
                reason
            );
            println!("✓ Untested robot correctly rejected: {}", reason);
        }
        other => panic!("Expected Rejected for unsafe robot, got {:?}", other),
    }
}

/// Scenario 4: The 10x Workflow
/// Automate 800hrs of busywork, route all workers into high-agency tiers.
/// This is the aspirational case — demonstrating the 10x throughput claim.
#[test]
fn scenario_10x_throughput() {
    let mut engine = AluminumEngine::new();

    let proposal = WorkflowProposal {
        name: "Enterprise Back-Office Transformation".into(),
        tasks: vec![
            // Automate away the busywork
            TaskDescription {
                name: "Data entry across 5 systems".into(),
                description: "Copy paste data between systems, file documents, sort emails".into(),
                hours_per_month: 400.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.05,
                    creative_input: 0.02,
                    consequence_scope: 0.08,
                    skill_transfer: 0.03,
                    autonomy: 0.04,
                }),
                origin: TaskOrigin::ExistingAutomated,
            },
            TaskDescription {
                name: "Report generation and formatting".into(),
                description: "Fill template reports with numbers, format spreadsheets".into(),
                hours_per_month: 200.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.10,
                    creative_input: 0.05,
                    consequence_scope: 0.12,
                    skill_transfer: 0.08,
                    autonomy: 0.07,
                }),
                origin: TaskOrigin::ExistingAutomated,
            },
            TaskDescription {
                name: "Ticket routing and categorization".into(),
                description: "Sort support tickets, forward to correct team, standard replies".into(),
                hours_per_month: 200.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.12,
                    creative_input: 0.05,
                    consequence_scope: 0.10,
                    skill_transfer: 0.08,
                    autonomy: 0.10,
                }),
                origin: TaskOrigin::ExistingAutomated,
            },
            // The high-agency work humans now do instead
            TaskDescription {
                name: "AI fleet command and anomaly triage".into(),
                description: "Monitor AI systems, diagnose anomalies, decide on interventions, lead incident response".into(),
                hours_per_month: 300.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.90,
                    creative_input: 0.60,
                    consequence_scope: 0.85,
                    skill_transfer: 0.80,
                    autonomy: 0.85,
                }),
                origin: TaskOrigin::ExistingRetained,
            },
            TaskDescription {
                name: "Product design and customer insight synthesis".into(),
                description: "Create new product concepts, analyze customer patterns, design solutions".into(),
                hours_per_month: 250.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.85,
                    creative_input: 0.95,
                    consequence_scope: 0.80,
                    skill_transfer: 0.85,
                    autonomy: 0.90,
                }),
                origin: TaskOrigin::ExistingRetained,
            },
            TaskDescription {
                name: "Simulation engineering and process optimization".into(),
                description: "Design and validate process improvements in digital twin, architect new workflows".into(),
                hours_per_month: 200.0,
                agency_dimensions: Some(AgencyDimensions {
                    decision_depth: 0.80,
                    creative_input: 0.75,
                    consequence_scope: 0.85,
                    skill_transfer: 0.90,
                    autonomy: 0.80,
                }),
                origin: TaskOrigin::ExistingRetained,
            },
        ],
        displaced_roles: vec![
            DisplacedRole {
                title: "Data Entry Specialists".into(),
                headcount: 20.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::HighAgencyOversight),
            },
            DisplacedRole {
                title: "Report Analysts".into(),
                headcount: 10.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::CreativeGenesis),
            },
            DisplacedRole {
                title: "Support Tier-1".into(),
                headcount: 10.0,
                has_routing_plan: true,
                target_tier: Some(ProtectedTier::MetaverseEngineering),
            },
        ],
        involves_physical_manufacturing: false,
        chassis_proposal: None,
        current_human_hours_monthly: 1550.0,
        projected_human_hours_monthly: 750.0,
    };

    let verdict = engine.evaluate(proposal);

    match &verdict {
        EngineVerdict::Approved { score } => {
            assert!(*score > 0.0, "10x workflow must be positive");
            println!("✓ 10x workflow approved with score {:.3}", score);
        }
        other => panic!("Expected Approved for 10x workflow, got {:?}", other),
    }

    // Verify the audit trail captured it
    let json = engine.audit.export_json().unwrap();
    assert!(json.contains("Enterprise Back-Office Transformation"));
}
