# Product Requirements Document (PRD)

**Project Title:** USV Sentinel – AI-Powered Self-Healing Diagnostic System
**Prepared by:** Boris Eldarov
**Version:** 1.0
**Date:** June 2025

---

## Table of Contents

1. [Purpose](#1-purpose)
2. [Scope](#2-scope)
3. [Product Overview](#3-product-overview)
4. [Intended Users](#4-intended-users)
5. [High-Level Use Cases](#5-high-level-use-cases)
6. [High-Level Product Requirements](#6-high-level-product-requirements)
7. [Product Constraints](#7-product-constraints)
8. [Success Criteria](#8-success-criteria)
9. [Out of Scope (for PRD)](#9-out-of-scope-for-prd)
10. [Open Questions](#10-open-questions)

---

## 1. Purpose

The purpose of this document is to define the vision, key objectives, high-level functional expectations, and intended capabilities of the USV Sentinel system — an embedded AI-powered fault detection and mitigation module designed for military-grade Unmanned Surface Vessels (USVs). The system aims to improve mission continuity, reduce manual diagnostics, and increase autonomous resilience by proactively detecting and responding to onboard system degradation or failure risks.

---

## 2. Scope

USV Sentinel is intended for integration into various classes of military USVs, including autonomous patrol and reconnaissance vessels. It will operate independently of external infrastructure during missions and provide post-mission diagnostics for review and refinement. The system will monitor onboard electrical, thermal, and communication subsystems to detect anomalies and predict failures before they occur.

This PRD defines product-level expectations and business-driven outcomes. Detailed technical specifications will be documented in a System Requirements Document (SRD).

---

## 3. Product Overview

USV Sentinel is a smart embedded module combining real-time sensor data collection, onboard diagnostics, and lightweight AI-based inference. It acts as a health monitoring "watchdog" that enhances mission reliability and system safety.

### Key Features:

* Continuous real-time health monitoring of electrical and thermal subsystems
* AI-based prediction of fault conditions based on sensor behavior over time
* Autonomous activation of fallback modes to prevent failure escalation
* Post-mission logging and reporting for operator review
* Onboard operation without reliance on internet/cloud infrastructure

### Benefits:

* Reduces the risk of critical failures during unmanned missions
* Minimizes manual troubleshooting
* Enables faster maintenance and root cause analysis
* Enhances confidence in long-endurance USV deployments

---

## 4. Intended Users

* **System Integrators:** Embed USV Sentinel into the USV platform during design or retrofit.
* **Mission Operators:** Use diagnostic outputs to verify vessel readiness before and after deployment.
* **Maintenance Teams:** Analyze post-mission logs to identify degrading subsystems and plan proactive maintenance.
* **Command & Control Centers:** Review summaries to assess operational reliability trends across fleets.

---

## 5. High-Level Use Cases

### Use Case 1: Normal Operation

* **Precondition:** USV is on mission and systems are stable.
* **Use Case:** Sentinel monitors onboard conditions and logs system health.
* **Result:** No user intervention required; full log generated for later review.

### Use Case 2: Gradual Thermal Degradation

* **Precondition:** Temperature on a subsystem rises unusually over time.
* **Use Case:** Sentinel identifies the abnormal trend and flags it as a potential failure.
* **Result:** The affected system is scaled down or disabled to avoid damage. Operator notified after mission.

### Use Case 3: Sudden EMI Interference

* **Precondition:** The vessel enters a high-EMI environment.
* **Use Case:** Sentinel detects RF noise signature associated with jamming or interference.
* **Result:** RF subsystems are disabled or rerouted; incident logged for tactical review.

### Use Case 4: Internal Power Instability

* **Precondition:** Propulsion or payload causes sudden current surges.
* **Use Case:** Sentinel detects and responds to power anomalies.
* **Result:** Sentinel temporarily reduces load or disables non-essential systems to stabilize power delivery.

### Use Case 5: Post-Mission Analysis

* **Precondition:** Mission has ended.
* **Use Case:** Sentinel compiles health and fault logs.
* **Result:** Logs are exported to base for review, and optionally used to improve AI prediction models.

---

## 6. High-Level Product Requirements

| **ID**  | **Requirement**                                                                                 | **Rationale**                                                          |
|--------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [USV-1](https://github.com/Dark-Bors/usv-sentinel/issues/2)  | The system shall continuously monitor electrical and environmental conditions onboard the USV. | Early detection depends on real-time awareness of critical parameters. |
| [USV-2](https://github.com/Dark-Bors/usv-sentinel/issues/3)  | The system shall detect and flag anomalous behavior using machine learning or AI logic.        | Enables predictive diagnostics instead of reactive failure handling.   |
| [USV-3](https://github.com/Dark-Bors/usv-sentinel/issues/4)  | The system shall initiate mitigation responses without requiring operator approval.            | Increases autonomy and enables real-time risk containment.             |
| [USV-4](https://github.com/Dark-Bors/usv-sentinel/issues/5)  | The system shall store mission diagnostics for post-operation analysis.                        | Supports root cause analysis and system optimization.                  |
| [USV-5](https://github.com/Dark-Bors/usv-sentinel/issues/6)  | The system shall be embeddable in a wide range of small-to-medium USVs.                        | Enhances system flexibility and broadens applicability.                |
| [USV-6](https://github.com/Dark-Bors/usv-sentinel/issues/7)  | The system shall operate without relying on real-time communication with a control station.    | Ensures system independence in disconnected or jammed environments.    |
| [USV-7](https://github.com/Dark-Bors/usv-sentinel/issues/8)  | The system shall acquire voltage, current, temperature, and other physical parameters.          | Provides input for diagnostics and fault detection.                    |
| [USV-8](https://github.com/Dark-Bors/usv-sentinel/issues/9)  | The system shall preprocess sensor data to remove noise and outliers.                          | Improves AI analysis accuracy.                                         |
| [USV-9](https://github.com/Dark-Bors/usv-sentinel/issues/10) | The system shall evaluate buffered sensor data every 1 second.                                 | Maintains timely diagnostic cycles.                                    |
| [USV-10](https://github.com/Dark-Bors/usv-sentinel/issues/11)| The AI engine shall produce a fault likelihood score between 0–1.                              | Enables threshold-based mitigation logic.                              |
| [USV-11](https://github.com/Dark-Bors/usv-sentinel/issues/12)| The system shall initiate a mitigation response if the fault likelihood exceeds 0.8.           | Automates defensive responses in high-risk scenarios.                  |
| [USV-12](https://github.com/Dark-Bors/usv-sentinel/issues/13)| The system shall disable or isolate non-critical subsystems during faults.                     | Preserves mission-critical operations.                                 |
| [USV-13](https://github.com/Dark-Bors/usv-sentinel/issues/14)| The system shall continue to log data even during or after a mitigation event.                 | Captures context and post-fault behavior.                              |
| [USV-14](https://github.com/Dark-Bors/usv-sentinel/issues/15)| The system shall provide a status flag indicating 'Normal,' 'Warning,' or 'Fault.'             | Communicates system health externally.                                 |
| [USV-15](https://github.com/Dark-Bors/usv-sentinel/issues/16)| The system shall store all logs locally in a non-volatile medium.                              | Retains logs through power cycles.                                     |
| [USV-16](https://github.com/Dark-Bors/usv-sentinel/issues/17)| The system shall package all logs in JSON or CSV format and compress them.                     | Standardizes post-mission analysis formats.                            |
| [USV-17](https://github.com/Dark-Bors/usv-sentinel/issues/18)| The system shall operate in environments from -10°C to +60°C.                                  | Ensures reliability in naval deployment.                               |
| [USV-18](https://github.com/Dark-Bors/usv-sentinel/issues/19)| The system shall tolerate EMI per MIL-STD-461G for military hardware.                          | Complies with defense regulations.                                     |
| [USV-19](https://github.com/Dark-Bors/usv-sentinel/issues/20)| The system shall consume no more than 2 watts average power during operation.                  | Supports energy-limited platforms.                                     |
| [USV-20](https://github.com/Dark-Bors/usv-sentinel/issues/21)| The AI inference latency shall not exceed 1 second per cycle.                                 | Maintains system responsiveness.                                       |
| [USV-21](https://github.com/Dark-Bors/usv-sentinel/issues/22)| The system shall recover to a known safe state within 2 seconds after power restoration.       | Ensures fast fault recovery.                                           |
| [USV-22](https://github.com/Dark-Bors/usv-sentinel/issues/23)| The system shall operate fully offline, with no dependency on cloud or external APIs.          | Enables operation in signal-denied zones.                              |
| [USV-23](https://github.com/Dark-Bors/usv-sentinel/issues/24)| The system shall support integration with USVs running embedded Linux or RTOS.                 | Enhances software compatibility.                                       |
| [USV-24](https://github.com/Dark-Bors/usv-sentinel/issues/25)| The system shall expose a digital status output (3-state: Normal, Warning, Fault).             | Facilitates hardware-level feedback.                                   |
| [USV-25](https://github.com/Dark-Bors/usv-sentinel/issues/26)| The system shall support UART interface for log retrieval and command-line interface.          | Enables serial debugging and diagnostics.                              |
| [USV-26](https://github.com/Dark-Bors/usv-sentinel/issues/27)| The system shall support configuration through a dedicated setup utility.                      | Simplifies deployment and reprogramming.                               |
| [USV-27](https://github.com/Dark-Bors/usv-sentinel/issues/28)| The sensor interface shall support analog input ranges of 0–3.3V.                              | Matches standard sensor output levels.                                 |
| [USV-28](https://github.com/Dark-Bors/usv-sentinel/issues/29)| The log export format shall support structured JSON and flat CSV.                             | Offers flexibility in analysis pipelines.                              |
| [USV-29](https://github.com/Dark-Bors/usv-sentinel/issues/30)| All system actions, predictions, and state changes shall be timestamped.                       | Maintains traceability for audits.                                     |
| [USV-30](https://github.com/Dark-Bors/usv-sentinel/issues/31)| Log entries shall include: timestamp, sensor snapshot, AI output, system state, and action.   | Enables complete fault reconstruction.                                 |
| [USV-31](https://github.com/Dark-Bors/usv-sentinel/issues/32)| Logs shall be checksum-verified for integrity before export.                                  | Ensures trustworthy data.                                              |
| [USV-32](https://github.com/Dark-Bors/usv-sentinel/issues/33)| If memory storage reaches >90% utilization, the system shall alert and discard the oldest logs.| Prevents overflow and ensures continuity.                              |


---

## 7. Product Constraints

* The system must operate autonomously without network access during missions.
* All data collection and inference must execute on a low-power embedded platform.
* The solution must be suitable for marine and military environments (temperature, vibration, EMI).
* Logs must be securely stored and easily exportable post-mission.

---

## 8. Success Criteria

* Early field deployments identify at least one predictive fault before failure occurs.
* Feedback from system integrators validates that integration effort is minimal.
* Maintenance crews report reduction in unscheduled repairs or replacements.
* Logs are found useful for root-cause analysis and future system design improvements.

---

## 9. Out of Scope (for PRD)

* Specific voltage levels, temperature thresholds, or AI inference time
* Circuit design details, firmware architecture, or data formatting protocols
* Compliance verification methods (will be defined in SRS and V\&V plans)

---

## 10. Open Questions

* Will post-mission analysis be manual only, or include automated analytics dashboards?
* Will the AI model retraining be handled in the field or centrally by command infrastructure?
* Should the system provide real-time feedback to an operator if within range?

---

*Note: A detailed System Requirements Document (SRD) will follow to formalize specific measurements, interfaces, thresholds, and test protocols.*
