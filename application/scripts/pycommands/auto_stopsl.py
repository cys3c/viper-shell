#!/usr/bin/env python

import os
import sys
import win32serviceutil

#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\')
#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\Libs\immlib')

import immlib

def main(args):
    imm = immlib.Debugger()
    #popserviceName = "Seattle Lab POP3 Server"
    serviceName = "Seattle Lab Smtp Server"
    #win32serviceutil.StopService(popserviceName)
    win32serviceutil.StopService(serviceName)

    
    return "success"


##Extra notes
#imm.assemble("JMP ESP")
#imm.assemble("JMP ESP\nRET")
#OUTPUT IN HEX
#Search
#imm.search("HEX")
#RETURNS LIST OF ADDRESS OF PROGRAM IN MEMORY

#imm.findModule("RETURNS LIST OF ADDRESS")
#RETURNS THE MODULE AND BASE ADDRESS OF MODULE

#TAKE INPUT FROM USER ON SET OF INSTRUCTIONS > AUTO SEARCH FIND
#ADDRESS in current programs address space find address and modules
#create table. 
