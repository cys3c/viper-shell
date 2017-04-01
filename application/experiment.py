#!/usr/bin/python
from twisted.application import service
from twisted.internet.protocol import Factory
from twisted.internet import protocol, reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import pollreactor
#pollreactor.install() #installs the poll reactor work with larger numbers of connected sockets, it may provide for better performance than the SelectReactor
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
    print "[*] chatserver ========= > will start your chat server on port 8123. You will have to open a new terminal to connect" 
    print "[*] stopchat ========= > will tear down the chat server when needed" 
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "\n"

class Viper(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols+1
        self.transport.write( "Welcome! There are currently %d open connections.\n" %(self.factory.numProtocols,))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols-1       
        
    
    def dataReceived(self, data):
        self.transport.write(data)


class CONSOLEFactory(Factory):
    def buildProtocol(self, addr):
        banner()
        while(True):
            command = raw_input('$ Viper]}>> ')
            if "help" in command:
                for x in command:
                    x = "help"
                    print("[+] here is the help ")
                    menu()
                    break    
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
                #subprocess.call("../payloads/Client2exe.sh", stdin=None, stdout=None, stderr=None, shell=True)
                subprocess.call("payloads/Client2exe.sh 2>/dev/null", shell=True)
                print ( "[+] created the exe inside the payloads folder. Reminder you still may have a payload in /var/www/html")
                pass
                #banner()           
                #menu()
            
            elif 'chatserver' in command:
                os.system("twistd -ny services/chatserver.py  --pidfile services/chatserver.pid &")
                print ( "[+] chatserver reactor started")
                print ( "[+] created the chatserver please connect to server as host @ telnet 127.0.0.1 8123 username host")
                print ( "[*] remember for now you will have to manually kill the chat server type (stopchat) for commands to stop chat ")
                pass 
               
            elif 'stopchat' in command:
                print ( "[+] for now you will have to manually stop chatserver with the usual methods")
                print ( "[+] type in terminal ps aux | grep chatserver and then kill -9 pid")
                pass     
            else:
                print('')


port = 8007
application = service.Application(CONSOLEFactory)
#CONSOLEService = pollreactor.listenTCP(port, factory)
#pollreactor.callWhenRunning(application)
#reactor.listenTCP(port,V)
endpoint = TCP4ServerEndpoint(reactor, port)
endpoint.listen(CONSOLEFactory())
reactor.run()

#pollreactor.run(stack)
#pollreactor.run()
#from twisted.internet import reactor
#reactor.callWhenRunning(stack)
#reactor.run()

     
#log.startLogging(open('data/echo.log', 'w'))    
#endpoint = TCP4ServerEndpoint(reactor, 8081)
#endpoint.listen(CONSOLEFactory())
#print 'Starting the teamserver reactor.' 
#pollreactor.run(stack)
#pollreactor.run(CONSOLEFactory())

