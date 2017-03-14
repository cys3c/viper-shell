#!/usr/local/bin/python

import os
import subprocess

while(True):
    # cntrl-c to quit
    input = raw_input('your_prompt$ ')

    process = subprocess.Popen(input, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    out, err = process.communicate()

    print(out)
    print(err)