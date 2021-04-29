# -*- encoding: utf-8 -*-
import java
import re
import admin.utilities.AdminUtilities as adminUtilities
'''
def findWebsphereAppServer(context, serverName):
	locator = ''
	if context != '' :
		locator += context
	locator += '/Server:'
	locator += serverName
	return AdminConfig.getid(locator)
'''

def createWorkManager(context,name,workReqQFullAction,minThreads,numAlarmThreads,jndiName,maxThreads,isGrowable,threadPriority):
	node = AdminConfig.getid(context)	
	provider = AdminConfig.list('WorkManagerProvider',node).splitlines()[-1]
	try:
		if not findWorkManager(context,name):
			AdminConfig.create('WorkManagerInfo', provider,[['name', name],
								['workReqQFullAction', workReqQFullAction],
								['minThreads',minThreads],
								['numAlarmThreads',numAlarmThreads],
								['jndiName',jndiName],
								['maxThreads',maxThreads],
								['isGrowable',isGrowable],
								['threadPriority',threadPriority]])
			print 'Work Manager: ' + name + ' creado'
		else:
			print 'Work Manager: ' + name + ' ya existe'			
	except e:
		print 'Error al crear el work manager. '
		

def findWorkManager(context,wmName):
	locator = ''
	listServer = ''
	exist = 0
	locator += '/WorkManagerInfo:'	
	locator += wmName
	listServer = re.findall(r"[-\w']+", AdminConfig.getid(locator))
	if context.split(":")[1] in listServer: exist = 1
	return exist

'''
def removeWorkManager(context,name):
'''
