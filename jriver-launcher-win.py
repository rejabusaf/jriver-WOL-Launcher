
import os
import socket
import subprocess
import datetime

def isTaskRunning(ApplicationName):
    tasklist = os.popen('tasklist /v | findstr "' + ApplicationName + '"')
    if ApplicationName in tasklist:
        return True
    return False

def checkForWOL(InputBin):
    wOLServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    wOLServer.bind(("", wolPort))
    print(datetime.datetime.now(), ":\t", "Listening on 0.0.0.0 for Wake-on-LAN on port", wolPort, '(UDP)')
    wOLData = wOLServer.recv(1024)
    wOLServer.shutdown(0)
    if InputBin in wOLData:
        return True
    else:
        return False

def openApp(ApplicationName, ApplicationPath ,InputBin):
    if checkForWOL(InputBin):
        print(datetime.datetime.now(), ":\t", "Wake-on-LAN received")
        if isTaskRunning(ApplicationName):
            print(datetime.datetime.now(), ":\t", ApplicationName + 'is already running')
            return False
        else:
            print(datetime.datetime.now(), ":\t", 'Starting:', ApplicationName)
            subprocess.call([ApplicationPath + ApplicationName], 0)
            return True

ApplicationName = 'Media Center 21.exe'
ApplicationPath = 'C:\\Program Files (x86)\\J River\\Media Center 21\\'
wolPort = 9
InputBin = b'0'

while (True):
    openApp(ApplicationName, ApplicationPath, InputBin)
