#/env/python

import os

def run(**args):
    print "[*] In environment modlue."
    return str(os.environ)