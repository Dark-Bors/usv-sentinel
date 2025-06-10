# USV Sentinel – System Requirements Document (SRD)

**Project Title:** USV Sentinel - AI-Powered Self-Healing diagnostic System

**Version:** 1.0

**Date:** June 2025

**Prepared by:** Boris Eldarov

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

| **ID**                                                        | **Requirement**                                                                                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [USV-7](https://github.com/Dark-Bors/usv-sentinel/issues/8)   | The system shall acquire voltage, current, temperature, and EMI sensor data at intervals not exceeding 100 milliseconds.       |
| [USV-8](https://github.com/Dark-Bors/usv-sentinel/issues/9)   | The system shall preprocess sensor data to remove noise and normalize values before feeding into the AI engine.                |
| [USV-9](https://github.com/Dark-Bors/usv-sentinel/issues/10)  | The system shall evaluate buffered sensor data every 1 second using an onboard AI inference engine.                            |
| [USV-10](https://github.com/Dark-Bors/usv-sentinel/issues/11) | The AI engine shall produce a fault likelihood score between 0–100% with a confidence value for each analysis cycle.           |
| [USV-11](https://github.com/Dark-Bors/usv-sentinel/issues/12) | The system shall initiate a mitigation response if the fault likelihood score exceeds a configurable threshold (default: 85%). |
| [USV-12](https://github.com/Dark-Bors/usv-sentinel/issues/13) | The system shall disable or isolate non-critical subsystems if required to preserve operational integrity.                     |
| [USV-13](https://github.com/Dark-Bors/usv-sentinel/issues/14) | The system shall continue to log data even during or after a mitigation event.                                                 |
| [USV-14](https://github.com/Dark-Bors/usv-sentinel/issues/15) | The system shall provide a status flag indicating "Normal," "Warning," or "Mitigation Active" to the USV controller.           |
| [USV-15](https://github.com/Dark-Bors/usv-sentinel/issues/16) | The system shall store all logs locally in a non-volatile memory buffer during missions.                                       |
| [USV-16](https://github.com/Dark-Bors/usv-sentinel/issues/17) | The system shall package all logs in JSON or CSV format and prepare them for export post-mission.                              |

### 5.2 Non-Functional Requirements

| **ID**                                                        | **Requirement**                                                                                             |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [USV-17](https://github.com/Dark-Bors/usv-sentinel/issues/18) | The system shall operate in environments from -10°C to +60°C without performance degradation.               |
| [USV-18](https://github.com/Dark-Bors/usv-sentinel/issues/19) | The system shall tolerate EMI per MIL-STD-461G for military environments.                                   |
| [USV-19](https://github.com/Dark-Bors/usv-sentinel/issues/20) | The system shall consume no more than 2 watts average power during active operation.                        |
| [USV-20](https://github.com/Dark-Bors/usv-sentinel/issues/21) | The AI inference latency shall not exceed 1 second per cycle.                                               |
| [USV-21](https://github.com/Dark-Bors/usv-sentinel/issues/22) | The system shall recover to a known safe state within 2 seconds of reboot or brownout.                      |
| [USV-22](https://github.com/Dark-Bors/usv-sentinel/issues/23) | The system shall operate fully offline, with no dependency on cloud or external network communication.      |
| [USV-23](https://github.com/Dark-Bors/usv-sentinel/issues/24) | The system shall support integration with USVs running embedded RTOS, Linux, or bare-metal control systems. |

### 5.3 Interfaces

| **ID**                                                        | **Requirement**                                                                                                |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [USV-24](https://github.com/Dark-Bors/usv-sentinel/issues/25) | The system shall expose a digital status output (3-state: Normal, Warning, Mitigation) to the host controller. |
| [USV-25](https://github.com/Dark-Bors/usv-sentinel/issues/26) | The system shall support UART interface for log retrieval and optional post-mission communication.             |
| [USV-26](https://github.com/Dark-Bors/usv-sentinel/issues/27) | The system shall support configuration through a dedicated serial protocol or config file loaded via USB.      |
| [USV-27](https://github.com/Dark-Bors/usv-sentinel/issues/28) | The sensor interface shall support analog input ranges of 0–3.3V and digital (I2C/SPI) inputs.                 |
| [USV-28](https://github.com/Dark-Bors/usv-sentinel/issues/29) | The log export format shall support structured JSON and flat CSV outputs.                                      |

### 5.4 Data Logging & Security

| **ID**                                                        | **Requirement**                                                                                             |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [USV-29](https://github.com/Dark-Bors/usv-sentinel/issues/30) | All system actions, predictions, and state changes shall be timestamped and logged.                         |
| [USV-30](https://github.com/Dark-Bors/usv-sentinel/issues/31) | Log entries shall include: timestamp, sensor snapshot, AI output, and any mitigation action.                |
| [USV-31](https://github.com/Dark-Bors/usv-sentinel/issues/32) | Logs shall be checksum-verified for integrity before export.                                                |
| [USV-32](https://github.com/Dark-Bors/usv-sentinel/issues/33) | If memory storage reaches >90% utilization, the system shall overwrite oldest logs using a circular buffer. |




## 6. Verification & Traceability

Each requirement listed in Section 5 shall be verified through test cases defined in the Verification & Validation (V\&V) Plan. Requirements shall be uniquely tracked via their USV-IDs and referenced in implementation tickets, validation reports, and GitHub issues.

---

*End of Document – USV Sentinel SRD v1.0*
