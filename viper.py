#!/usr/bin/python

import subprocess
import os
import sys
import readline
import modules.handler.ViperServer as viperserver



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

#   __   _____ ___ ___ ___    ___ ___    _   __  __ _____      _____  ___ _  __    _ _   
#   \ \ / /_ _| _ \ __| _ \  | __| _ \  /_\ |  \/  | __\ \    / / _ \| _ \ |/ /  _| | |_  #
#    \ V / | ||  _/ _||   /  | _||   / / _ \| |\/| | _| \ \/\/ / (_) |   / ' <  |_  .  _| #
#     \_/ |___|_| |___|_|_\  |_| |_|_\/_/ \_\_|  |_|___| \_/\_/ \___/|_|_\_|\_\ |_     _| #
#                                                                                 |_|_|   #
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



def console():
	while(True):
		command = raw_input('$ Viper>> ')
		command = command.split(" ") 

		if 'ls' in command:
			dirlist = os.listdir(".")
			print(dirlist)
		
		if 'dir' in command:
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

		
		

    
        
def main():
	banner()
	menu()
	console()
	
if __name__ == "__main__":
	main()
        
