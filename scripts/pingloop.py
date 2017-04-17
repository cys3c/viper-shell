#!/usr/bin/python

import os
from datetime import datetime
import platform

net = raw_input("Enter the Network Address ")
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
str1 = int(raw_input("Enter the Starting Number "))
en1 = int(raw_input("Enter the Last Number "))
en1=en1+1
oper = platform.system()


if (oper=="Windows"):
   ping1 = "ping -n 1 "
elif (oper=="Linux"):
    ping1 = "ping -c 1 "
else:
    ping1 = "ping -c 1 "

t1= datetime.now()

print "Scanning in progress"

for ip in xrange(str1,en1):

    addr = net2+str(ip)

    comm = ping1+addr
    response = os.popen(comm)

    for line in response.readlines():
        if (line.count("ttl")):
            print addr, "--> Live"


t2= datetime.now()
total =t2-t1
print "Scanning complete in " , total



