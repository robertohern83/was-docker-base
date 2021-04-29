import java
########################################################
# Búsqueda de una fabrica de conexiones de colas para MQ
########################################################    
def findWebsphereAppServer(context, serverName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/Server:'
    locator += serverName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)


def createListenerPort(context, serverName, listenerName, destinationQCF, destinationQueue, maxSessions, maxRetries, maxMessages, initialState):
    print 'createListenerPort: ' + listenerName
    serverId = findWebsphereAppServer(context, serverName)
    mls = AdminConfig.list('MessageListenerService', serverId)
    new = AdminConfig.create('ListenerPort',
                       mls,
                       [['name',listenerName],
                        ['destinationJNDIName',destinationQueue],
                        ['connectionFactoryJNDIName', destinationQCF],
                        ['maxSessions',maxSessions],
                        ['maxRetries',maxRetries],
                        ['maxMessages',maxMessages]])
    sm = AdminConfig.list('StateManageable',new)
    AdminConfig.modify(sm,[['initialState',initialState]])
    
def findListenerPort(context, listenerPortName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/ApplicationServer:/EJBContainer:/MessageListenerService:/ListenerPort:'
    locator += listenerPortName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)


def removeListenerPort(context, listenerPortName):
    print 'removeListenerPort: ' + listenerPortName
    print removeResource(findListenerPort(context, listenerPortName))

########################################################
# Borrado genérico de un recurso
########################################################
def removeResource(id):  
    print AdminConfig.remove(id)
    
def createServer(nodeName, name):
    #nodeContext = AdminConfig.getid(node)
    print 'creating server ' + name + ' on ' + nodeName
    print AdminTask.createApplicationServer(nodeName, ['-name', name, '-templateName', 'default'])
    #print AdminConfig.create('Server', nodeContext, ['name', name])
    
def changeServerPort(nodeName, server, portId, port, host):
    AdminTask.modifyServerPort (server, '[-nodeName ' + nodeName + ' -endPointName ' + portId + ' -host ' + host + ' -port ' + port +']')
    
def getEndPointValue(pNodeName, pServerName, pEndPointName):
	lineSeparator = java.lang.System.getProperty("line.separator")
	nodes=AdminConfig.list("Node").split(lineSeparator) 
	for node in nodes:
	  nodeName = AdminConfig.showAttribute(node, "name")
	  serverEntries  = AdminConfig.list("ServerEntry", node).split(lineSeparator)
	  if (nodeName == pNodeName):
		  for serverEntry in serverEntries:
		    serverName = AdminConfig.showAttribute(serverEntry, "serverName")
		    if (serverName == pServerName):
			    namedEndPoints = AdminConfig.list("NamedEndPoint", serverEntry).split(lineSeparator)
			    for namedEndPoint in namedEndPoints:
			    	endPointName  = AdminConfig.showAttribute(namedEndPoint, "endPointName")
			    	endPoint = AdminConfig.showAttribute(namedEndPoint, "endPoint")
			    	host = AdminConfig.showAttribute(endPoint, "host")
			    	port  = AdminConfig.showAttribute(endPoint, "port")
			        if (endPointName == pEndPointName):
			    	    print "EndPointFound: " + endPointName+ ": " + host + ":" + port
			    	    return port
        return ''    

def createSharedLibrary(pNodeName, pServerName, pLibraryName, pClasspath):
    print "Creating " + pLibraryName
    node = AdminConfig.getid("/Node:" + pNodeName + "/")
    print node
    library = AdminConfig.create('Library', node, [['name', pLibraryName], ['classPath', pClasspath]])
    print library
    server = AdminConfig.getid("/Server:" + pServerName + "/")
    print server
    serverToAssignClassLoader = AdminConfig.list('ApplicationServer', server)
    classloader = AdminConfig.create('Classloader', serverToAssignClassLoader, [['mode', 'PARENT_FIRST']])
    print classloader
    print AdminConfig.create('LibraryRef', classloader, [['libraryName', pLibraryName]])
    print "SharedLibraryCreated!"
