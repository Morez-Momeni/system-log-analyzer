import re
from datetime import datetime
from parser import extract_processes, extract_auth_logs

PROCESSES = extract_processes()
AUTH_LOGS_PROCESS = extract_auth_logs()

def uniqe_process():
    uniqe_ps = []
    counter = 0 
    for ps in PROCESSES.values():
        for psc in PROCESSES.values():
            if ps["process"] == psc["process"]:
                counter+=1
                if counter > 1:
                    counter = 0
                    break
        else:
            uniqe_ps.append(ps["process"])
    return uniqe_ps
    
def ps_counter():
    ps_val_count = {}
    counted_ps = []
    counter = 0
    for ps in PROCESSES.values():
        if ps['process'] in counted_ps:
            continue
        for psc in PROCESSES.values():
            if ps["process"] == psc["process"]:
                counted_ps.append(ps["process"])
                counter += 1
        else:
            ps_val_count[ps["process"]] = counter
            counter = 0
    return ps_val_count
    
def most_repeated_ps():
    process = ps_counter()
    highest_count = max(process.values())
    most_repeated_process = []
    for ps_key in process.keys():
        if process[ps_key] == highest_count:
            most_repeated_process.append(ps_key)
    return (most_repeated_process) , highest_count

def psid_counter():
    counter = 0
    psid = {}
    counted_psid = []
    for ps in PROCESSES.values():
        if ps['pid'] in counted_psid:
            continue
        for psc in PROCESSES.values():
            if ps['pid'] == psc['pid']:
                counted_psid.append(ps['pid'])
                counter += 1
        else:
            psid[ps["pid"]] = counter
            counter = 0
    return psid


def most_repeated_psid():
    process = psid_counter()
    highest_count = max(process.values())
    most_repeated_processid = []
    for ps_key in process.keys():
        if process[ps_key] == highest_count:
            most_repeated_processid.append(ps_key)
    return (most_repeated_processid) , highest_count

def statistics():
    unique_processes = uniqe_process()
    process_counts = ps_counter()
    most_processes, most_process_count = most_repeated_ps()

    pid_counts = psid_counter()
    most_pids, most_pid_count = most_repeated_psid()

    print(f"Unique Processes: {len(unique_processes)}")
    print(f"Total Processes: {len(PROCESSES)}")

    print("\nProcess Counts:")
    for process, count in process_counts.items():
        print(f"  {process}: {count}")

    print("\nMost Repeated Process:")
    print(f"  Process: {most_processes}")
    print(f"  Count: {most_process_count}")

    print("\nPID Counts:")
    for pid, count in pid_counts.items():
        print(f"  PID {pid}: {count}")

    print("\nMost Repeated PID:")
    print(f"  PID: {most_pids}")
    print(f"  Count: {most_pid_count}")



def special_log(log_name: str):

    log_val = ps_counter()

    result = log_val.get(log_name)

    if result is None:
        print(f"Process '{log_name}' not found.")
        return

    print(f"Process: {log_name}")
    print(f"Occurrences: {result}")

def top_ps(length = 10):
    process = ps_counter()
    process = sorted(process.items(),key=lambda item:item[1],reverse=True)
    print(process[:length])

def tail_ps(length = 10):
    process = ps_counter()
    process = sorted(process.items(),key=lambda item:item[1])
    print(process[:length])


def ps_and_time():
    
    time_count = {}
    counted_time = []
    counter = 0 
    for ps in PROCESSES.values():
        if ps['time'] in counted_time:
            continue
        for ps2 in PROCESSES.values():
            if ps['time'] == ps2['time']:
                counted_time.append(ps['time'])
                counter += 1
        else:
            time_count[ps["time"]] = counter
            counter = 0
    return time_count


def define_range():
    process = ps_and_time()
    ranges = {}
    for ps in process.keys():
        start_time = int(ps[:2])
        finish_time = start_time + 1
        ranges[ps] = (start_time,finish_time)
    return ranges        


def summry_times():
    process = define_range()
    processes_per_hour = {}
    used_time_key = []
    counter = 0
    for pst in process.values():
        if pst in used_time_key:
            continue
        for pst2 in process.values():
            if pst == pst2:
                used_time_key.append(pst)
                counter += 1
        else:
            processes_per_hour[pst] = counter
            counter = 0 
    return processes_per_hour

def wrrite_message():
    for m in AUTH_LOGS_PROCESS.values():
        with open("messages.txt" , "w") as file:
            file.write(f"{m['message']}\n")



    
def login_failed():
        result = [] 
        with open("messages.txt" , 'r') as file:
            SAMPLE = file.read()
     
        regex = re.compile(r"^ +(?P<event>password check failed).+\((?P<user>\w+)", re.MULTILINE | re.UNICODE)
        for match in regex.finditer(SAMPLE):
            result.append((match.group('user'),match.group('event')))
        return result

def session_status():
        result = [] 
        with open("messages.txt" , 'r') as file:
            SAMPLE = file.read()
     
        regex = re.compile(r"^ +(?P<process>[\w\(\)\:]+)\:\ssession\s(?P<stat>\w+).+user\s(?P<user>\w+)",
                        re.MULTILINE | re.UNICODE)
        for match in regex.finditer(SAMPLE):
            result.append((match.group('process'),match.group('user'),match.group('stat')))
        return result

def session_counter():
        data = session_status()
        result = {}
        counter = 0
        counted = []
        for u in data:
            if u[1] in counted:
                continue
            for us in data:
                if u[1] == us[1]:
                    counted.append(us[1])
                    counter += 1    
            else:
                result[u[1]] = counter 
                counter = 0 
        return result

def status_counter():
        data = session_status()
        result = {}
        counter = 0
        counted = []
        for u in data:
            if u[2] in counted:
                continue
            for us in data:
                if u[2] == us[2]:
                    counted.append(us[2])
                    counter += 1    
            else:
                result[u[2]] = counter 
                counter = 0 
        return result
    
def show_report():

        failed = login_failed()
        sessions = session_status()
        users = session_counter()
        statuses = status_counter()

        print("\n" + "=" * 55)
        print("           AUTHENTICATION ANALYSIS")
        print("=" * 55)

        print("\n[ Failed Passwords ]")

        if failed:
            for user, event in failed:
                print(f"  User: {user:<15} Event: {event}")
        else:
            print("  No failed password attempts found.")

        print("\n[ Session Events ]")
        print(f"  {'Process':<35} {'User':<15} {'Status'}")
        print("  " + "-" * 65)

        for process, user, status in sessions:
            print(f"  {process:<35} {user:<15} {status}")

        print("\n[ Sessions Per User ]")
        for user, count in users.items():
            print(f"  {user:<20} {count}")

        print("\n[ Session Status Summary ]")
        for status, count in statuses.items():
            print(f"  {status:<20} {count}")

        print("\n" + "=" * 55)
 