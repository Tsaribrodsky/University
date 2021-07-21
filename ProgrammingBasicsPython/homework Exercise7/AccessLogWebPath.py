# 1. Create a python program that reads apache log file - access_log and from that log file using regular expressions
# extracts and group following information:
# - accessed page path
# And based on that information:
#   - show top 5 most visited web content
import re
from collections import Counter


class AccessLog:
    def apacheLogPathConter(logfile):
        pathRegex = r"(?P<request>[^ \"]+)? HTTP/[0-9.]+\" (?P<status>[0-9]{3})"

        with open(logfile) as f:
            logFile = f.read()
            pathList = re.findall(pathRegex,logFile)
            status = "200"
            pathCount = []
            for x in pathList:
                if status in x:
                    accessed = x
                    pathCount.append(accessed)
            accessedPathCount = Counter(pathCount)
            for k, v in accessedPathCount.most_common(5):
                print("Accessed page path : ", str(k), " Count: ", str(v))

    if __name__ == "__main__":
        apacheLogPathConter("access_log")