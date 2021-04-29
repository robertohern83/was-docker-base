# -*- encoding: utf-8 -*-
#Scripts de Instalación de paguelo
#mduarte-interfazsoftware
#versión 1.0
#Utilidades con strings

import sys
import string
import os

##Valida si un string es vacio o nulo
##@param value. String a chequear
##@result Resultado de la validación 
def isEmptyOrNull(value):
    result = True
    if value != None and len(value) > 0:
        result =False
    return result

##Valida si un string no es nulo
##@param value. String a chequear
##@result Resultado de la validación 
def isNotNull(value):
    
    try:
        
        if value == None:
            result =False
    except:
        print "Fallo la validación" , sys.exc_info()[0], sys.exc_info()[1] 
    return result       

##Valida si un string no es vacio
##@param value. String a chequear
##@result Resultado de la validación 
def isNotEmpty(value):
    result = False
    if len(value) > 0:
        result =True
    return result

variable = False

if(not variable):
    print("Hola")
