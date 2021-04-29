##################################################################
# Activa la propiedad rmicCompatible para la JVM de los servidores
##################################################################
import re

#---------------------------------------------------------------------
# Name: createPropertyInJVM
# Role: Crea una propiedad en la JVM de los servidores que cumplen la expresión regular.
# From: WebSphere Application Server Administration using Jython
#   By: Guido Delgado Hernandez
#---------------------------------------------------------------------
def createPropertyInJVM(regularExpression, propertyName, propertyValue, propertyDescription = 'NONE'):
    
    # obtiene los servers del nodo    
    servers = AdminConfig.list('Server').splitlines()
    count = 1
    totalServers = len (servers)
    modifiedServers = 0
       
    # procesa con los servers encontrados
    if totalServers == 0 :
        print 'No posee servidores en el Node Agent'
    elif totalServers >= 1 :
        print 'Se ha encontrado un total de %d servidores' % totalServers
        print '\nAgregando propiedad:'        
        print '\tNombre: %s' % propertyName
        print '\tValor: %s' % propertyValue
        print '\tDescripcion: %s' % propertyDescription
        
        # Recorre los servidores
        for server in servers:
            
            serverName = AdminConfig.showAttribute(server, 'name')
            print '\n\tServidor %s, %d de %d' % (serverName, count, totalServers)
            count = count + 1 
            writeProperty = 'true'
            
            # Si el servidor se encuentra en la expresion regular lo procesa                       
            if re.match(regularExpression, serverName):
                
                # Valida que la propiedad no se encuentre ya en la maquina virtual
                jvm  = AdminConfig.list( 'JavaVirtualMachine', server );
                jvmDict = showAsDict( jvm );
                for p in jvmDict[ 'systemProperties' ][ 1:-1 ].split( ' ' ) :
                    ##print 'property:', p
                    pDict = showAsDict( p );
                    
                    if pDict[ 'name' ] == propertyName :
                        print '\t\tLa propiedad ya existe, no es necesario agregarla'
                        writeProperty = 'false'
                        break
                
                # Si la propiedad no existe la agrega 
                if  writeProperty == 'true' :
                    createProperty( jvm, propertyName, propertyValue, propertyDescription);
                    print '\t\tPropiedad agregada'
                    modifiedServers = modifiedServers + 1                
            else:
                print '\t\tServidor %s no aplica para el cambio' % serverName                       
                
        print '\nFin de los servidores'
        print 'Modificados %d de %d servidores' % (modifiedServers, totalServers)


#---------------------------------------------------------------------
# Name: createPropertyInJVM
# Role: Remueve una propiedad en la JVM de los servidores que cumplen la expresión regular.
# From: WebSphere Application Server Administration using Jython
#   By: Guido Delgado Hernandez
#---------------------------------------------------------------------
def removePropertyInJVM(regularExpression, propertyName):
    
    # obtiene los servers del nodo    
    servers = AdminConfig.list('Server').splitlines()
    count = 1
    totalServers = len (servers)
    modifiedServers = 0
       
    # procesa con los servers encontrados
    if totalServers == 0 :
        print 'No posee servidores en el Node Agent'
    elif totalServers >= 1 :
        print 'Se ha encontrado un total de %d servidores' % totalServers
        print '\nRemoviendo propiedad:'        
        print '\tNombre: %s' % propertyName
        
        # Recorre los servidores
        for server in servers:
            
            serverName = AdminConfig.showAttribute(server, 'name')
            print '\n\tServidor %s, %d de %d' % (serverName, count, totalServers)
            count = count + 1 
            removeProperty = 'false'
            
            # Si el servidor se encuentra en la expresion regular lo procesa                       
            if re.match(regularExpression, serverName):
                
                # Valida que la propiedad no se encuentre ya en la maquina virtual
                jvm  = AdminConfig.list( 'JavaVirtualMachine', server );
                jvmDict = showAsDict( jvm );
                for p in jvmDict[ 'systemProperties' ][ 1:-1 ].split( ' ' ) :
                    ##print 'property:', p
                    pDict = showAsDict( p );
                    
                    if pDict[ 'name' ] == propertyName :
                        print '\t\tRemoviendo...'
                        removeProperty = 'true'
                        AdminConfig.remove( p );
                        modifiedServers = modifiedServers + 1
                        break
                
                # Si la propiedad no existe la agrega 
                if  removeProperty == 'false' :
                    print '\t\tLa propiedad no existe en el server, no es necesario remover'
                                    
            else:
                print '\t\tServidor %s no aplica para el cambio' % serverName                       
                
        print '\nFin de los servidores'
        print 'Modificados %d de %d servidores' % (modifiedServers, totalServers)



#---------------------------------------------------------------------
# Name: showAsDict
# Role: Convert result of AdminConfig.show( configID ) to a dictionary
# From: WebSphere Application Server Administration using Jython
#   By: Robert A. (Bob) Gibson [rag], Arthur Kevin McGrath, Noel J. Bergman
# ISBN: 0-137-00952-6
#---------------------------------------------------------------------
def showAsDict( configId ) :
  'showAsDict( configId ) - Return a dictionary of the AdminConfig.show( configID ) result.'
  result = {};
  try :
    #-----------------------------------------------------------------
    # The result of the AdminConfig.show() should be a string
    # containing many lines.  Each line of which starts and ends
    # with brackets.  The "name" portion should be separated from the
    # associated value by a space.
    #-----------------------------------------------------------------
    for item in AdminConfig.show( configId ).splitlines() :
      if ( item[ 0 ] == '[' ) and ( item[ -1 ] == ']' ) :
        ( key, value ) = item[ 1:-1 ].split( ' ', 1 );
        if ( value[ 0 ] == '"' ) and ( value[ -1 ] == '"' ) :
          value = value[ 1:-1 ];
        result[ key ] = value;
  except NameError, e :
    print 'Name not found: ' + str( e );
  except :
    kind, value = sys.exc_info()[ :2 ];
    print 'Exception  type: ' + str( kind );
    print 'Exception value: ' + str( value );
  return result;


#---------------------------------------------------------------------
# Name: createProperty
# Role: Create a Property object using the user specified parameters
# Note: List comprehension allows us to easily create the parameters
#       required by the AdminConfig.create() method.
#---------------------------------------------------------------------
def createProperty( parent, name, value, desc = None ) :
  return AdminConfig.create( 'Property', parent, [ item for item in [ 'name', name ], [ 'value', value ], [ 'description', desc ] if item[ 1 ] ] );


#---------------------------------------------------------------------
# Name: Usage()
# Role: Display script usage information
#---------------------------------------------------------------------
def Usage( cmdName = None ) :
  if not cmdName :
    cmdName = 'setJVMproperties';
  print __doc__ % locals();
