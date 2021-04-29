import java
import re
import sys
import string
import os

def serverExist(serverList, serverName):
    result = None
    if(re.search(serverName, serverList)):
        #print serverName      
        result = 1
    else: 
        result = 0
    return result

def search(searchType, match):
	elements = AdminConfig.list(searchType)
    #print match
	#print elements
	return elements.find(match)

def find(searchType, match):
    result = 0
    elements = AdminConfig.list(searchType)
    if re.search(match, elements):
        result = 1
    return result

def findResource(context, resource):
    exist = 0
    context += resource
    if len(AdminConfig.getid(context)) > 0: exist = 1    
    return exist
