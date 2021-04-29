#
# TODO: enter JYTHON code and save
#

def createObjectCache(context, objectName, JNDIName, cacheSize, memoryCacheSizeInMB):
    contextId = AdminConfig.getid(context + '/CacheProvider:CacheProvider')
    createdResource = AdminTask.createObjectCacheInstance(contextId, '[-name ' + objectName + ' -jndiName ' + JNDIName + ' ]' )
    AdminConfig.modify(createdResource, [['cacheSize', cacheSize], ['memoryCacheSizeInMB', memoryCacheSizeInMB]])
    
    print 'creating: ' + objectName + ' on ' + contextId