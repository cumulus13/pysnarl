#! /usr/bin/python
# -*- coding: utf-8 -*-

import PySnarl
import time

#snGetVersion tells you if Snarl is alive
if PySnarl.snGetVersion() != False:
    #Get Version gives you the major and minor version numbers of the running snarl
    (major, minor) = PySnarl.snGetVersion()
    print "Found Snarl version",str(major)+"."+str(minor),"running."
    
    #Show a message,  otherwise snarl is useless
    id = PySnarl.snShowMessage("Test Message", "Hello World!")
    time.sleep(2)
    #wait and then update message for the fun of it
    PySnarl.snUpdateMessage(id, "Test 2", "Hello Snarl!")
    
    #If the message is still visible,  set a timeout for it to go away
    if PySnarl.snIsMessageVisible(id):
        PySnarl.snSetTimeout(id, 2)
        
    #timeout can be set inline and unicode can be sent.
    id = PySnarl.snShowMessage('Test Unicode', u'привет мир', timeout=5)
    
else:
    print "Sorry Snarl does not appear to be running"

