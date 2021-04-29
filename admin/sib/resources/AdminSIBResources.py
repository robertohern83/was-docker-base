'''
Created on 03/06/2013

@author: rhernandezm
'''


########################################################
# Búsqueda de una fabrica de conexiones de colas para SIB
########################################################
def findSIBQueueConnectionFactory(context, resourceName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/J2CResourceAdapter:SIB JMS Resource Adapter/J2CConnectionFactory:'
    locator += resourceName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)

########################################################
# Búsqueda de un destino para SIB
########################################################
def findSIBQueue(context, resourceName):
    print 'locating: ' + resourceName + ' in ' + context
    propertyList = AdminTask.listSIBJMSQueues(AdminConfig.getid(context)).splitlines()
    for elem in propertyList:
        if (AdminConfig.showAttribute(elem,"name") == resourceName):
            return elem

########################################################
# Borrado de una fabrica de conexiones de colas para SIB
########################################################     
def removeSIBQueueConnectionFactory(context, resourceName):
    print removeResource(findSIBQueueConnectionFactory(context, resourceName))    
    
########################################################
# Borrado de una fabrica de conexiones de colas para SIB
########################################################     
def removeSIBQueue(context, resourceName):
    print removeResource(findSIBQueue(context, resourceName))
    
########################################################    
# Creación de una fabrica de conexiones de colas para SIB
########################################################
def createSIBQueueConnectionFactory(context, name, jndiName, busName, connectionPoolProperties):
    print 'createSIBQueueConnectionFactory ' + name
    contextId = AdminConfig.getid(context)
    createdResource = AdminTask.createSIBJMSConnectionFactory(contextId, ["-name "+ name +
                                                     " -jndiName "+ jndiName + 
                                                     " -busName " + busName + 
                                                     " -type queue "])
    AdminConfig.modify(createdResource, [["connectionPool", connectionPoolProperties]])    


########################################################    
# Creación de una fabrica de conexiones de colas para SIB
########################################################
def createSIBQueue(context, name, jndiName, busName, destinationQueue):
    print 'createSIBQueue ' + name
    contextId = AdminConfig.getid(context)
    AdminTask.createSIBJMSQueue(contextId, ["-name", name, "-jndiName",jndiName, "-busName", busName, "-queueName", destinationQueue])
   

########################################################
# Borrado genérico de un recurso
########################################################
def removeResource(id):  
    print AdminConfig.remove(id)
