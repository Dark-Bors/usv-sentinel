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

### 5.1 Use Case: Normal Autonomous Operation

**Objective:**  
Ensure stable mission performance with passive monitoring.

**Preconditions:**  
- All subsystems (navigation, propulsion, communication, sensors) are functional.  
- Environmental conditions are within acceptable limits.

**System Behavior:**  
- The onboard Jetson-based Sentinel system collects real-time telemetry and health data.  
- Metrics include voltage, current, temperatures, CPU usage, and network signal quality.  
- Data is logged locally with optional MQTT live telemetry to the cloud dashboard.

**Result:**  
- Mission runs uninterrupted without human intervention.  
- Full system log is generated for post-mission review.  
- Live monitoring is optionally available via remote dashboard.

---

### 5.2 Use Case: Gradual Thermal Degradation

**Objective:**  
Detect and mitigate slow overheating trends before damage occurs.

**Preconditions:**  
- A subsystem (e.g., Jetson module, motor driver) exhibits a long-term rise in temperature beyond expected operational norms.

**System Behavior:**  
- Sentinel uses historical trend analysis and thermal modeling to flag abnormal patterns.  
- Predictive thresholds trigger a warning before hardware alarms activate.  
- Subsystem load is reduced (e.g., lower processing speed or reduced motor power).  
- Event is logged as a proactive thermal mitigation.

**Result:**  
- Hardware damage is prevented.  
- USV continues mission with degraded performance if needed.  
- Operator is informed post-mission with suggested action or service check.

---

### 5.3 Use Case: Sudden Electromagnetic Interference (EMI)

**Objective:**  
Adapt communication subsystems in response to hostile or environmental RF conditions.

**Preconditions:**  
- The USV enters a region with unexpected high RF noise, jamming, or industrial EMI.

**System Behavior:**  
- Sentinel detects packet loss, signal degradation, or spectrum anomalies.  
- EMI patterns are classified using known interference signatures.  
- Affected communication links (e.g., Wi-Fi, LTE) are disabled or rerouted (e.g., SATCOM fallback).  
- Detailed RF log and spectrum snapshots are saved.

**Result:**  
- Communication continuity is maintained through alternative links.  
- Unnecessary retries or power consumption are avoided.  
- EMI event is logged and classified for tactical review.

---

### 5.4 Use Case: Internal Power Instability

**Objective:**  
Protect core systems from power anomalies due to surges or brownouts.

**Preconditions:**  
- High-load modules (e.g., thrusters, lidar) cause sudden current surges or voltage drops.

**System Behavior:**  
- Power Management System monitors battery voltage, current spikes, and thermal activity.  
- Sentinel correlates anomalies with system events and recent commands.  
- Load balancing or subsystem shutdown is initiated (e.g., reduce propulsion or disable camera).  
- Health monitoring continues and recovery logic re-enables modules when safe.

**Result:**  
- System stability is preserved.  
- Mission may continue in reduced capacity.  
- Event details are logged with timestamp and affected components.

---

### 5.5 Use Case: Post-Mission Analysis and Learning

**Objective:**  
Enable fault diagnosis, mission debrief, and predictive model training.

**Preconditions:**  
- Mission is completed or system is idle in base station mode.

**System Behavior:**  
- All logs (sensor data, event history, power trends, fault records) are compiled.  
- Data is exported via MQTT or physical retrieval (e.g., USB).  
- Optional: Logs are used to retrain AI models for predictive maintenance and fault detection.

**Result:**  
- Operators receive actionable mission summaries.  
- System improvements are identified and implemented.  
- Predictive capabilities are continuously refined for future missions.

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
