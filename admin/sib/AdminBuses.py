'''
Created on 04/06/2013

@author: rhernandezm
'''


def createBus (busName):
    print 'createBus ' + busName
    AdminTask.createSIBus(['-bus', busName, '-busSecurity', 'false'])
    
    
def addServerAsBusMember(busName, nodeName, serverName):
    print 'addServerAsBusMember ' + busName + ', ' + serverName
    AdminTask.addSIBusMember(['-bus', busName, 
                              '-node', nodeName,
                              '-server', serverName])
    
def removeBus (busName):
    print 'removeBus ' + busName
    AdminTask.deleteSIBus(['-bus', busName ])
    
def createBusDestinationForServer(busName, destinationName, serverName, nodeName):
    print 'createBusDestination ' + busName + ', ' + destinationName + ', ' + serverName
    AdminTask.createSIBDestination(['-bus', busName, '-node', nodeName, '-name', destinationName, '-type', 'QUEUE', '-server', serverName])