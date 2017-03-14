#!/bin/env python




class exit_cmd(cmd.Cmd,object):
    def can_exit(self):
        return True
    def onecmd(self, line):
        r = super (exit_cmd, self).onecmd(line)
        if r and (self.can_exit() or
           raw_input('exit anyway ? (yes/no):')=='yes'):
             return True
        return False
    def do_exit(self, s):
        return True
    def help_exit(self):
        print "Exit the interpreter."
        print "You can also use the Ctrl-D shortcut."
    do_EOF = do_exit
    help_EOF= help_exit