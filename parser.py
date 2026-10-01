import re 


PATTERN = re.compile(
    r"^(?P<time>[0-9\-\:\.\+T]+)\s"
    r"(?P<Hostname>[a-zA-Z0-9_\-]+)\s"
    r"(?P<PsName>[a-zA-Z\-.]+)\[(?P<PsId>[0-9]+)\]",
    re.MULTILINE | re.UNICODE
)

with open("log.txt",'r',encoding='utf-8') as file:
    SAMPLE_LOG = file.read()

def extract_processes():

    results = {}
    counter = 1
    for match in PATTERN.finditer(SAMPLE_LOG):
        results[counter] = {
            "time": match.group("time"),
            "hostname": match.group("Hostname"),
            "process": match.group("PsName"),
            "pid": match.group("PsId")
        }   
        counter +=1        
    return results

if __name__ == "__main__":
    print("This is for parsing data")
