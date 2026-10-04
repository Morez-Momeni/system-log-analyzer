from datetime import datetime
from parser import extract_processes

PROCESSES = extract_processes()


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


