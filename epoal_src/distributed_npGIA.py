from FeatureSplitConfig import eshop_better_config_names
from consts import METRICS_MAXIMIZE, METRICS_MINIMIZE
from featuresplitGIA import getBestFeatures, getZ3Feature, \
    generateConsumerConstraints, extractWeights, getWeightRanges, \
    getConstraintFromFile
from npGIAforZ3 import GuidedImprovementAlgorithm, \
    GuidedImprovementAlgorithmOptions, RECORDPOINT, setRecordPoint
from z3 import *
import Z3ModelEShopUpdate as SHP_Min
import Z3ModelEmergencyResponseUpdate as ERS_Min
import Z3ModelWebPortalUpdate as WPT_Min
import argparse
import featuresplitGIA
import math
import multiprocessing
import os
import sys
import time

'''
INPUT: experiment outfile numcores constraintINDEX recordpointFile
NOTES:
 some config variables in npGIAforZ3:
    OUTPUT_PARETO_FRONT -- set to true if desired (for ERS possibly).
'''

#from Z3ModelEmergencyResponseUpdateAllMin import *
#from Z3ModelWebPortal import *


def getZ3Feature(feature, expr):
    if(str(expr) == feature):
        return expr
    for child in expr.children():
        result = getZ3Feature(feature, child)
        if result:
            return result
    return []

def getBestBySharpSat(num_consumers, weights, names):
    features=[]
    for i in weights:
        (name, weight) = i
        if str(name) in names:
            #print name
            features.append((name,weight))
    return features





if __name__ == '__main__':
    sys.argv.append("ERS")
    sys.argv.append("bestvars")
    sys.argv.append("out")
    sys.argv.append(16)
    sys.argv.append(4) 
    sys.argv.append("recordpointfile")
    ########################
    constraint_index = int(sys.argv[5])
    recordpointfile = sys.argv[6]
    experiment = sys.argv[1]
    file_ext = str(int(math.log(int(sys.argv[4]),2)))
    outfile=sys.argv[3]
    infilename = sys.argv[2]
    ########################
    if experiment == "SHP":
        from Z3ModelEShopUpdate import * 
        INPUT = SHP_Min
        setRecordPoint(True)
    elif experiment == "WPT":
        from Z3ModelWebPortalUpdate import * 
        INPUT = WPT_Min
    elif experiment == "ERS":
        from Z3ModelEmergencyResponseUpdate import * 
        INPUT = ERS_Min    
    
    cons = getConstraintFromFile(INPUT.s, infilename, constraint_index)
    INPUT.s.add(cons)
    
    ########################
    GIAOptionsNP = GuidedImprovementAlgorithmOptions(verbosity=0, \
        incrementallyWriteLog=False, \
        writeTotalTimeFilename="timefile.csv", \
        writeRandomSeedsFilename="randomseed.csv", useCallLogs=False)  
 
    GIAAlgorithmNP = GuidedImprovementAlgorithm(INPUT.s, INPUT.metrics_variables, \
            INPUT.metrics_objective_direction, INPUT.FeatureVariable, options=GIAOptionsNP)
    outfilename = str(outfile).strip()#"npGIA_" + str(sys.argv[1]).strip() + ".csv"
    GIAAlgorithmNP.ExecuteGuidedImprovementAlgorithm(outfilename, recordpointfile)

    
