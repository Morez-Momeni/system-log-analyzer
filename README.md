<div align="center">

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:0f1117,50:18212f,100:00d4aa&" width="100%"/>

<br>


<img src="./assets/syslog.jpg" width="100%" alt="System Log Analyzer">


</div>

---

# Linux System Log Analyzer

A lightweight Linux system log analysis tool written in Python.

This project collects system logs, parses process-related information from them, analyzes process frequency, and provides a visual representation of the most frequently occurring processes.

The project was built as a practical exercise in **Linux system logs, Regular Expressions, Python data processing, and basic security-oriented log analysis**.

---

## Overview

Linux systems generate a large amount of information through system logs. These logs can contain useful information about running services, processes, authentication events, system activity, and potential problems.

This project provides a simple pipeline for working with those logs:

```text
System Logs
     │
     ▼
Data Collector
     │
     ▼
Parser / Regex
     │
     ▼
Analyzer
     │
     ├── Process Statistics
     │
     └── PID Statistics
     │
     ▼
Visualization
```

The project currently focuses on extracting process information and finding the processes that appear most frequently in the collected logs.

---

## Features

* Collect Linux system logs from `/var/log/syslog`
* Automatically create a local `log.txt` file
* Parse log entries using Regular Expressions
* Extract:

  * Timestamp
  * Hostname
  * Process name
  * Process ID
* Count process occurrences
* Find unique processes
* Find the most frequently occurring process
* Count PID occurrences
* Find the most frequently occurring PID
* Visualize the top 10 most frequent processes
* Command-line interface using `argparse`

---

## Project Structure

```text
.
├── datacollector.py
├── parser.py
├── analyzer.py
├── visualizer.py
├── main.py
└── log.txt
```

### `datacollector.py`

Responsible for collecting the system logs.

The collector reads the system log from:

```text
/var/log/syslog
```

and creates:

```text
log.txt
```

in the project directory.

The log file does not need to be manually added to the repository. It is generated when the collection command is executed.

---

### `parser.py`

The parser processes the collected log and extracts structured information using Regular Expressions.

The current parser extracts information such as:

```text
Timestamp
Hostname
Process Name
Process ID
```

For example, a log entry containing:

```text
apparmor.systemd[1260]
```

can be parsed into:

```text
Process: apparmor.systemd
PID: 1260
```

The extracted information is then passed to the analyzer.

---

### `analyzer.py`

The analyzer works with the parsed process information.

It currently provides statistics such as:

* Unique processes
* Number of occurrences of each process
* Most frequently occurring process
* PID occurrence counts
* Most frequently occurring PID

For example, the analyzer can produce information conceptually similar to:

```text
Process              Occurrences
--------------------------------
systemd              1240
sshd                  730
NetworkManager        512
...
```

These statistics are also used by the visualization component.

---

### `visualizer.py`

The visualization component uses **Matplotlib** to display the top 10 most frequently occurring processes.

The processes are sorted by their number of occurrences and displayed as a horizontal bar chart.

Each bar also contains its exact occurrence count.

The resulting visualization looks conceptually like:

```text
systemd             ███████████████████  1240
sshd                ███████████           730
NetworkManager      ███████               512
...
```

This makes it easier to quickly identify which processes appear most frequently in the system logs.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

Install the required Python package:

```bash
pip install matplotlib
```

The project also uses Python's standard library modules such as:

```text
argparse
re
os
```

which do not require separate installation.

---

## Usage

The project is controlled through command-line arguments.

### Collect Logs

To collect the system logs:

```bash
python main.py --collog
```

This command reads the system log and creates:

```text
log.txt
```

Output:

```text
collecting logs from system...
Done
```

---

### Show Statistics

To analyze the collected logs:

```bash
python main.py --sholog
```

This runs the analyzer and displays the collected process statistics.

---

### Show Visualization

To generate the process frequency chart:

```bash
python main.py --plot
```

This displays the **Top 10 Most Frequent Processes** using a horizontal bar chart.

---

### Collect and Analyze

The options can also be combined.

For example:

```bash
python main.py --collog --sholog --plot
```

This will:

1. Collect the system logs
2. Analyze the parsed process information
3. Display the visualization

---

## Technologies

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| Python              | Main programming language         |
| Regular Expressions | Log parsing                       |
| Linux               | Source system and log environment |
| `argparse`          | Command-line interface            |
| Matplotlib          | Data visualization                |

---

## What I Learned

This project was built to practice working with real Linux system data rather than artificial input.

Through the project, I practiced:

* Reading Linux system logs
* Working with `/var/log/syslog`
* Designing Regular Expressions for structured log extraction
* Processing large amounts of log entries
* Counting and comparing process occurrences
* Working with Python dictionaries
* Building command-line interfaces
* Creating basic security-oriented data visualizations
* Separating data collection, parsing, analysis, and visualization into different modules

---

## Future Improvements

Possible future improvements include:

* Support for additional Linux log files
* More log formats and parsing patterns
* Filtering logs by date and time
* Authentication event analysis
* Failed login detection
* Detection of unusual process activity
* More visualization types
* Exporting analysis results to JSON or CSV
* Adding command-line filters
* Improving the parser for different Linux distributions

---

## Disclaimer

This project is intended for **learning and educational purposes**.

It is a simple log-analysis project and should not be considered a complete security monitoring or SIEM solution.


<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:0B0F14,50:18212F,100:00D4AA&section=footer" width="100%">

</div>

