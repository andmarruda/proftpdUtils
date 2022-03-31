#This is a utility to read xferlog of Proftpd server with python. Beta version 1.
#Powered by Anderson Arruda < anderson@sysborg.com.br >
#The purpose is to insert in a relational database as PostgreSQL and MySQL to futher analyzis and server administration tools
#versoin 1.0.0
#Beta Version

import re
from datetime import datetime
from os.path import exists

def xferlogDateToTimeStamp(dateStr, pattern='%a %b %d %H:%M:%S %Y'):
    return str(datetime.strptime(dateStr, pattern))

def xferlogMatchColumn(xferlogLine):
    names = [
        'current-time', 'transfer-time', 'remote-host', 
        'file-size', 'filename', 'transfer-type', 'special-action-flag', 
        'direction', 'access-mode', 'username', 'service-name', 
        'authentication-method', 'authenticated-user-id', 'completion-status'
    ]
    
    regx = r"(^(([a-zA-Z]{3}\s){2}[0-9]{2}\s([0-9]{2}\:){2}[0-9]{2}\s[0-9]{4}))|((?<=\s)(?<!$1)).*?(?=\s|$)"
    result = dict()
    i=0
    for m in re.finditer(regx, xferlogLine):
        if i<=len(names)-1:
            if names[i]=='current-time':
                result[names[i]] = xferlogDateToTimeStamp(m.group())
                i=i+1
                continue
            result[names[i]] = m.group()
            i=i+1
    return result

def readXferlog(path):
    if not exists(path):
        return []
    
    tLog = open(path, 'r')
    result = []
    for l in tLog:
        if len(l) > 0:
            result.append(xferlogMatchColumn(l))
    tLog.close()
    return result


#print(readXferlog('xferlog'))
