from java.io import File
from java.io import FileInputStream 
from java.io import FileNotFoundException 
from java.util import Properties 
import os
import re
import Constants as const

#Este Script es para cargar las propiedades de Paguelo

propertiesFile = Properties()

#Este método me va a cargar el archivo de propiedades de páguelo
#Párametros: pathFileName: Dirección física del archivo de propiedades
#Retorna: las propiedades correspondientes al archivo
def loadPropertiesFile(pathFileName):
    try:	
	inStream = FileInputStream(pathFileName)
  	global propertiesFile
  	propertiesFile = Properties()
 	propertiesFile.load(inStream)
    except FileNotFoundException:	
           print const.READING_FILE_EROR
		  	
#Método que me retorna todas las propiedades que se encuentran en archivo de properties. 
#Retorna: retorna la lista de propiedades que se encuentran en el 
#Envia un mensaje si no tiene propiedades disponibles
def getAllProperties():
	global propertiesFile
	if(len(propertiesFile) == 0 ):
		print const.PROPERTIES_NOT_FOUND_ERROR
	elif  len(propertiesFile) > 0 :		  	
	        return propertiesFile	


########################################################
# Lecturas de lista de propiedades por datasource
########################################################    

#Metodo que me agrupa para JDBCProvider los Dictionaries deacuerdo al DataSource
#Retorna: una lista con todas las propiedades correspondientes a ese data source
def groupByJDBCProvider():
	global propertiesFile

	#Obtenemos los llaves correspondientes a nuestro archivo de propiedades
	keys = propertiesFile.keySet().iterator()

	#Instacia de dictionary para el datasource 
	jdbcProvider = {}
	
	for key in keys:
		if(str(key).find(const.JDBCProvider_KEY) != -1):
		   jdbcProvider[key] = propertiesFile.getProperty(key)
		  	  
        return jdbcProvider

#Metodo que me agrupa para JDBCDataSource los Dictionaries deacuerdo al DataSource
#Retorna: una lista con todas las propiedades correspondientes a ese data source
def groupByKey(searchKey):
	global propertiesFile
	#Obtenemos los llaves correspondientes a nuestro archivo de propiedades
	keys = propertiesFile.keySet().iterator()
	#Instacia de dictionary para el datasource 
	configs = {}
	for key in keys:
	   if(str(key).find(searchKey) != -1):
              configKey = key[0:str(key).find('.')]
	      if (configs.get(configKey) == None):
		  configs[configKey] = {}
	      valueKey = key[str(key).find('.') + 1:len(key)]	   	
	      configs[configKey][valueKey] = propertiesFile.getProperty(key)
	return configs
   