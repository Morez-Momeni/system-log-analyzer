# Linux System Log Analyzer

A lightweight Python-based tool for analyzing Linux system logs.

This project reads system logs, extracts useful information using regular expressions, and provides different analyses through a command-line interface. It also provides visualizations for process activity, log distribution over time, and authentication/session events.

The project was built as a practical way to understand Linux system logs, regular expressions, log parsing, data analysis, and basic security-oriented log investigation.

---

## Features

### Log Collection

The analyzer can collect the current system log from:

```text
/var/log/syslog
```

The collected log is automatically stored as:

```text
log.txt
```

No manual log preparation is required.

---

### Process Analysis

The project can analyze processes found in the system logs.

Current process analysis includes:

* Total number of process entries
* Unique processes
* Process occurrence counts
* Most frequently occurring process
* PID occurrence counts
* Most frequently occurring PID
* Search for a specific process
* Top N processes
* Least frequent N processes

---

### Time Analysis

The analyzer can also examine when processes appear in the system logs.

It can:

* Extract exact timestamps
* Count occurrences for each timestamp
* Group log activity into hourly ranges
* Show the number of process entries recorded during each hour

Only hours that actually contain log entries are included in the analysis.

---

### Authentication & Session Analysis

The project also extracts authentication-related messages from the system logs.

Current analysis includes:

* Failed password checks
* Authentication-related events
* Session open events
* Session close events
* Session activity per user
* Session status statistics

For example, the analyzer can identify events such as:

```text
password check failed for user
session opened for user
session closed for user
```

Authentication messages are extracted into:

```text
messages.txt
```

and then analyzed separately.

---

## Visualizations

The project uses Matplotlib to visualize the analyzed data.

### Process Visualization

Displays process frequency using a horizontal bar chart.

```bash
python main.py --plot
```

### Time Visualization

Displays the amount of process activity for each hour.

```bash
python main.py --timeplot
```

### Session Status

Shows the number of opened and closed sessions.

```bash
python main.py --sessionplot
```

### Sessions Per User

Shows the number of recorded session events for each user.

```bash
python main.py --userplot
```

### Failed Authentication

Shows failed authentication attempts grouped by user.

```bash
python main.py --authplot
```

---

## Command-Line Interface

The analyzer is controlled through command-line arguments.

| Option           | Description                                |
| ---------------- | ------------------------------------------ |
| `--collog`       | Collect system logs from `/var/log/syslog` |
| `--sholog`       | Show general process statistics            |
| `--plot`         | Display process frequency chart            |
| `--timeplot`     | Display hourly process activity chart      |
| `--sessionplot`  | Display session status chart               |
| `--userplot`     | Display sessions per user                  |
| `--authplot`     | Display failed authentication chart        |
| `--slog PROCESS` | Show information about a specific process  |
| `--top N`        | Show the top N most frequent processes     |
| `--tail N`       | Show the N least frequent processes        |

---

## Examples

### Collect System Logs

```bash
python main.py --collog
```

This reads the system log and creates:

```text
log.txt
```

---

### Show Process Statistics

```bash
python main.py --sholog
```

---

### Analyze a Specific Process

For example:

```bash
python main.py --slog systemd
```

---

### Show Top Processes

```bash
python main.py --top 10
```

---

### Show Least Frequent Processes

```bash
python main.py --tail 10
```

---

### Display Process Chart

```bash
python main.py --plot
```

---

### Display Time Chart

```bash
python main.py --timeplot
```

---

### Analyze Authentication Sessions

```bash
python main.py --sessionplot
```

---

### Analyze Sessions Per User

```bash
python main.py --userplot
```

---

### Analyze Failed Authentication

```bash
python main.py --authplot
```

Multiple analyses can also be requested at the same time:

```bash
python main.py --sholog --plot --timeplot
```

---

## Project Structure

```text
.
├── analyzer.py
├── datacollector.py
├── main.py
├── parser.py
├── visualizer.py
├── log.txt
└── messages.txt
```

### `main.py`

The command-line interface of the project.

It receives user arguments and determines which analysis or visualization should be executed.

### `datacollector.py`

Responsible for collecting the system log from:

```text
/var/log/syslog
```

and storing it in `log.txt`.

### `parser.py`

Responsible for parsing system log entries using regular expressions and extracting structured information such as:

* Date
* Time
* Hostname
* Process name
* PID
* Message

It also extracts authentication-related log entries.

### `analyzer.py`

Contains the main analysis logic.

It handles:

* Process statistics
* PID statistics
* Process frequency
* Time-based analysis
* Authentication analysis
* Session analysis
* Failed authentication detection

### `visualizer.py`

Responsible for visualizing analyzed data using Matplotlib.

Current visualizations include:

* Process frequency
* Hourly activity
* Session status
* Sessions per user
* Failed authentication

---

## How It Works

The project follows a simple analysis pipeline:

```text
Linux System Log
       │
       ▼
/var/log/syslog
       │
       ▼
datacollector.py
       │
       ▼
    log.txt
       │
       ▼
    parser.py
       │
       ├───────────────┐
       ▼               ▼
Process Data      Auth Log Data
       │               │
       ▼               ▼
 analyzer.py      messages.txt
       │               │
       │               ▼
       │          Auth Analysis
       │               │
       └───────┬───────┘
               ▼
         visualizer.py
               │
               ▼
            Charts
```

---

## Technologies

* Python
* Regular Expressions
* argparse
* Matplotlib
* Linux system logs

---

## Project Goals

This project is mainly focused on learning and practicing:

* Linux system log analysis
* Regular expressions
* Python file handling
* Data extraction and transformation
* Command-line interfaces
* Basic authentication/session analysis
* Data visualization
* Security-oriented log investigation

The goal is not to build a full SIEM system, but to create a lightweight tool for understanding and analyzing Linux system logs in a practical way.

---

## Future Improvements

Possible future improvements include:

* More authentication event types
* Better detection of suspicious login activity
* More detailed session analysis
* Filtering logs by date and time
* Exporting analysis results
* Additional visualization options
* Detection of unusual process activity
* Support for additional Linux log sources
* More structured output formats such as JSON or CSV

---

## License

This project is created for educational and learning purposes.
