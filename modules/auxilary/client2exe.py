#!/usr/bin/python

import os
import sys
import subprocess

"""This is python script to convert agent.py to ViperClient.exe for x86!"""


# step 1 create exe inside payloads

os.system('cd ../../../payloads/')
os.system('wine pyinstaller --onefile --noconsole --nowindowed ViperClient.py')
os.system('rm -rf build')
os.system('rm -rf dist')
os.system("sed -i 's/console=True/console=False/g' ViperClient.spec")
os.system('wine pyinstaller ViperClient.spec')
os.system('cd dist')
os.system('cp dist/ViperClient.exe /root/')
os.system('rm -rf dist')
os.system('rm -rf build')
os.system('rm ViperClient.spec')


print "[*] File has been created and moved to /root/ViperClient.exe"













