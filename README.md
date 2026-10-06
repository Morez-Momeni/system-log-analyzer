<div align="center">

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:0f1117,50:18212f,100:00d4aa" width="100%"/>

<br>

<img src="./assets/syslog.jpg" width="100%" alt="Linux System Log Analyzer">

<br>

### Linux System Log Analyzer

**A lightweight Python tool for collecting, parsing, analyzing, and visualizing Linux system logs.**

<br>

</div>

---

## `01` — About

Linux systems continuously generate system logs containing information about processes, services, authentication events, sessions, and other system activity.

This project reads entries from `/var/log/syslog`, extracts structured information using Regular Expressions, analyzes the extracted data, and provides command-line and graphical output.

### Analysis Pipeline

```text
                    /var/log/syslog
                           │
                           ▼
                  ┌─────────────────┐
                  │  Data Collector │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Regex Parser   │
                  └────────┬────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
      Process Log Data          Authentication Data
              │                         │
              ▼                         ▼
         ┌─────────┐              messages.txt
         │ Analyzer│                    │
         └────┬────┘                    │
              │                         │
       ┌──────┼────────┐                │
       ▼      ▼        ▼                ▼
    Process  PID      Time       Authentication
       │      │        │              │
       └──────┼────────┘              │
              │                       │
              └───────────┬───────────┘
                          ▼
                   ┌──────────────┐
                   │ Visualizer   │
                   └──────────────┘
```

---

## `02` — Features

| Category       | Feature                          | Description                                    |
| -------------- | -------------------------------- | ---------------------------------------------- |
| Collection     | **Log Collection**               | Collect logs from `/var/log/syslog`            |
| Parsing        | **Regex Parsing**                | Extract structured fields from raw log entries |
| Process        | **Process Analysis**             | Count and compare process activity             |
| Process        | **PID Analysis**                 | Analyze process IDs and their frequency        |
| Process        | **Process Filtering**            | Investigate a specific process                 |
| Process        | **Process Ranking**              | Find the most and least frequent processes     |
| Time           | **Time Analysis**                | Analyze activity using one-hour ranges         |
| Authentication | **Failed Authentication**        | Detect failed password checks                  |
| Authentication | **Session Analysis**             | Extract session open/close events              |
| Authentication | **User Analysis**                | Count session events per user                  |
| Visualization  | **Process Visualization**        | Visualize process frequency                    |
| Visualization  | **Time Visualization**           | Visualize activity by hour                     |
| Visualization  | **Session Visualization**        | Visualize opened and closed sessions           |
| Visualization  | **User Visualization**           | Visualize session activity per user            |
| Visualization  | **Authentication Visualization** | Visualize failed authentication attempts       |
| CLI            | **Command-Line Interface**       | Control the analyzer using `argparse`          |

---

## `03` — Project Structure

```text
.
├── datacollector.py
├── parser.py
├── analyzer.py
├── visualizer.py
├── main.py
├── log.txt
├── messages.txt
└── assets
    └── syslog.jpg
```

| File                | Responsibility                                                     |
| ------------------- | ------------------------------------------------------------------ |
| `datacollector.py`  | Collect system logs from `/var/log/syslog`                         |
| `parser.py`         | Parse system log entries using Regular Expressions                 |
| `analyzer.py`       | Analyze processes, PIDs, time ranges, authentication, and sessions |
| `visualizer.py`     | Generate Matplotlib visualizations                                 |
| `main.py`           | Command-line interface and feature selection                       |
| `log.txt`           | Automatically generated collected system log                       |
| `messages.txt`      | Extracted authentication-related messages                          |
| `assets/syslog.jpg` | README project banner                                              |

> **Note:** `log.txt` and `messages.txt` are generated during execution and do not need to exist before running the program.

---

## `04` — Data Collection

### `datacollector.py`

The collector reads the Linux system log:

```text
/var/log/syslog
```

and writes the collected data to:

```text
log.txt
```

### Workflow

```text
Linux System
     │
     ▼
/var/log/syslog
     │
     ▼
Data Collector
     │
     ▼
  log.txt
```

### Command

```bash
python main.py --collog
```

### Output

```text
collecting logs from system...

Done
```

| Input             | Output    |
| ----------------- | --------- |
| `/var/log/syslog` | `log.txt` |

---

## `05` — Parsing

### `parser.py`

Raw syslog entries contain multiple fields in a single line.

The parser uses **Regular Expressions** to extract structured information.

### Example Log Entry

```text
2026-09-27T16:52:22.397784+03:30 ubuntu apparmor.systemd[1260]
```

### Extracted Fields

| Field    | Example            |
| -------- | ------------------ |
| Date     | `2026-09-27`       |
| Time     | `16:52:22`         |
| Hostname | `ubuntu`           |
| Process  | `apparmor.systemd` |
| PID      | `1260`             |

The parser also extracts authentication-related log entries and their messages for further analysis.

---

## `06` — Process Analysis

### Process Statistics

The analyzer calculates process-related statistics from the parsed system logs.

| Analysis              | Description                            |
| --------------------- | -------------------------------------- |
| Unique Processes      | Number of different processes          |
| Process Counts        | Number of occurrences for each process |
| Most Repeated Process | Most frequently occurring process      |
| PID Counts            | Number of occurrences for each PID     |
| Most Repeated PID     | Most frequently occurring PID          |

### Example

```text
Process              Occurrences
--------------------------------
systemd                   1240
sshd                       730
NetworkManager             512
```

### Show Statistics

```bash
python main.py --sholog
```

---

### Process Filtering

A specific process can be investigated without displaying the entire dataset.

```bash
python main.py --slog systemd
```

Example:

```text
Process: systemd
Occurrences: 1240
```

| Argument         | Purpose                       |
| ---------------- | ----------------------------- |
| `--slog PROCESS` | Search for a specific process |

---

### Process Ranking

The analyzer can return the most or least frequent processes.

#### Most Frequent

```bash
python main.py --top 10
```

Example:

```text
[
    ('systemd', 1240),
    ('sshd', 730),
    ('NetworkManager', 512)
]
```

#### Least Frequent

```bash
python main.py --tail 10
```

| Command    | Result                     |
| ---------- | -------------------------- |
| `--top N`  | N most frequent processes  |
| `--tail N` | N least frequent processes |

---

## `07` — Time Analysis

The parser preserves the timestamp down to the second.

```text
16:52:22
16:52:23
16:52:25
```

The analyzer first counts activity for exact timestamps and then groups the available timestamps into one-hour ranges.

### Example

| Time Range    | Events |
| ------------- | -----: |
| `00:00–01:00` |     44 |
| `01:00–02:00` |     47 |
| `02:00–03:00` |    151 |
| `17:00–18:00` |     33 |
| `18:00–19:00` |    120 |
| `19:00–20:00` |     21 |
| `20:00–21:00` |     23 |
| `21:00–22:00` |     32 |

Hours without log entries are not included in the result.

### Time Visualization

```bash
python main.py --timeplot
```

The resulting bar chart displays the number of log entries recorded during each hour containing activity.

---

## `08` — Authentication & Session Analysis

Authentication analysis operates on authentication-related messages extracted from the system logs.

The extracted messages are stored in:

```text
messages.txt
```

### Authentication Events

The analyzer currently identifies events such as:

| Event                 | Example                          |
| --------------------- | -------------------------------- |
| Failed Password Check | `password check failed for user` |
| Session Open          | `session opened for user`        |
| Session Close         | `session closed for user`        |

---

### Failed Authentication

`login_failed()` extracts failed password checks and identifies the associated user.

Example:

```text
User: morez
Event: password check failed
```

The result can contain multiple failed attempts for the same user.

### Visualization

```bash
python main.py --authplot
```

This generates a bar chart showing failed authentication attempts per user.

---

### Session Status

`session_status()` extracts:

* Process
* User
* Session status

Example:

| Process                          | User    | Status   |
| -------------------------------- | ------- | -------- |
| `pam_unix(cron:session)`         | `root`  | `opened` |
| `pam_unix(cron:session)`         | `root`  | `closed` |
| `pam_unix(gdm-password:session)` | `morez` | `opened` |
| `pam_unix(gdm-password:session)` | `morez` | `closed` |

---

### Sessions Per User

`session_counter()` counts session events associated with each user.

Example:

| User    | Session Events |
| ------- | -------------: |
| `root`  |             26 |
| `morez` |              2 |

### Visualization

```bash
python main.py --userplot
```

---

### Session Status Summary

`status_counter()` groups session events by status.

Example:

| Status   | Count |
| -------- | ----: |
| `opened` |    27 |
| `closed` |    26 |

### Visualization

```bash
python main.py --sessionplot
```

This generates a bar chart comparing opened and closed sessions.

---

## `09` — Visualization

The project uses **Matplotlib** for graphical analysis.

### Available Visualizations

| Command         | Visualization         | Data                     |
| --------------- | --------------------- | ------------------------ |
| `--plot`        | Process Frequency     | Most frequent processes  |
| `--timeplot`    | Activity by Hour      | Log activity per hour    |
| `--sessionplot` | Session Status        | Opened / closed sessions |
| `--userplot`    | Sessions Per User     | Session events per user  |
| `--authplot`    | Failed Authentication | Failed attempts per user |

### Process Frequency

```bash
python main.py --plot
```

Displays a horizontal bar chart of the most frequent processes.

### Activity by Hour

```bash
python main.py --timeplot
```

Displays the number of log entries recorded in each active hour.

### Session Status

```bash
python main.py --sessionplot
```

Displays the distribution of session states.

### Sessions Per User

```bash
python main.py --userplot
```

Displays session activity grouped by user.

### Failed Authentication

```bash
python main.py --authplot
```

Displays failed authentication attempts grouped by user.

---

## `10` — CLI

The project is controlled through command-line arguments using Python's `argparse`.

| Command          | Argument Type | Purpose                         |
| ---------------- | ------------- | ------------------------------- |
| `--collog`       | Flag          | Collect system logs             |
| `--sholog`       | Flag          | Show process statistics         |
| `--slog PROCESS` | String        | Analyze a specific process      |
| `--top N`        | Integer       | Show N most frequent processes  |
| `--tail N`       | Integer       | Show N least frequent processes |
| `--plot`         | Flag          | Visualize process frequency     |
| `--timeplot`     | Flag          | Visualize activity by hour      |
| `--sessionplot`  | Flag          | Visualize session status        |
| `--userplot`     | Flag          | Visualize sessions per user     |
| `--authplot`     | Flag          | Visualize failed authentication |

### Example

```bash
python main.py --collog --top 10 --timeplot
```

Multiple flags can be supplied in the same execution.

---

## `11` — Installation

### Clone

```bash
git clone <repository-url>
cd <repository-directory>
```

### Install Dependencies

```bash
pip install matplotlib
```

### Standard Library

The project also uses Python standard-library modules:

| Module     | Usage                        |
| ---------- | ---------------------------- |
| `argparse` | Command-line interface       |
| `re`       | Regular Expression parsing   |
| `os`       | Operating system interaction |
| `datetime` | Date/time handling           |

No separate installation is required for standard-library modules.

---

## `12` — Technologies

| Technology              | Role                       |
| ----------------------- | -------------------------- |
| **Python**              | Core programming language  |
| **Linux**               | System and log environment |
| **Regular Expressions** | Log parsing                |
| **argparse**            | CLI interface              |
| **Matplotlib**          | Data visualization         |

---

## `13` — Analysis Overview

The current analyzer provides several different views of the collected system logs.

| Analysis Area  | Available Information                                   |
| -------------- | ------------------------------------------------------- |
| Process        | Unique processes, frequency, ranking                    |
| PID            | PID frequency and ranking                               |
| Time           | Exact timestamps and hourly activity                    |
| Authentication | Failed password checks                                  |
| Sessions       | Opened / closed sessions                                |
| Users          | Session events per user                                 |
| Visualization  | Process, time, session, user, and authentication charts |

### Current CLI Capabilities

```text
Collection
    └── /var/log/syslog → log.txt

Parsing
    ├── Date
    ├── Time
    ├── Hostname
    ├── Process
    ├── PID
    └── Message

Analysis
    ├── Process Analysis
    ├── PID Analysis
    ├── Time Analysis
    └── Authentication / Session Analysis

Visualization
    ├── Process Frequency
    ├── Activity by Hour
    ├── Session Status
    ├── Sessions Per User
    └── Failed Authentication
```

---

## `14` — Future Improvements

| Area           | Possible Improvement                    |
| -------------- | --------------------------------------- |
| Log Sources    | Support additional Linux log files      |
| Log Sources    | Support different log formats           |
| Authentication | Analyze more authentication event types |
| Authentication | Add `sudo` activity analysis            |
| Authentication | Extract IP addresses where available    |
| Security       | Detect suspicious process activity      |
| Security       | Basic anomaly detection                 |
| Filtering      | Filter logs by date and time            |
| Output         | Export results to JSON / CSV            |
| Visualization  | Add additional chart types              |
| CLI            | Add more flexible filtering options     |

---

## `15` — Disclaimer

> This project is intended for learning and educational purposes.
>
> It is a lightweight Linux system log analysis tool and is not intended to replace a production security monitoring system or SIEM.

---

<div align="center">

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:0B0F14,50:18212F,100:00D4AA&section=footer" width="100%">

</div>
