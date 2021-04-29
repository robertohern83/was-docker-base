#
# TODO: enter JYTHON code and save
#

def modifyVariable(context, varName, newVarValue):
    node = AdminConfig.getid(context)
    varSubstitutions = AdminConfig.list("VariableSubstitutionEntry",node).splitlines()
    for varSubst in varSubstitutions:
    	getVarName = AdminConfig.showAttribute(varSubst, "symbolicName")
    	if getVarName == varName:
    		AdminConfig.modify(varSubst,[["value", newVarValue]])
    		break    
    
    print 'modifiying: ' + varName + ' to ' + newVarValue