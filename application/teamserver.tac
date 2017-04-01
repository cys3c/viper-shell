#!/usr/bin/python
# Copyright (c) 2017 Joseph Inverarity <jinverar@gmail.com>

# See the COPYRIGHT file for more information

import os
from twisted.application import service
from twisted.internet import pollreactor
pollreactor.install() #installs the poll reactor work with larger numbers of connected sockets, it may provide for better performance than the SelectReactor
from twisted.internet.protocol import Factory
from teamserverdev import CONSOLEFactory
from twisted.internet import protocol, reactor
from twisted.python import log
from twisted.internet.defer import Deferred as D
import traceback

#def stack():
#    print 'The python stack:'
#    traceback.print_stack()
#    err.printTraceback()
#    d = D()
#    d.addCallback(start_app)
#    d.addErrback(command_die)
#    d.callback(0)    




#teamserver = Server()
#teamserverdev.listen(myport)
application = service.Application(CONSOLEFactory)
CONSOLEService = pollreactor.TCPServer(port, ip)
CONSOLEService.setServiceParent(application)
pollreactor.callWhenRunning(application)
reactor.listenTCP(port,ip)
pollreactor.run(stack)
pollreactor.run()


#from twisted.internet import reactor
#pollreactor.CONSOLEFactory() 
#reactor.callWhenRunning(Countdown().count)
#

     
#log.startLogging(open('../data/echo.log', 'w'))    
#endpoint = TCP4ServerEndpoint(reactor, 8007)
#endpoint.listen(CONSOLEFactory())
#print 'Starting the teamserver reactor.' 
#pollreactor.run(stack)

