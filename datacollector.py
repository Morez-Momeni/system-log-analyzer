from parser import extract_auth_logs

AUTH_LOGS_PROCESS = extract_auth_logs()



def collect_logs():
    with open("/var/log/syslog", "r", encoding="utf-8") as source:
        logs = source.read()

    with open("log.txt", "w", encoding="utf-8") as destination:
        destination.write(logs)

def collect_auth_log():
    with open("/var/log/auth.log") as source:
        logs = source.read()
        
    with open("auth-log.txt", "w", encoding="utf-8") as destination:
        destination.write(logs)

def wrrite_message():
    for m in AUTH_LOGS_PROCESS.values():
        with open("messages.txt" , "w") as file:
            file.write(f"{m['message']}\n")



if __name__ == "__main__":
    collect_logs()
    collect_auth_log()
    wrrite_message()
    print("This is for collecting syslogs from system")