#
# TODO: enter JYTHON code and save
#

def installApplication(nodeName, serverName, path, appname, virtualHost):
    AdminApp.install(path, ['-server', serverName, '-node', nodeName, '-appname', appname, '-MapWebModToVH', [['.*', '.*', virtualHost]]])
    print path + ' deployed on ' + serverName

def updateApplication(path, appname, appUri, virtualhost):
    AdminApp.update(appname, 'app', ['-operation', 'update', '-contents', path])
    if (virtualhost != None):
    	AdminApp.edit(appname, ['-MapWebModToVH', [['.*', '.*', virtualhost]]])
    print path + ' updated'

def installApplicationOnCluster(nodeName, clusterName, path, appname):
    AdminApp.install(path, ['-cluster', clusterName, '-node', nodeName, '-appname', appname])
    print path + ' deployed on ' + clusterName


