########################################################
# Búsqueda de una fabrica de conexiones de colas para MQ
########################################################    
def findMQQueueConnectionFactory(context, resourceName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/JMSProvider:WebSphere MQ JMS Provider/MQQueueConnectionFactory:'
    locator += resourceName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)

########################################################
# Búsqueda de una cola para MQ
########################################################    
def findMQQueue(context, resourceName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/JMSProvider:WebSphere MQ JMS Provider/MQQueue:'
    locator += resourceName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)

########################################################
# Borrado de una fabrica de conexiones de colas para MQ 
########################################################    
def removeMQQueueConnectionFactory(context, resourceName):
    print 'removeMQQueue: ' + resourceName
    print removeResource(findMQQueueConnectionFactory(context, resourceName))
    
########################################################
# Borrado de colas para MQ 
########################################################    
def removeMQQueue(context, resourceName):
    print 'removeMQQueue: ' + resourceName
    print removeResource(findMQQueue(context, resourceName))

########################################################
# Creación de una fabrica de conexiones de colas para MQ tipo Bindings
########################################################     
def createBindingsMQQueueConnectionFactory(context, name, jndiName, queueMgrName, connectionPoolProperties, sessionPoolProperties):
    print 'createBindingsMQQueueConnectionFactory: ' + name
    contextId = AdminConfig.getid(context)
    createdResource = AdminTask.createWMQConnectionFactory(contextId, ["-name "+ name +
                                                     " -jndiName "+ jndiName +
                                                     " -type QCF " + 
                                                     " -qmgrName " + queueMgrName + 
                                                     " -wmqTransportType BINDINGS"])
    AdminConfig.modify(createdResource, [["connectionPool", connectionPoolProperties], 
                                         ["sessionPool", sessionPoolProperties]])
    
    
########################################################
# Creación de una fabrica de conexiones de colas para MQ tipo Client
########################################################     
def createClientMQQueueConnectionFactory(context, name, jndiName, queueMgrName, connectionPoolProperties, sessionPoolProperties, host, port, channel):
    print 'createClientMQQueueConnectionFactory: ' + name
    contextId = AdminConfig.getid(context)
    createdResource = AdminTask.createWMQConnectionFactory(contextId, ["-name "+ name +
                                                     " -jndiName "+ jndiName +
                                                     " -type QCF " + 
                                                     " -qmgrName " + queueMgrName + 
                                                     " -wmqTransportType CLIENT" + 
                                                     " -qmgrHostname " + host + 
                                                     " -qmgrPortNumber " + port + 
                                                     " -qmgrSvrconnChannel " + channel])
                                                     
    AdminConfig.modify(createdResource, [["connectionPool", connectionPoolProperties], 
                                        ["sessionPool", sessionPoolProperties]])

########################################################
# Creación de una cola de MQ
########################################################   
def createMQQueue(context, name, jndiName, queueName, useRFH2):
    print 'createMQQueue: ' + name
    contextId = AdminConfig.getid(context)
    AdminTask.createWMQQueue(contextId, 
                             ["-name " + name + 
                              " -jndiName " + jndiName + 
                              " -queueName " + queueName + 
                              " -useRFH2 " + useRFH2])

########################################################
# Borrado genérico de un recurso
########################################################
def removeResource(id):  
    print AdminConfig.remove(id)
    
    