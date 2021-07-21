# 2. From the apache error_log file extract error messages and show report
# - classify the type of error
# - when the error had happened
# - which user IP addresses has been affected
import re

# After fierce fighting that is my result.
# I wanted to make loop and print sentence with parts of regex but it didn't work.
class ErrorMessages:
    def apacheLogConter(logfile):
        lineRegex = r"(\[[a-zA-Z]{3} [a-zA-Z]{3} (?:\s[0-9]{1}|[0-9]{2}) [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}\])" \
                        r" (\[[e-r]{5}\]) (\[[c-t]{6} \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]) (File\ .*)"

        with open(logfile) as f:
            logFile = f.read()
            errorList = re.findall(lineRegex, logFile)
            for line in errorList:
                print(line)

    if __name__ == "__main__":
        apacheLogConter("error_log")