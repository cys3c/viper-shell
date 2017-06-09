#!/usr/bin/env python

import os
import sys


#add to PYTHON PATH > MY COMPUTER PROPERTIES > ENVIRONMENT VARIABLES
#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\')
#sys.path.append('C:\Program Files\Immunity Inc\Immunity Debugger\Libs\immlib')

#add multiple instrctions look in pycomands then click on custom_search.py and add more instructions

#usage in imunity debugget "!custom_seach JMP ESP"
#usage "!custom_search POP EAX"

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

import immlib

def main(args):
    imm = immlib.Debugger()

    assembledInstruction = imm.assemble(' '.join(args))

    if not assembledInstruction:
        return "[-] No Instruction Given!"
    #use the search command to find the addresses
    addressList = imm.search(assembledInstruction)
    #Create table with four columns
    td = imm.createTable("Instruction Locations", ['Module', 'Base Address', 'Instruction Address', 'Instruction'])
    #loop over list of addresses found in search command then call find module to find the 
    for address in addressList:
        #Get the module for this address and loop through addresses to find the modules
        module = imm.findModule(address)

        if not module:
            imm.log("Address: 0x%08X no in any module" %address)
            continue

        #get module object by name.
        #next we find the number of instruction sets. 

        instruction = ''
        #split to find multiple arguments
        numArgs = len(' '.join(args).split('\n'))
                      
        for count in range(0, numArgs):
                      instruction += imm.disasmForward(address, nlines=count).getDisasm() + ' '

        td.add(0, [module[0],
                   str('0x%08X'%module[1]),
                   str('0x%08X'%address),
                   instruction
                   ])


    return "Success"
