#!/usr/local/bin/python

import sys
import os

dire = '.'
if len(sys.argv) > 1:
    dire = sys.argv[1]
print('\n'.join(os.listdir(dire)))