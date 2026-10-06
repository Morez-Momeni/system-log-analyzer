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

Linux systems continuously generate logs containing information about processes, services, system activity, authentication events, and user sessions.

This project analyzes two different Linux log sources:

| Log Source          | Purpose                                 |
| ------------------- | --------------------------------------- |
| `/var/log/syslog`   | System, process, PID, and time analysis |
| `/var/log/auth.log` | Authentication and session analysis     |

The project collects raw log entries, extracts structured information using Regular Expressions, analyzes the extracted data, and provides command-line and graphical output.

### Analysis Pipeline

```text
                         Linux Logs
                             │
                  ┌──────────┴──────────┐
                  │                     │
                  ▼                     ▼
           /var/log/syslog       /var/log/auth.log
                  │                     │
                  ▼                     ▼
          Data Collection        Data Collection
                  │                     │
                  ▼                     ▼
             Regex Parser          Auth Parser
                  │                     │
          ┌───────┼───────┐            │
          ▼       ▼       ▼            ▼
       Process   PID     Time    Authentication
          │       │       │            │
          └───────┼───────┘            │
                  │                    │
                  └─────────┬──────────┘
                            ▼
                         Analyzer
                            │
                            ▼
                       Visualizer
```

---

## `02` — Features

| Category       | Feature                           | Description                                          |
| -------------- | --------------------------------- | ---------------------------------------------------- |
| Collection     | **System Log Collection**         | Collect logs from `/var/log/syslog`                  |
| Collection     | **Authentication Log Collection** | Collect authentication logs from `/var/log/auth.log` |
| Parsing        | **Regex Parsing**                 | Extract structured information from raw log entries  |
| Process        | **Process Analysis**              | Count and compare process activity                   |
| Process        | **PID Analysis**                  | Analyze process IDs and their frequency              |
| Process        | **Process Filtering**             | Investigate a specific process                       |
| Process        | **Process Ranking**               | Find the most and least frequent processes           |
| Time           | **Time Analysis**                 | Analyze system activity using one-hour ranges        |
| Authentication | **Failed Authentication**         | Detect failed password checks from `auth.log`        |
| Authentication | **Session Analysis**              | Extract opened and closed sessions                   |
| Authentication | **User Analysis**                 | Count session activity per user                      |
| Visualization  | **Process Visualization**         | Visualize process frequency                          |
| Visualization  | **Time Visualization**            | Visualize activity by hour                           |
| Visualization  | **Session Visualization**         | Visualize opened and closed sessions                 |
| Visualization  | **User Visualization**            | Visualize session activity per user                  |
| Visualization  | **Authentication Visualization**  | Visualize failed authentication attempts             |
| CLI            | **Command-Line Interface**        | Control the analyzer using `argparse`                |

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
| `datacollector.py`  | Collect system and authentication logs                             |
| `parser.py`         | Parse log entries using Regular Expressions                        |
| `analyzer.py`       | Analyze processes, PIDs, time ranges, authentication, and sessions |
| `visualizer.py`     | Generate Matplotlib visualizations                                 |
| `main.py`           | Command-line interface and feature selection                       |
| `log.txt`           | Collected system log                                               |
| `messages.txt`      | Extracted authentication-related messages                          |
| `assets/syslog.jpg` | README project banner                                              |

> **Note:** `log.txt` and `messages.txt` are generated during execution and do not need to exist beforehand.

---

## `04` — Data Collection

### `datacollector.py`

The collector works with two Linux log sources.

### System Logs

```text
/var/log/syslog
```

These logs are used for:

* Process analysis
* PID analysis
* Time analysis

The collected data is stored in:

```text
log.txt
```

### Authentication Logs

```text
/var/log/auth.log
```

These logs are used for:

* Authentication analysis
* Failed password checks
* Session analysis
* User session activity

Authentication-related messages are extracted and stored in:

```text
messages.txt
```

### System Log Workflow

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

### Authentication Log Workflow

```text
Linux Authentication Events
          │
          ▼
/var/log/auth.log
          │
          ▼
   Auth Log Collector
          │
          ▼
     messages.txt
```

### Collection

```bash
python main.py --collog
```

Example output:

```text
collecting logs from system...

Done
```

---

## `05` — Parsing

### `parser.py`

Raw Linux log entries contain multiple fields in a single line.

The parser uses **Regular Expressions** to extract structured information.

### System Log Example

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

These fields are used by the system-log analysis functions.

### Authentication Log Example

Authentication entries can contain events such as:

```text
password check failed for user (morez)
```

or:

```text
pam_unix(cron:session): session opened for user root(uid=0)
```

The authentication parser extracts relevant message information for further analysis.

---

## `06` — Process Analysis

Process analysis is performed on entries collected from:

```text
/var/log/syslog
```

### Process Statistics

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

Time analysis is performed on entries collected from:

```text
/var/log/syslog
```

The parser preserves the timestamp down to the second.

```text
16:52:22
16:52:23
16:52:25
```

The analyzer counts events for exact timestamps and groups them into one-hour ranges.

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

The resulting bar chart displays the number of system-log entries recorded during each hour containing activity.

---

## `08` — Authentication & Session Analysis

Authentication and session analysis is performed using:

```text
/var/log/auth.log
```

This analysis is separate from the system-log analysis performed on `/var/log/syslog`.

### Authentication Events

The analyzer currently works with authentication-related events such as:

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

Multiple failed attempts from the same user can be counted and visualized.

### Visualization

```bash
python main.py --authplot
```

This generates a bar chart showing failed authentication attempts per user.

---

### Session Status

`session_status()` extracts three fields:

| Field   | Description                                |
| ------- | ------------------------------------------ |
| Process | Authentication/session process             |
| User    | User associated with the event             |
| Status  | Session state such as `opened` or `closed` |

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

The project uses **Matplotlib** to visualize the analyzed data.

### Available Visualizations

| Command         | Visualization         | Source              |
| --------------- | --------------------- | ------------------- |
| `--plot`        | Process Frequency     | `/var/log/syslog`   |
| `--timeplot`    | Activity by Hour      | `/var/log/syslog`   |
| `--sessionplot` | Session Status        | `/var/log/auth.log` |
| `--userplot`    | Sessions Per User     | `/var/log/auth.log` |
| `--authplot`    | Failed Authentication | `/var/log/auth.log` |

### Process Frequency

```bash
python main.py --plot
```

Displays a horizontal bar chart of the most frequent processes.

### Activity by Hour

```bash
python main.py --timeplot
```

Displays the number of system-log entries recorded in each active hour.

### Session Status

```bash
python main.py --sessionplot
```

Displays the distribution of opened and closed sessions from authentication logs.

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

| Command          | Argument Type | Purpose                           |
| ---------------- | ------------- | --------------------------------- |
| `--collog`       | Flag          | Collect log data                  |
| `--sholog`       | Flag          | Show process statistics           |
| `--slog PROCESS` | String        | Analyze a specific process        |
| `--top N`        | Integer       | Show N most frequent processes    |
| `--tail N`       | Integer       | Show N least frequent processes   |
| `--plot`         | Flag          | Visualize process frequency       |
| `--timeplot`     | Flag          | Visualize system activity by hour |
| `--sessionplot`  | Flag          | Visualize session status          |
| `--userplot`     | Flag          | Visualize sessions per user       |
| `--authplot`     | Flag          | Visualize failed authentication   |

### Example

```bash
python main.py --collog --top 10 --timeplot
```

Multiple flags can be supplied during the same execution.

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

| Technology              | Role                                      |
| ----------------------- | ----------------------------------------- |
| **Python**              | Core programming language                 |
| **Linux**               | System and authentication log environment |
| **Regular Expressions** | Log parsing                               |
| **argparse**            | CLI interface                             |
| **Matplotlib**          | Data visualization                        |

---

## `13` — Analysis Overview

The project currently provides two main analysis paths based on different Linux log sources.

| Log Source          | Analysis                | Output                   |
| ------------------- | ----------------------- | ------------------------ |
| `/var/log/syslog`   | Process Analysis        | Process frequency        |
| `/var/log/syslog`   | PID Analysis            | PID frequency            |
| `/var/log/syslog`   | Time Analysis           | Activity by hour         |
| `/var/log/auth.log` | Authentication Analysis | Failed authentication    |
| `/var/log/auth.log` | Session Analysis        | Opened / closed sessions |
| `/var/log/auth.log` | User Analysis           | Session events per user  |

### Current Analysis Pipeline

```text
/var/log/syslog
      │
      ├── Process
      ├── PID
      └── Time
             │
             ▼
          Analyzer
             │
             ▼
        Visualization


/var/log/auth.log
      │
      ├── Authentication
      ├── Failed Passwords
      ├── Sessions
      └── Users
             │
             ▼
          Analyzer
             │
             ▼
        Visualization
```

---

## `14` — Future Improvements

| Area           | Possible Improvement                    |
| -------------- | --------------------------------------- |
| Log Sources    | Support additional Linux system logs    |
| Log Sources    | Support different log formats           |
| Authentication | Analyze more authentication event types |
| Authentication | Analyze `sudo` activity                 |
| Authentication | Extract IP addresses where available    |
| Authentication | Improve failed-login analysis           |
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
