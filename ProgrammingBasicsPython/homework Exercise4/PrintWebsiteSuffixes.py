# ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# Write a python program to print website suffixes (com , org , net ,in) from this list

def printSuffixes(websiteList):
    domainList = []
    for i in websiteList:
        domain = i.split((".")[-1])
        domainList.append(domain[-1])
    print(domainList)

websiteList = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
printSuffixes(websiteList)