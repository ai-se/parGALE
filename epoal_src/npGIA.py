from consts import METRICS_MAXIMIZE, METRICS_MINIMIZE
from npGIAforZ3 import GuidedImprovementAlgorithm, \
    GuidedImprovementAlgorithmOptions, RECORDPOINT, setRecordPoint
from src import featuresplitGIA
from src.FeatureSplitConfig import eshop_better_config_names
from src.featuresplitGIA import getBestFeatures, getZ3Feature, \
    generateConsumerConstraints, extractWeights, getWeightRanges
from z3 import *
import Z3ModelEShopOriginal as SHP_Min
import Z3ModelEmergencyResponseUpdateAllMin as ERS_Min
import Z3ModelWebPortalUpdateAllMin as WPT_Min
import argparse
import math
import multiprocessing
import os
import sys
import time

'''
INPUT: experiment outfile
NOTES:
 some config variables in npGIAforZ3:
    OUTPUT_PARETO_FRONT -- set to true if desired (for ERS possibly).
'''

#from Z3ModelEmergencyResponseUpdateAllMin import *
#from Z3ModelWebPortal import *


if __name__ == '__main__':
    sys.argv.append("ERS")
    sys.argv.append("out")
    sys.argv.append(16)
    sys.argv.append(4) 
    
    experiment = sys.argv[1]    
    if experiment == "SHP":
        from Z3ModelEShopOriginal import * 
        INPUT = SHP_Min
        setRecordPoint(True)
        if sys.argv[3]:
            names = eshop_better_config_names
            num_consumers=int(sys.argv[3])
            constraint_index = int(sys.argv[4])
            csvfile = './eshop_attributes.csv'
            weights = extractWeights(csvfile)
            ranges = getWeightRanges(weights)
            
            sorted_features = getBestFeatures(featuresplitGIA.BY_NAME, weights, ranges, num_consumers, names, metrics_variables, metrics_objective_direction) 
            num_desired_features = int(math.log(num_consumers, 2))
            #i didnt reverse, but also try middle of the pack
            sorted_features.reverse()
            print sorted_features
            #random.shuffle(sorted_features)
            desired_features = [i for (i, _) in sorted_features][:num_desired_features]
            
            new_desired_features= []
            for i in desired_features:
                for j in SHP_Min.s.assertions():
                    result = getZ3Feature(i, j)
                    if result:
                        new_desired_features.append(result)
                        break
            desired_features = new_desired_features      
            print desired_features
            consumerConstraints = generateConsumerConstraints(desired_features)
            print consumerConstraints
    elif experiment == "WPT":
        INPUT = WPT_Min
    elif experiment == "ERS":
        INPUT = ERS_Min
    # Non-Parallel    
    print consumerConstraints[constraint_index]
    GIAOptionsNP = GuidedImprovementAlgorithmOptions(verbosity=0, \
        incrementallyWriteLog=False, \
        writeTotalTimeFilename="timefile.csv", \
        writeRandomSeedsFilename="randomseed.csv", useCallLogs=False)
    INPUT.s.add(consumerConstraints[constraint_index])   
 
    GIAAlgorithmNP = GuidedImprovementAlgorithm(INPUT.s, INPUT.metrics_variables, \
            INPUT.metrics_objective_direction, INPUT.FeatureVariable, options=GIAOptionsNP)
    outfilename = str(sys.argv[2]).strip()#"npGIA_" + str(sys.argv[1]).strip() + ".csv"
    print(INPUT.s.check())
    GIAAlgorithmNP.ExecuteGuidedImprovementAlgorithm(outfilename)

    