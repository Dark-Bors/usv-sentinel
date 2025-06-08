import subprocess

# All USV requirements from PRD and SRD
requirements = [
    ("USV-1", "The system shall continuously monitor electrical and environmental conditions onboard the USV."),
    ("USV-2", "The system shall detect and flag anomalous behavior using machine learning or AI logic."),
    ("USV-3", "The system shall initiate mitigation responses without requiring operator approval."),
    ("USV-4", "The system shall store mission diagnostics for post-operation analysis."),
    ("USV-5", "The system shall be embeddable in a wide range of small-to-medium USVs."),
    ("USV-6", "The system shall operate without relying on real-time communication with a control station."),
    ("USV-7", "The system shall acquire voltage, current, temperature, and EMI sensor data at intervals not exceeding 100 milliseconds."),
    ("USV-8", "The system shall preprocess sensor data to remove noise and normalize values before feeding into the AI engine."),
    ("USV-9", "The system shall evaluate buffered sensor data every 1 second using an onboard AI inference engine."),
    ("USV-10", "The AI engine shall produce a fault likelihood score between 0–100% with a confidence value for each analysis cycle."),
    ("USV-11", "The system shall initiate a mitigation response if the fault likelihood score exceeds a configurable threshold (default: 85%)."),
    ("USV-12", "The system shall disable or isolate non-critical subsystems if required to preserve operational integrity."),
    ("USV-13", "The system shall continue to log data even during or after a mitigation event."),
    ("USV-14", "The system shall provide a status flag indicating 'Normal,' 'Warning,' or 'Mitigation Active' to the USV controller."),
    ("USV-15", "The system shall store all logs locally in a non-volatile memory buffer during missions."),
    ("USV-16", "The system shall package all logs in JSON or CSV format and prepare them for export post-mission."),
    ("USV-17", "The system shall operate in environments from -10°C to +60°C without performance degradation."),
    ("USV-18", "The system shall tolerate EMI per MIL-STD-461G for military environments."),
    ("USV-19", "The system shall consume no more than 2 watts average power during active operation."),
    ("USV-20", "The AI inference latency shall not exceed 1 second per cycle."),
    ("USV-21", "The system shall recover to a known safe state within 2 seconds of reboot or brownout."),
    ("USV-22", "The system shall operate fully offline, with no dependency on cloud or external network communication."),
    ("USV-23", "The system shall support integration with USVs running embedded RTOS, Linux, or bare-metal control systems."),
    ("USV-24", "The system shall expose a digital status output (3-state: Normal, Warning, Mitigation) to the host controller."),
    ("USV-25", "The system shall support UART interface for log retrieval and optional post-mission communication."),
    ("USV-26", "The system shall support configuration through a dedicated serial protocol or config file loaded via USB."),
    ("USV-27", "The sensor interface shall support analog input ranges of 0–3.3V and digital (I2C/SPI) inputs."),
    ("USV-28", "The log export format shall support structured JSON and flat CSV outputs."),
    ("USV-29", "All system actions, predictions, and state changes shall be timestamped and logged."),
    ("USV-30", "Log entries shall include: timestamp, sensor snapshot, AI output, and any mitigation action."),
    ("USV-31", "Logs shall be checksum-verified for integrity before export."),
    ("USV-32", "If memory storage reaches >90% utilization, the system shall overwrite oldest logs using a circular buffer."),
]

# Loop through and create each issue via GitHub CLI
for req_id, req_text in requirements:
    title = f"[{req_id}] {req_text[:60]}..."
    body = f"**Requirement ID**: {req_id}\n\n**Description**:\n{req_text}\n\n**Source**: Refer to PRD/SRD documents."
    cmd = [
        "gh", "issue", "create",
        "--title", title,
        "--body", body,
        "--label", "requirement"
    ]
    print(f"Creating issue: {title}")
    subprocess.run(cmd)
