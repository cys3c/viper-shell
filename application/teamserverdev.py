#!/usr/bin/python

from twisted.internet.protocol import Factory
from twisted.internet import protocol, reactor
from twisted.python import log

import subprocess
import os
import sys
import readline
import services.viperserver as viperserver
import commands
import platform


sys.dont_write_bytecode = True

"""
1. This is python framework designed to control agents that get deployed on computers in defense of exploitation frameworks!
2. The framework is designed in order to detect compromised files, processes, and services in order to grab or kill the malware. 
3. This framework can also be used for testing exploitation and enumeration for the purpose of learning offensive for defensible actions. 


"""


def banner():
    print """

Name : Viper Framework by Black Signals
Date : 03 March 17
Version : v1.0

Twisted Viper Security for Active Defense

                    Going low and slow
"""

def menu():
    """This is the program menu"""
    print "[*] Command options: "
    print
    print "[*] handler ========= > starts the viper server and waits for a call back" 
    print "[*] client2exe ========= > builds a exe payload and stores it inside payloads"
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "\n"

class Viper(protocol.Protocol):
    def dataReceived(self, data):
        log.msg(data)
        self.transport.write(data)


class CONSOLEFactory(Factory):
    banner()
    while(True):
        command = raw_input('$ Viper]}>> ')
        #command = command.split(" ")

        if "help" in command:
            menu = menu()
            print(menu)
            
        elif 'ls' in command:
            dirlist = os.listdir(".")
            print(dirlist)

        elif 'cd' in command:
            for x in command:
                if 'cd*' in x:
                    code, command = command.split("*")
                    os.chdir(command)
                    print ("[+] CWD Is " + os.getcwd())
                elif 'cd' in command:
                    code, command = command.split(" ")
                    os.chdir(command)
                    print ("[+] CWD Is " + os.getcwd())
            
        elif 'dir' in command:
            dirlist = os.listdir(".")
            print(dirlist)
        
        elif 'handler' in command:
            print ( "[+] Starting server standby " + viperserver.main())
        
        elif 'client2exe' in command:
            #subprocess.call("payloads/Client2exe.sh", stdin=None, stdout=None, stderr=None, shell=True)
            subprocess.call("payloads/Client2exe.sh 2>/dev/null", shell=True)
            print ( "[+] created the exe inside the payloads folder. Reminder you still may have a payload in /var/www/html")
            pass
            #banner()           
            #menu()
            
        else:
            print('')

        
        
log.startLogging(open('data/echo.log', 'w'))    
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(CONSOLEFactory())
reactor.run()
    

