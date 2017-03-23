#!/usr/bin/python
# Copyright (c) 2017 Joseph Inverarity <jinverar@gmail.com>

# See the COPYRIGHT file for more information

import os
from twisted.application import service, internet
from teamserverdev import CONSOLEFactory


port = 8007
factory = CONSOLEFactory()

application = service.Application("teamserver")
CONSOLEService = internet.TCPServer(port, factory)

CONSOLEService.setServiceParent(application)

