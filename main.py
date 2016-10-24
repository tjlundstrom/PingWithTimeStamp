#!/usr/bin/python
import PingWIthTimeStamp

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