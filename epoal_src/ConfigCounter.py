'''
Created on Jan 17, 2014

@author: ezulkosk
'''
from random import choice
from MapDimacsBackToBestVars import getDimacsMap
from string import split
from subprocess import Popen, PIPE
from tokenize import generate_tokens
from z3 import Tactic, IntNumRef, BoolRef, is_not, BoolSortRef, Not, simplify
import Z3ModelERSNoObjectives as ERS
import Z3ModelEShopNoObjectives as SHP
import Z3ModelWPTNoObjectives as WPT
import itertools
import os
import random
import subprocess
import sys
import z3
import time

MAXDEPTH=1
tempfile="temp"
dimacs_map = {}
    
def genTempFile(sign,i,experiment, TCL, VARS, selectedVars):
    global tempfile
    try:
        os.remove(tempfile)
    except:
        pass
    currtemp= open(tempfile, 'a+')
    if i != 0:
        clauses = str(TCL+len(selectedVars)+1)
    else:
        clauses = str(TCL+len(selectedVars))
    currtemp.write("p cnf " + str(VARS) + " " + clauses +"\n")
    for j in selectedVars:
        currtemp.write(str(j) + " 0\n")
    if i != 0:
        currtemp.write(sign+""+str(i) + " 0\n")
    Popen(["tail -n +2 " + str(experiment) +".dimacs"], stdout=currtemp, shell=True)
    currtemp.close()

def getTopPairs(pairs):
    mymax = 9999999999999999999999999999999999999999999999999999999999999
    top = []
    for i in pairs:
        (myvar,val) = i
        if val < mymax:
            mymax = val
            top = [myvar]
        elif val == mymax:
            top.append(myvar)
    return top

def getPairs(TCL, VARS, selectedVars):
    pairs = []
    #print(TCL + len(selectedVars)+ 1)
    for i in range(1,VARS+1):
        try:
            genTempFile("", i,experiment, TCL, VARS,selectedVars)
            outputpos = Popen(["./sharpSAT -q " + tempfile], stderr=open("/dev/null", "w"),stdout=PIPE,shell=True)
            valpos=int(outputpos.stdout.read())
            genTempFile("-", i,experiment, TCL, VARS,selectedVars)
            outputneg = Popen(["./sharpSAT -q "+tempfile], stderr=open("/dev/null", "w"),stdout=PIPE,shell=True)
            valneg=int(outputneg.stdout.read())
            pairs.append((i, abs(valpos - valneg)))
        except:
            #print(i)
            continue
        
    if len(pairs) == 0:
        return False
    pairs.sort(key=lambda x: x[1])
    return pairs

def getBestFeatures(workingdir, experiment, TCL, VARS, selectedVars, totalConfigs):
    #print(selectedVars)
    if len(selectedVars) == MAXDEPTH:
        length = len(selectedVars)
        bestConfigsFile = open(workingdir + "dimacsvars" , 'a+')
        strList = [str(i) for i in selectedVars]
        bestConfigsFile.write(",".join(strList)+"\n")
        bestConfigsFile.close()
    if(len(selectedVars) == MAXDEPTH):
        #print("Found: " + str(selectedVars))
        genTempFile("", 0,experiment, TCL, VARS,selectedVars)
        output = Popen(["./sharpSAT -q "+ tempfile], stderr=open("/dev/null", "w"),stdout=PIPE,shell=True)
        val = output.stdout.read()
        
        #print(str(float(1)/pow(2,MAXDEPTH)) + " , " + str(float(val)/totalConfigs) )
        return True
    
    pairs = getPairs(TCL, VARS, selectedVars)
    #print pairs
    topPairs = getTopPairs(pairs)
    #print topPairs
    while True:
        myvar = choice(topPairs)
        if dimacs_map[myvar].startswith("k!"):
            #print "found k"
            continue
        res = getBestFeatures(workingdir,experiment, TCL,VARS, selectedVars+[-(myvar)], totalConfigs)
        res2 = getBestFeatures(workingdir,experiment, TCL,VARS, selectedVars+[(myvar)], totalConfigs)
        if res and res2:
            break
    '''while True:
        myvar = choice(topPairs)
        if dimacs_map[myvar].startswith("k!"):
            #print "found k"
            continue
        
        if res:
            break
    '''
    return True


        
        



def main(experiment, maxdepth=1, workingdir=""):
    global MAXDEPTH
    MAXDEPTH=maxdepth
    global dimacs_map
    if experiment == "SHP":
        TCL=634
        VARS=329
        dimacs_map = getDimacsMap(SHP.s)
    elif experiment == "WPT":
        TCL=114
        VARS=53
        dimacs_map = getDimacsMap(WPT.s)
    elif experiment == "ERS":
        TCL=190
        VARS=61
        dimacs_map = getDimacsMap(ERS.s)
    #genCombConfigFile(experiment, combs, outfile, TCL, VARS)
    global tempfile
    tempfile = workingdir+tempfile + experiment + "_" + str(maxdepth)
    genTempFile("", 0,experiment, TCL, VARS,[])
    output = Popen(["./sharpSAT -q " + tempfile], stderr=open("/dev/null", "w"),stdout=PIPE,shell=True)
    val=int(output.stdout.read())
    #print("Total Configs: " + str(val))
    for i in range(MAXDEPTH+1):
        try:
            os.remove(workingdir + experiment + ".bestconfigs." + str(i))
        except:
            pass
    getBestFeatures(workingdir,experiment, TCL, VARS, [], val)


if __name__ == '__main__':
    #sys.argv.append("ERS")
    #sys.argv.append(3)
    #sys.argv.append("")
    ########
    experiment = sys.argv[1]
    depth = int(sys.argv[2])
    workingdir = sys.argv[3] 
    start = time.time()
    main(experiment, depth, workingdir)
    print(time.time() - start)
    
    
'''
def getBestFeaturesForOne(experiment, TCL, VARS, selectedVars, totalConfigs):
    #print(selectedVars)
    if(len(selectedVars) == MAXDEPTH):
        print("Found: " + str(selectedVars))
        genTempFile("", 0,experiment, TCL, VARS,selectedVars)
        output = Popen(["./sharpSAT -q " + tempfile], stderr=open("/dev/null", "w"),stdout=PIPE,shell=True)
        val = output.stdout.read()
        
        print(str(float(1)/pow(2,MAXDEPTH)) + " , " + str(float(val)/totalConfigs) )
        return True
    
    pairs = getPairs(TCL,VARS,selectedVars)
    print(pairs)
    topPairs = getTopPairs(pairs)
    print topPairs
    sys.exit()
    for i in range(len(pairs)):
        res = getBestFeatures(experiment, TCL,VARS, selectedVars+[-(pairs[i][0])], totalConfigs)
        if res:
            break
    for i in range(len(pairs)):
        res = getBestFeatures(experiment, TCL,VARS, selectedVars+[(pairs[i][0])], totalConfigs)
        if res:
            break
    return True
'''
