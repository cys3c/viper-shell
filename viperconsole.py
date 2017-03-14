#!/usr/local/bin/python

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

    Name : Viper TCPServer by Black Signals
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
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "[*] ??????? ========= > " 
    print "\n"



def console():
	while(True):
		command = raw_input('$ Viper>> ')
		command = command.split() 

		if command[0] == 'ls':
			dire = '.'

			if len(command) > 1:
				dire = command[1]
				print('\n'.join(os.listdir(dire)))
			elif command[0] == 'exit':
					exit()	

		
		elif 'handler' in command:
			print ( "[+] Starting server standby " + viperserver.main())
			
		else:
			print('error')
			print('error')

		
		

    
        
def main():
	banner()
	menu()
	console()
	
if __name__ == "__main__":
	main()
        
