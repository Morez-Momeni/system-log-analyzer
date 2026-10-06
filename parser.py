import re 


PATTERN = re.compile(
    r"^(?P<date>.+)T(?P<time>[0-9\:]+).+\s"
    r"(?P<Hostname>[a-zA-Z0-9_\-]+)\s"
    r"(?P<PsName>[a-zA-Z\-.]+)\[(?P<PsId>[0-9]+)\]",
    re.MULTILINE | re.UNICODE
)


LOGIN_PATTERN = re.compile(r"^(?P<date>[\d\-]+)T(?P<time>[\d\:]+).+?"
                           r"\s(?P<hostname>[\w]+)\s(?P<process>\w+)"
                           r"\[(?P<pid>\d+)\]\:(?P<message>.+)",
                           re.MULTILINE | re.UNICODE
)  


with open("log.txt",'r',encoding='utf-8') as file:
    SAMPLE_LOG = file.read()


with open("auth-log.txt" , 'r', encoding="utf-8") as file:
    AUTH_SAMPLE_LOG = file.read()

def extract_processes():

    results = {}
    counter = 1
    for match in PATTERN.finditer(SAMPLE_LOG):
        results[counter] = {
            "date": match.group("date"),
            "time": match.group("time"),
            "hostname": match.group("Hostname"),
            "process": match.group("PsName"),
            "pid": match.group("PsId")
        }   
        counter +=1        
    return results

def extract_auth_logs():

    results = {}
    counter = 1
    for match in LOGIN_PATTERN.finditer(AUTH_SAMPLE_LOG):
        results[counter] = {
            "date": match.group("date"),
            "time": match.group("time"),
            "hostname": match.group("hostname"),
            "process": match.group("process"),
            "pid": match.group("pid"),
            "message": match.group("message"),
            
        }   
        counter +=1        
    return results




if __name__ == "__main__":
    print("This is for parsing data")
