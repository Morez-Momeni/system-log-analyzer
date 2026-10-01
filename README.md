<div align="center">
<br>

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:0f1117,50:18212f,100:00d4aa&text=SYSTEM%20LOG%20ANALYZER&fontColor=ffffff&fontSize=38&fontAlignY=38&desc=Understand%20your%20Linux%20logs&descAlignY=60&descSize=16" width="100%"/>

<br>

<img src="./assets/syslog.jpg" width="100%" alt="System Log Analyzer">

<br>

# SYSTEM LOG ANALYZER

### Linux Logs · Regex Parsing · Analysis · Visualization

<br>

A Python-based system for collecting, parsing, analyzing, and visualizing Linux system logs.

<br>


**Collect → Parse → Analyze → Visualize**

</div>

---

## About

**System Log Analyzer** is a Python project built to explore how Linux system logs can be processed programmatically.

The project focuses on taking raw Linux log data and turning it into structured information that can be analyzed and visualized.

Instead of treating a log file as a large block of text, the project breaks it down into useful fields such as:

* Timestamp
* Hostname
* Process name
* Process ID
* Process frequency
* PID frequency

Regular expressions are used as the main parsing mechanism.

The project is intentionally being developed incrementally, with each component built to solve a specific part of the log-analysis process.

---

## Pipeline

```text
                    LINUX SYSTEM LOG
                           │
                           ▼
                    ┌─────────────┐
                    │  Collector  │
                    └──────┬──────┘
                           │
                           ▼
                        log.txt
                           │
                           ▼
                    ┌─────────────┐
                    │    Parser   │
                    │    Regex    │
                    └──────┬──────┘
                           │
                           ▼
                  Structured Log Data
                           │
                           ▼
                    ┌─────────────┐
                    │   Analyzer  │
                    └──────┬──────┘
                           │
                           ▼
                  Process / PID Data
                           │
                           ▼
                    ┌─────────────┐
                    │ Visualizer  │
                    └─────────────┘
                           │
                           ▼
                       Charts
```

The goal is simple:

> **Turn raw Linux logs into information that can actually be understood.**

---

## Current Features

| Component       | Purpose                               | Status |
| --------------- | ------------------------------------- | :----: |
| `collector.py`  | Collect Linux system logs             |    ✅   |
| `parser.py`     | Extract structured fields using Regex |    ✅   |
| `analyzer.py`   | Analyze processes and PIDs            |    ✅   |
| `visualizer.py` | Visualize analyzed data               |   🚧   |
| `main.py`       | Main application entry point          |   🚧   |

### Current parsing fields

The parser currently extracts:

```text
Timestamp
Hostname
Process Name
Process ID
```

For example, a log entry such as:

```text
2026-09-27T16:52:22.397784+03:30 ubuntu apparmor.systemd[1260]: Warning: ...
```

can be interpreted as:

```text
Time     → 2026-09-27T16:52:22.397784+03:30
Hostname → ubuntu
Process  → apparmor.systemd
PID      → 1260
```

---

## Project Structure

```text
system-log-analyzer/
│
├── assets/
│   └── system-log-analyzer-banner.png
│
├── collector.py
├── parser.py
├── analyzer.py
├── visualizer.py
├── main.py
│
├── log.txt
├── requirements.txt
├── .gitignore
└── README.md
```

### `collector.py`

Responsible for collecting Linux system logs.

The collected data is written to:

```text
log.txt
```

> `log.txt` is generated automatically by the collector and does not need to be created manually.

---

### `parser.py`

Responsible for converting raw log lines into structured data.

Regex is used to identify important components of each log entry.

The extracted information currently includes:

```text
time
hostname
process
pid
```

---

### `analyzer.py`

Responsible for analyzing the structured log data.

Current analysis includes:

* Process occurrence counting
* PID occurrence counting
* Finding processes that appear only once
* Finding the most repeated process
* Finding the most repeated PID

The analysis layer is intentionally kept simple while the underlying concepts are being developed.

---

### `visualizer.py`

Responsible for presenting analysis results visually.

Current visualization work focuses on representing process distribution using `Matplotlib`.

Future visualizations may include:

```text
Process frequency
PID frequency
Time-based activity
Event distribution
```

---

### `main.py`

`main.py` will eventually become the main entry point of the project.

The goal is to connect the individual components:

```text
Collector
   ↓
Parser
   ↓
Analyzer
   ↓
Visualizer
```

This part of the project is currently under development.

---

## Why Regular Expressions?

Linux logs are primarily text.

That makes them a useful environment for learning how to extract structured information from semi-structured data.

For example:

```text
2026-09-27T16:52:22.397784+03:30 ubuntu apparmor.systemd[1260]
```

contains several pieces of information inside a single string.

A regular expression can describe the structure:

```regex
^(?P<time>[0-9\-:\.+T]+)\s
(?P<Hostname>[a-zA-Z0-9_\-]+)\s
(?P<PsName>[a-zA-Z\-.]+)
\[(?P<PsId>[0-9]+)\]
```

The purpose is not simply to write a complicated Regex.

The purpose is to understand how structured information can be extracted from real system data.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Morez-Momeni/system-log-analyzer.git
cd system-log-analyzer
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

The project is currently being developed component by component.

The current workflow can be thought of as:

```text
Linux Log
   ↓
collector.py
   ↓
log.txt
   ↓
parser.py
   ↓
Structured Data
   ↓
analyzer.py
   ↓
Analysis
   ↓
visualizer.py
   ↓
Visualization
```

The final interface will be provided through `main.py`.

---

## Data Source

The initial version of the project works with Linux system logs such as:

```text
/var/log/syslog
```

The collector creates a local:

```text
log.txt
```

file containing the collected log data.

This keeps the rest of the project independent from the original system log source.

---

## Future Development

The project is designed to grow beyond a single log source.

Possible future sources include:

```text
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
journalctl
```

Possible future analysis:

| Area           | Possible Analysis                  |
| -------------- | ---------------------------------- |
| Processes      | Frequency and activity             |
| PIDs           | Process occurrence                 |
| Authentication | Login / authentication events      |
| Kernel         | Kernel-related events              |
| Time           | Activity over time                 |
| Errors         | Error frequency                    |
| Warnings       | Warning frequency                  |
| Security       | Suspicious authentication patterns |
| Visualization  | Advanced log dashboards            |

The project will evolve as new Linux logging and security concepts are learned.

---

## Project Philosophy

This project is not intended to be a full-featured SIEM.

It is a learning-oriented system built around a simple idea:

> **Don't just read logs. Understand them.**

The project combines several areas of practical learning:

```text
Python
   +
Linux
   +
Regular Expressions
   +
Data Analysis
   +
Visualization
   +
Security Concepts
```

Each component exists for a reason and is built incrementally.

---

## Technologies

* **Python**
* **Linux**
* **Regular Expressions**
* **Matplotlib**
* **Git / GitHub**

---

## Project Status

🚧 **Actively under development**

The project is being developed incrementally.

The current implementation focuses on:

```text
Collection
Parsing
Process Analysis
PID Analysis
Visualization
```

The architecture is intentionally open so that additional Linux log sources and security-oriented analysis can be added later.

---

<div align="center">

### SYSTEM LOG ANALYZER

**Linux logs are data.
Regex gives them structure.
Analysis gives them meaning.**

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:0B0F14,50:18212F,100:00D4AA&section=footer" width="100%">

</div>

