#!/usr/bin/env python
import Globals
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

service_name = "What service would you like to check for?"
print (service_name)
service = raw_input()
print ('Zenoss has found "' + service + '" on the following servers:')

dmd = ZenScriptBase(connect=True).dmd

for s in dmd.Services.WinService.serviceclasses():
        if s.id == (service):
                for i in s.instances():
                        if i.getStatus() == 0:
                                status = "monitored"
                                print i.getDeviceName() + ", " + (status)
                        else:
                                status = "unmonitored"
                                print i.getDeviceName() + ", " + (status)
