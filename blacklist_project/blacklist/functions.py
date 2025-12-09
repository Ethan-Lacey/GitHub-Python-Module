import sys
import os
import platform
import re
import argparse

#the address used to block the suspect FQDN
dns_blackHole = "0.0.0.0"




#Function: Determine the HOSTS file path
getHostPath():
#determine the path to the HOSTS file, irrespective of the OS
    if system == "Windows":
       return "C:\\Windows\\System32\\drivers\\etc\\hosts"
    elif system == "Linux":
       return "/etc/hosts"
    else:
       #for MacOS and other OSes
       return "/etc/hosts"
   
pathToHost = getHostPath()



#Function: Locate entries in the Hosts file
def findHost(FQDN, lines):
    hostRE = re.compile("\^\\s*(?:0\.0\.0\.0|127\.0.\0\.1)\s+" + re.escape(FQDN.lower()) + "(?:\s+#.\*)?$")

    for i, line in enumerate(lines):
        if hostRE.search(line.strip().lower()):
            return i, line.strip()

    hostfulWWW = 'www." + FQDN.lower()
    if hostfulWWW in line.lower() and re.search("\\b" +re.escape(hostfulWWW) + "\\b", line.lower()):
        return i, line.strip()
        



#Function: Read the Hosts file
def hosts_file():
    try:
        with open(pathToHost, 'r') as hostFile:
            return hostFile.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found in {pathToHost}")



#Function: Write to the Hosts file
def writeHostsFile(hostsPath, fileContent):
    try:
        with open(hostsPath, 'w') as hostsFile:
            hostsFile.writelines(fileContent)
    except PermissionError:
        raise PermissionError("This action requires admin privleges")    



#Function: Block a host
def blockHost(FQDN, hostsPath):
    hostsPath = getHostPath()
    
    lines = readHostFile(hostsPath)
    index = findHost(lines, FQDN)

    if index is not None:
      return False, print(f"An entry for {FQDN} already exists"

    addEntry = [
      f"{dns_blackHole} {FQDN}\n"
      f"{dns_blackHole} www.{FQDN}\n"
    ]

    lines.extend(addEntry)
    writeHostsFile(hostsPath, lines)
    


#Function: Unblock a host
def removeHost(FQDN, hostsPath=None)
    hostsPath = getHostPath()
    
    lines = readHostsFile(hostsPath)
    index = findHostEntry(lines, FQDN)

    if index is None:
        return False, print(f"Entry for {FQDN} does not exist.")

    del lines[index]
    writeHostsFile(hostsPath, lines)

    return True, print(f"{FQDN} has been removed from Blocked Hosts."
                       


    





