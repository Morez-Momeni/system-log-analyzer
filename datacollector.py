def collect_logs():
    with open("/var/log/syslog", "r", encoding="utf-8") as source:
        logs = source.read()

    with open("log.txt", "w", encoding="utf-8") as destination:
        destination.write(logs)

if __name__ == "__main__":
    print("This is for collecting syslogs from system")