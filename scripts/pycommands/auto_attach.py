#!/usr/bin/env python

import sys

#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\')
#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\Libs\immlib')

import immlib

def main(args):
    imm = immlib.Debugger()

    #imm.openProcess("C:\\Windows\\System32\\control.exe SLmail.cpl")

    imm.Attach(int(args[0]))
    
    return "[+] Success ok now you can run the buffer overflow, if you want to start from scratch just exit immunity and restart immunity. to search use !custom_search JMP ESP"
