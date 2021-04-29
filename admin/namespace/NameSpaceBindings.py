
########################################################
# Creación variables de espacio de nombres 
########################################################  
def createNameSpaceBindings(pnode,name,nameSpace,stringToBind):
      node = AdminConfig.getid(pnode)
      print 'createNameSpaceBindings: ' + name
      AdminConfig.create('StringNameSpaceBinding', node,[['name', name],
                                  ['nameInNameSpace', nameSpace],
                                  ['stringToBind',stringToBind]])


def modifyNameSpaceBindings(pnode,name,nameSpace,stringToBind):
	
	node = AdminConfig.getid(pnode+"/StringNameSpaceBinding:" + name + "/")
      	print 'modifyNameSpaceBinding: ' + name
      	AdminConfig.modify(node,[['name', name],
                                  ['nameInNameSpace', nameSpace],
                                  ['stringToBind',stringToBind]])                       
                                  
                                  