# -*- encoding: utf-8 -*-
#Scripts de Instalación de paguelo
#aduartev
#versión 1.0
#Utilidades con strings

import sys
import traceback
import java
from   java.util.logging  import Logger, FileHandler, SimpleFormatter

logger = None
stdoutActive = 0

def initLogger(pStdoutActive):
	global logger
	global stdoutActive
	stdoutActive = pStdoutActive
	logger  = Logger.getLogger( 'ConfigureServersLog' )
	logFile = FileHandler( r'.\log.log' )
	logFile.setFormatter( SimpleFormatter() )
	logger.addHandler( logFile )


def logException(message):
	ex_type, ex, tb = sys.exc_info()
	global logger
	global stdoutActive
	logger  = Logger.getLogger( 'ConfigureServersLog' )
	desc1 = message
	
	if ex_type is not None: 
		variable = traceback.format_tb(tb)
		desc1 = desc1 + str(ex_type) + '(' + str(ex) + ')\n'
		for string in variable:
		 	desc1 = desc1 + string
		 
	logger.severe(desc1)
	if(stdoutActive):
		print desc1


def info(message):
	global stdoutActive
	global logger
	logger  = Logger.getLogger( 'ConfigureServersLog' )
	logger.info(message)
	if(stdoutActive):
		print message