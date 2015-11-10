'''
Created on Jan 17, 2014

@author: ezulkosk
'''
from z3 import *

FeatureIndexMap = {}
FeatureVariable = []
FeatureIndexMap['searchandrescuefm'] = 0
searchandrescuefm = Bool('searchandrescuefm')
FeatureVariable.append(searchandrescuefm) 
FeatureIndexMap['locationfinding'] = 1
locationfinding = Bool('locationfinding')
FeatureVariable.append(locationfinding) 
FeatureIndexMap['gps'] = 2
gps = Bool('gps')
FeatureVariable.append(gps) 
FeatureIndexMap['radiotriangulation'] = 3
radiotriangulation = Bool('radiotriangulation')
FeatureVariable.append(radiotriangulation) 
FeatureIndexMap['hardwareplatform'] = 4
hardwareplatform = Bool('hardwareplatform')
FeatureVariable.append(hardwareplatform) 
FeatureIndexMap['nexusonehtc'] = 5
nexusonehtc = Bool('nexusonehtc')
FeatureVariable.append(nexusonehtc) 
FeatureIndexMap['droidmotoroal'] = 6
droidmotoroal = Bool('droidmotoroal')
FeatureVariable.append(droidmotoroal) 
FeatureIndexMap['filesharing'] = 7
filesharing = Bool('filesharing')
FeatureVariable.append(filesharing) 
FeatureIndexMap['filemanageropentintents'] = 8
filemanageropentintents = Bool('filemanageropentintents')
FeatureVariable.append(filemanageropentintents) 
FeatureIndexMap['inhousefilemanager'] = 9
inhousefilemanager = Bool('inhousefilemanager')
FeatureVariable.append(inhousefilemanager) 
FeatureIndexMap['reportsynchronization'] = 10
reportsynchronization = Bool('reportsynchronization')
FeatureVariable.append(reportsynchronization) 
FeatureIndexMap['explicitreportssync'] = 11
explicitreportssync = Bool('explicitreportssync')
FeatureVariable.append(explicitreportssync) 
FeatureIndexMap['implicitreportssync'] = 12
implicitreportssync = Bool('implicitreportssync')
FeatureVariable.append(implicitreportssync) 
FeatureIndexMap['chatprotocol'] = 13
chatprotocol = Bool('chatprotocol')
FeatureVariable.append(chatprotocol) 
FeatureIndexMap['openfire'] = 14
openfire = Bool('openfire')
FeatureVariable.append(openfire) 
FeatureIndexMap['inhousechatprotocol'] = 15
inhousechatprotocol = Bool('inhousechatprotocol')
FeatureVariable.append(inhousechatprotocol) 
FeatureIndexMap['mapaccess'] = 16
mapaccess = Bool('mapaccess')
FeatureVariable.append(mapaccess) 
FeatureIndexMap['ondemandgooglesite'] = 17
ondemandgooglesite = Bool('ondemandgooglesite')
FeatureVariable.append(ondemandgooglesite) 
FeatureIndexMap['cachedgoogleserver'] = 18
cachedgoogleserver = Bool('cachedgoogleserver')
FeatureVariable.append(cachedgoogleserver) 
FeatureIndexMap['preloadedesri'] = 19
preloadedesri = Bool('preloadedesri')
FeatureVariable.append(preloadedesri) 
FeatureIndexMap['connectivity'] = 20
connectivity = Bool('connectivity')
FeatureVariable.append(connectivity) 
FeatureIndexMap['wifi'] = 21
wifi = Bool('wifi')
FeatureVariable.append(wifi) 
FeatureIndexMap['threegnexusone'] = 22
threegnexusone = Bool('threegnexusone')
FeatureVariable.append(threegnexusone) 
FeatureIndexMap['threedroid'] = 23
threedroid = Bool('threedroid')
FeatureVariable.append(threedroid) 
FeatureIndexMap['bluetooth'] = 24
bluetooth = Bool('bluetooth')
FeatureVariable.append(bluetooth) 
FeatureIndexMap['database'] = 25
database = Bool('database')
FeatureVariable.append(database) 
FeatureIndexMap['mysql'] = 26
mysql = Bool('mysql')
FeatureVariable.append(mysql) 
FeatureIndexMap['sqlite'] = 27
sqlite = Bool('sqlite')
FeatureVariable.append(sqlite) 
FeatureIndexMap['architecturalstyle'] = 28
architecturalstyle = Bool('architecturalstyle')
FeatureVariable.append(architecturalstyle) 
FeatureIndexMap['peertopeer'] = 29
peertopeer = Bool('peertopeer')
FeatureVariable.append(peertopeer) 
FeatureIndexMap['clientserver'] = 30
clientserver = Bool('clientserver')
FeatureVariable.append(clientserver) 
FeatureIndexMap['pushbased'] = 31
pushbased = Bool('pushbased')
FeatureVariable.append(pushbased) 
FeatureIndexMap['dataexchangeformat'] = 32
dataexchangeformat = Bool('dataexchangeformat')
FeatureVariable.append(dataexchangeformat) 
FeatureIndexMap['xml'] = 33
xml = Bool('xml')
FeatureVariable.append(xml) 
FeatureIndexMap['compressedxml'] = 34
compressedxml = Bool('compressedxml')
FeatureVariable.append(compressedxml) 
FeatureIndexMap['unformatteddata'] = 35
unformatteddata = Bool('unformatteddata')
FeatureVariable.append(unformatteddata) 
#s = Solver()
s = Goal()

#Parent-Children
s.add(Implies(locationfinding, searchandrescuefm))
s.add(Implies(hardwareplatform, searchandrescuefm))
s.add(Implies(filesharing, searchandrescuefm))
s.add(Implies(reportsynchronization, searchandrescuefm))
s.add(Implies(chatprotocol, searchandrescuefm))
s.add(Implies(mapaccess, searchandrescuefm))
s.add(Implies(connectivity, searchandrescuefm))
s.add(Implies(database, searchandrescuefm))
s.add(Implies(architecturalstyle, searchandrescuefm))
s.add(Implies(dataexchangeformat, searchandrescuefm))
s.add(Implies(gps, locationfinding))
s.add(Implies(radiotriangulation, locationfinding))
s.add(Implies(nexusonehtc, hardwareplatform))
s.add(Implies(droidmotoroal, hardwareplatform))
s.add(Implies(filemanageropentintents, filesharing))
s.add(Implies(inhousefilemanager, filesharing))
s.add(Implies(explicitreportssync, reportsynchronization))
s.add(Implies(implicitreportssync, reportsynchronization))
s.add(Implies(openfire, chatprotocol))
s.add(Implies(inhousechatprotocol, chatprotocol))
s.add(Implies(ondemandgooglesite, mapaccess))
s.add(Implies(cachedgoogleserver, mapaccess))
s.add(Implies(preloadedesri, mapaccess))
s.add(Implies(wifi, connectivity))
s.add(Implies(threegnexusone, connectivity))
s.add(Implies(threedroid, connectivity))
s.add(Implies(bluetooth, connectivity))
s.add(Implies(mysql, database))
s.add(Implies(sqlite, database))
s.add(Implies(peertopeer, architecturalstyle))
s.add(Implies(clientserver, architecturalstyle))
s.add(Implies(pushbased, architecturalstyle))
s.add(Implies(xml, dataexchangeformat))
s.add(Implies(compressedxml, dataexchangeformat))
s.add(Implies(unformatteddata, dataexchangeformat))


#Mandatory-Children
s.add(locationfinding == searchandrescuefm)
s.add(hardwareplatform == searchandrescuefm)
s.add(filesharing == searchandrescuefm)
s.add(reportsynchronization == searchandrescuefm)
s.add(chatprotocol == searchandrescuefm)
s.add(mapaccess == searchandrescuefm)
s.add(connectivity == searchandrescuefm)
s.add(database == searchandrescuefm)
s.add(architecturalstyle == searchandrescuefm)
s.add(dataexchangeformat == searchandrescuefm)


#Exclusive-Or Constraints
s.add(gps==And(Not(radiotriangulation),locationfinding))
s.add(radiotriangulation==And(Not(gps),locationfinding))
s.add(nexusonehtc==And(Not(droidmotoroal),hardwareplatform))
s.add(droidmotoroal==And(Not(nexusonehtc),hardwareplatform))
s.add(filemanageropentintents==And(Not(inhousefilemanager),filesharing))
s.add(inhousefilemanager==And(Not(filemanageropentintents),filesharing))
s.add(explicitreportssync==And(Not(implicitreportssync),reportsynchronization))
s.add(implicitreportssync==And(Not(explicitreportssync),reportsynchronization))
s.add(openfire==And(Not(inhousechatprotocol),chatprotocol))
s.add(inhousechatprotocol==And(Not(openfire),chatprotocol))
s.add(ondemandgooglesite==And(Not(cachedgoogleserver),Not(preloadedesri),mapaccess))
s.add(cachedgoogleserver==And(Not(ondemandgooglesite),Not(preloadedesri),mapaccess))
s.add(preloadedesri==And(Not(ondemandgooglesite),Not(cachedgoogleserver),mapaccess))
s.add(wifi==And(Not(threegnexusone),Not(threedroid),Not(bluetooth),connectivity))
s.add(threegnexusone==And(Not(wifi),Not(threedroid),Not(bluetooth),connectivity))
s.add(threedroid==And(Not(wifi),Not(threegnexusone),Not(bluetooth),connectivity))
s.add(bluetooth==And(Not(wifi),Not(threegnexusone),Not(threedroid),connectivity))
s.add(mysql==And(Not(sqlite),database))
s.add(sqlite==And(Not(mysql),database))
s.add(peertopeer==And(Not(clientserver),Not(pushbased),architecturalstyle))
s.add(clientserver==And(Not(peertopeer),Not(pushbased),architecturalstyle))
s.add(pushbased==And(Not(peertopeer),Not(clientserver),architecturalstyle))
s.add(xml==And(Not(compressedxml),Not(unformatteddata),dataexchangeformat))
s.add(compressedxml==And(Not(xml),Not(unformatteddata),dataexchangeformat))
s.add(unformatteddata==And(Not(xml),Not(compressedxml),dataexchangeformat))


#Or Constraints


#Requires Constraints
s.add(Implies(threegnexusone, nexusonehtc))
s.add(Implies(threedroid, droidmotoroal))   


s.add(searchandrescuefm==True)
