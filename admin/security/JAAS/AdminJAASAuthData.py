'''
Created on 04/06/2013

@author: rhernandezm
'''
import java

########################################################
# Búsqueda de una fabrica de conexiones de colas para SIB
########################################################
def findJAASAuthenticationAlias(authAlias):
    lineSeparator = java.lang.System.getProperty('line.separator')
    jaasAuthDataList = AdminConfig.list("JAASAuthData") 
    jaasAuthDataList=jaasAuthDataList.split(lineSeparator)
    for jaasAuthId in jaasAuthDataList:
        getAlias = AdminConfig.showAttribute(jaasAuthId, "alias")
        if (getAlias == authAlias):
            print 'JAAS alias found: ' + jaasAuthId
            return jaasAuthId


def createJAASAuthenticationAlias(aliasName, description, userId, password):
    cell = AdminControl.getCell()
    contextId = AdminConfig.getid('/Cell:'+ cell + '/Security:/')
    print contextId
    print AdminConfig.create('JAASAuthData', contextId, [['alias', aliasName], 
                                                   ['description', description], 
                                                   ['userId', userId], 
                                                   ['password', password]])
    


def removeJAASAuthenticationAlias(authAlias):
    removeResource(findJAASAuthenticationAlias(authAlias))


########################################################
# Borrado genérico de un recurso
########################################################
def removeResource(id):  
    print AdminConfig.remove(id)