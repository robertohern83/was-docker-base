'''
Created on 04/06/2013

@author: rhernandezm
'''

########################################################
# Búsqueda de una fabrica de conexiones de colas para SIB
########################################################
def findJDBCDatasource(context, providerName, resourceName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/JDBCProvider:' + providerName + '/DataSource:'
    locator += resourceName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)

def findJDBCProvider(context, resourceName):
    locator = ''
    if context != '' :
        locator += context
    locator += '/JDBCProvider:'
    locator += resourceName
    print 'locating: ' + locator
    print AdminConfig.getid(locator)
    return AdminConfig.getid(locator)

def removeJDBCProvider(context, resourceName):
    print removeResource(findJDBCProvider(context, resourceName))

########################################################
# Borrado genérico de un recurso
########################################################
def removeResource(id):  
    print AdminConfig.remove(id)
    

def createDB2JDBCProvider(context, template, name):
    print 'createDB2JDBCProvider: ' + name
    contextId = AdminConfig.getid(context)
    tpl = AdminConfig.listTemplates('JDBCProvider', template)
    AdminConfig.createUsingTemplate('JDBCProvider', contextId, [['name', name]], tpl)


def createJ2CAuthAlias(cellname,alias,description,user,password):
    sec = AdminConfig.getid('/Cell:'+ cellname +'/Security:/')
    alias_attr = ["alias", alias]
    desc_attr = ["description", description]
    userid_attr = ["userId", user]
    password_attr = ["password", password]
    attrs = [alias_attr, desc_attr, userid_attr, password_attr]
    authdata = AdminConfig.create('JAASAuthData', sec, attrs)
    print "J2C Auth Alias created ---> " + alias
    AdminConfig.save()
    return    


def createDB2Datasource(context, providerName, name, jndiName, authAlias, library, connectionPoolProperties, template, user, password, server):
    print 'createDB2Datasource: ' + name
    contextId = AdminConfig.getid(context + '/JDBCProvider:' + providerName)
    tpl = AdminConfig.listTemplates('DataSource', template)
    dbattributes = None
    if authAlias is not None:
        dbattributes = [['name', name],
                       ['jndiName', jndiName],
                       ['authDataAlias', authAlias], 
                       ['authMechanismPreference', 'BASIC_PASSWORD']]
    else:
        dbattributes = [['name', name],
                       ['jndiName', jndiName], 
                       ['authMechanismPreference', 'BASIC_PASSWORD']]
    
    createdResource = AdminConfig.createUsingTemplate('DataSource', 
                                                      contextId, 
                                                      dbattributes, 
                                                      tpl)
    AdminConfig.modify(createdResource, [["connectionPool", connectionPoolProperties]])
    propertySet = AdminConfig.showAttribute(createdResource,"propertySet")
    propertyList = AdminConfig.list("J2EEResourceProperty", propertySet).splitlines()
    for elem in propertyList:
        if (AdminConfig.showAttribute(elem,"name") == "libraries"):
            AdminConfig.modify(elem,[['value', library]])
        if (AdminConfig.showAttribute(elem,"name") == "serverName"):
            AdminConfig.modify(elem,[['value', server]])
    if user is not None:
        userAttr = [['name', 'user'], ['value', user]]
        AdminConfig.create("J2EEResourceProperty", propertySet, userAttr)
        passAttr = [['name', 'password'], ['value', password]]
        AdminConfig.create("J2EEResourceProperty", propertySet, passAttr)
            
