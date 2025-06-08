# USV Sentinel – System Requirements Document (SRD)

**Version:** 1.0

**Date:** June 2025

**Prepared by:** Chief Systems Engineer

---

## Table of Contents

1. [Revision History](#1-revision-history)
2. [Applicable Documents](#2-applicable-documents)
3. [Introduction – System Architecture](#3-introduction--system-architecture)
4. [Glossary](#4-glossary)
5. [System Requirements](#5-system-requirements)  
   - 5.1 [Functional Requirements](#51-functional-requirements)  
   - 5.2 [Non-Functional Requirements](#52-non-functional-requirements)  
   - 5.3 [Interfaces](#53-interfaces)  
   - 5.4 [Data Logging & Security](#54-data-logging--security)
6. [Verification & Traceability](#6-verification--traceability)

---

## 1. Revision History

| Version | Date      | Description     |
| ------- | --------- | --------------- |
| 1.0     | June 2025 | Initial release |

---

## 2. Applicable Documents

* USV Sentinel – Product Requirements Document (PRD)
* MIL-STD-461G: Requirements for the Control of Electromagnetic Interference

---

## 3. Introduction – System Architecture

The USV Sentinel system is an embedded AI-powered diagnostics and recovery module designed for Unmanned Surface Vessels (USVs). It continuously monitors onboard electronics for signs of degradation or failure, autonomously applies mitigation actions, and supports post-mission fault analysis.

---

## 4. Glossary

* **AI** – Artificial Intelligence
* **EMI** – Electromagnetic Interference
* **RTOS** – Real-Time Operating System
* **SRD** – System Requirements Document
* **USV** – Unmanned Surface Vehicle

---

## 5. System Requirements

### 5.1 Functional Requirements

| **ID** | **Requirement**                                                                                                                | **Rationale**                                                                              |
| ------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| USV-7  | The system shall acquire voltage, current, temperature, and EMI sensor data at intervals not exceeding 100 milliseconds.       | Enables real-time monitoring of mission-critical systems for early fault detection.        |
| USV-8  | The system shall preprocess sensor data to remove noise and normalize values before feeding into the AI engine.                | Ensures data accuracy and consistency for reliable AI inference.                           |
| USV-9  | The system shall evaluate buffered sensor data every 1 second using an onboard AI inference engine.                            | Provides timely diagnosis while balancing computational load on embedded systems.          |
| USV-10 | The AI engine shall produce a fault likelihood score between 0–100% with a confidence value for each analysis cycle.           | Quantifies system health and allows risk-based decision making.                            |
| USV-11 | The system shall initiate a mitigation response if the fault likelihood score exceeds a configurable threshold (default: 85%). | Enables autonomous reaction to prevent fault escalation.                                   |
| USV-12 | The system shall disable or isolate non-critical subsystems if required to preserve operational integrity.                     | Maintains mission continuity by isolating faults and protecting critical operations.       |
| USV-13 | The system shall continue to log data even during or after a mitigation event.                                                 | Maintains complete fault context for later analysis.                                       |
| USV-14 | The system shall provide a status flag indicating "Normal," "Warning," or "Mitigation Active" to the USV controller.           | Supports system-level awareness and integration with other onboard decision systems.       |
| USV-15 | The system shall store all logs locally in a non-volatile memory buffer during missions.                                       | Ensures fault data is preserved for post-mission analysis even after power cycles.         |
| USV-16 | The system shall package all logs in JSON or CSV format and prepare them for export post-mission.                              | Enables human-readable and machine-parseable logs for downstream analysis and diagnostics. |

### 5.2 Non-Functional Requirements

| **ID** | **Requirement**                                                                                             | **Rationale**                                                                                 |
| ------ | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| USV-17 | The system shall operate in environments from -10°C to +60°C without performance degradation.               | Ensures consistent operation in harsh marine and battlefield conditions.                      |
| USV-18 | The system shall tolerate EMI per MIL-STD-461G for military environments.                                   | Guarantees operational reliability in high-EMI settings like radar, RF, and propulsion zones. |
| USV-19 | The system shall consume no more than 2 watts average power during active operation.                        | Complies with power limitations of embedded, unmanned platforms.                              |
| USV-20 | The AI inference latency shall not exceed 1 second per cycle.                                               | Ensures near real-time response to dynamic fault scenarios.                                   |
| USV-21 | The system shall recover to a known safe state within 2 seconds of reboot or brownout.                      | Increases fault tolerance and fast recovery in case of transient power failures.              |
| USV-22 | The system shall operate fully offline, with no dependency on cloud or external network communication.      | Ensures full autonomy during missions without external connectivity.                          |
| USV-23 | The system shall support integration with USVs running embedded RTOS, Linux, or bare-metal control systems. | Enables wide adoption across diverse USV platforms with varying software environments.        |

### 5.3 Interfaces

| **ID** | **Requirement**                                                                                                | **Rationale**                                                                            |
| ------ | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| USV-24 | The system shall expose a digital status output (3-state: Normal, Warning, Mitigation) to the host controller. | Allows other onboard systems to react to Sentinel's state in real time.                  |
| USV-25 | The system shall support UART interface for log retrieval and optional post-mission communication.             | Provides a simple and low-power standard for data access and control.                    |
| USV-26 | The system shall support configuration through a dedicated serial protocol or config file loaded via USB.      | Enables field configuration and updates without complex UI requirements.                 |
| USV-27 | The sensor interface shall support analog input ranges of 0–3.3V and digital (I2C/SPI) inputs.                 | Maximizes compatibility with common onboard sensors in military systems.                 |
| USV-28 | The log export format shall support structured JSON and flat CSV outputs.                                      | Ensures flexibility in downstream data processing and compliance with varied toolchains. |

### 5.4 Data Logging & Security

| **ID** | **Requirement**                                                                                             | **Rationale**                                                                          |
| ------ | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| USV-29 | All system actions, predictions, and state changes shall be timestamped and logged.                         | Supports traceability and forensic review of mission events.                           |
| USV-30 | Log entries shall include: timestamp, sensor snapshot, AI output, and any mitigation action.                | Captures a complete picture of system behavior for diagnosis and training improvement. |
| USV-31 | Logs shall be checksum-verified for integrity before export.                                                | Ensures trustworthiness and authenticity of exported data.                             |
| USV-32 | If memory storage reaches >90% utilization, the system shall overwrite oldest logs using a circular buffer. | Maintains log continuity without manual intervention or storage overflow failures.     |


## 6. Verification & Traceability

Each requirement listed in Section 5 shall be verified through test cases defined in the Verification & Validation (V\&V) Plan. Requirements shall be uniquely tracked via their USV-IDs and referenced in implementation tickets, validation reports, and GitHub issues.

---

*End of Document – USV Sentinel SRD v1.0*
