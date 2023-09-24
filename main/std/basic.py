import time
import sys
import os

def getSystemInfo(infoMode = False) -> str:
    res = ''
    if 'win32' in sys.platform and infoMode:
        res += os.popen('systeminfo').read()
    else:
        return (str(time.time()),sys.platform)
    
    return (str(time.time()),sys.platform,res)

def getUnixtime() -> int:
    return int(time.time())
