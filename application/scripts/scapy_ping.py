#!/usr/bin/python

from scapy.all import *
import scapy

#pkt = IP(dst="10.11.1.5")/ICMP()/"Hack the planet"



for ip in range(1,50):
	ip = srp(Ether()/IP(dst="10.11.1.1-254")/ICMP()/"Hack the planet", iface="tap0", loop=1)
	response, no_response=_
	print response.summary()

	
#working	
#srp(Ether()/IP(dst="10.11.1.1-254")/ICMP()/"Hack the planet", iface="tap0", loop=1)
#sendp(Ether()/IP(dst="10.11.1.1-254")/ICMP()/"Hack the planet", iface="tap0", loop=1)