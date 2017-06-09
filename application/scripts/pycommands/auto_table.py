#!/usr/bin/env python

import sys
import immlib
import immutils
from immutils import *

DESC = "A simple but complicated way to create a table with PID"

def main(args):
    imm = immlib.Debugger()
    #imm.openProcess("C:\\Windows\\System32\\control.exe SLmail.cpl")

    imm.log("Writing to my Log Window")
    imm.updateLog()

    td = imm.createTable("Module Information", ['PID', 'Name', 'Path', 'Services'])
    psList = imm.ps()

    for process in psList:
        td.add(0, [ str(process[0]), process[1], process[2], str(process[3])])

    return "[+] Success TABLE is not generated now attach to pid with command !auto_attach <pid> "
