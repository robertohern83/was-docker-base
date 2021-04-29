########################################################
# Creación del cluster
########################################################
def createCluster( nameOfCluster, createReplicationDomain = 0 ):
 	cluster = None
  	# create the cluster
  	print "  . . . creating a " + nameOfCluster + " cluster"
  	if createReplicationDomain == 0:
    		cluster = AdminTask.createCluster('[-clusterConfig [-clusterName ' + nameOfCluster + ']]')
  	else:
    		cluster = AdminTask.createCluster('[-clusterConfig [-clusterName ' + nameOfCluster + '] -replicationDomain [-createDomain true] ]')
  	print cluster
  	#whatFilesChanged()
  	return

########################################################
# Creación de miembros del cluster
########################################################
def createFirstClusterMember( nameOfCluster, nodeName, serverName, joinReplicationDomain = 0, nodeGroupName = "DefaultNodeGroup", coreGroupName = "DefaultCoreGroup" ):
	replicate = 'false'

    	print "Adding first member " + nodeName + " / " + serverName + " to " + nameOfCluster
    	if joinReplicationDomain != 0:
    		 replicate = 'true'
    	print AdminTask.createClusterMember('[-clusterName ' + nameOfCluster +
        ' -memberConfig [-memberNode ' + nodeName + ' -memberName ' + serverName +
        ' -replicatorEntry ' + replicate   + '] ' +
        ' -firstMember[ -templateName default -nodeGroup ' + nodeGroupName +
        '  -coreGroup ' + coreGroupName + '   ] ' + ']')

def whatFilesChanged():
  	print "The following congfiguration files have changes pending:"
  	print AdminConfig.queryChanges()
  	return

def createAdditionalClusterMembers( nameOfCluster, listOfServerNames ):	
	listOfProposedNewMemberServers = list( listOfServerNames )
	print "  . . . adding " + str( len(listOfProposedNewMemberServers) ) + " additional members to the " + nameOfCluster + " cluster"
	
	# add the rest of the cluster members
	for server in listOfProposedNewMemberServers:
		nodeName = server[0]
		serverName = server[1]
		replicate = "false"
		if len( server ) == 2:
			print AdminTask.createClusterMember('[-clusterName ' + nameOfCluster + ' -memberConfig [-memberNode ' + nodeName + ' -memberName ' + serverName  + ']]')
		if len( server ) == 3:
			# convert the ReplicationDomain parameter of our parameter list
			# into the 'true' or 'false' notation that AdminTask requires
			if server[2] == 0:
				replicate = "false"
			else:
				replicate = "true"
			print AdminTask.createClusterMember('[-clusterName ' + nameOfCluster + ' -memberConfig [-memberNode ' + nodeName + ' -memberName ' + serverName + ' -replicatorEntry ' + replicate + ']]')
	return