#!/usr/bin/env python

import os
import sys
import win32serviceutil

#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\')
#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\Libs\immlib')

import immlib

def main(args):
    imm = immlib.Debugger()
    popserviceName = "Seattle Lab POP3 Server"
    #serviceName = "Seattle Lab Smtp Server"
    win32serviceutil.StartService(popserviceName)
    #win32serviceutil.StartService(serviceName)
    
    #imm.openProcess("C:\\Windows\\System32\\control.exe SLmail.cpl")
    #imm.openProcess("C:\\Program Files\\SLmail\\SLSmtp.exe")
    #imm.openProcess("C:\\Program Files\\SLmail\\SLmail.exe")
    

    #imm.Attach(int(args[0]))
    
    return "Success SLMAIL service is started! Ok now run !auto_table and look for the PID for SLMAIL"
