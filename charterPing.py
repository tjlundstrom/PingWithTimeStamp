#!/usr/bin/python
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

file = open(time.strftime("%d-%m-%Y"), 'ab')
i = 0
for num in range(0,300):
    location = ping("192.168.1.1", 1).find('time') + 5
    pingTime = ping("192.168.1.1", 1)[location:location+5]
    if(float(pingTime) > 0.000):
        file.write(str(ping("192.168.1.1", 1)) + " Ping: " + str(i) + " \n")
    time.sleep(1)
    i+=1

file.close()