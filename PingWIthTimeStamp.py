import subprocess
import datetime
import time

def ping(host, numOfPings):
    for num in range(0,numOfPings):
        ping = subprocess.Popen(["ping", "-c", "1", host], stdout=subprocess.PIPE)
        ping = ping.communicate()
        pings = ping[0].splitlines()
        for ping in pings:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if(ping[:2]=="64"):
                return str(now) + " : " + str(ping)