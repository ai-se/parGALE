'''
Created on Nov 21, 2013

@author: ezulkosk
'''
from FeatureSplitConfig import ers_better_config_names, \
    eshop_better_config_names, webportal_better_config_names, ers_optional_names, \
    bdb_optional_names, webportal_optional_names, eshop_optional_names, \
    ers_config_split_names, webportal_config_split_names, eshop_config_split_names, \
    bdb_config_split_names
from consts import METRICS_MAXIMIZE, METRICS_MINIMIZE

from npGIAforZ3 import GuidedImprovementAlgorithm, \
    GuidedImprovementAlgorithmOptions
from z3 import *
import Z3ModelEShopUpdate as SHP_Min
import Z3ModelEmergencyResponseUpdate as ERS_Min
import Z3ModelWebPortalUpdate as WPT_Min
import argparse
import csv
import importlib
import itertools
import math
import multiprocessing
import operator
import os
import sys
import time




#from Z3ModelEmergencyResponseUpdateAllMin import *
#from Z3ModelWebPortal import *

RECORDPOINT = False

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue, totalTime, index, outputFileParentName, num_consumers, s, extraConstraint):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
#         self.CurrentNotDomConstraints_queuelist = CurrentNotDomConstraints_queuelist
        self.totalTime = totalTime 
        self.index = index
        self.outputFileParentName = outputFileParentName
        self.num_consumers = num_consumers
        self.GIAOptions = GuidedImprovementAlgorithmOptions(verbosity=0, \
                        incrementallyWriteLog=False, \
                        writeTotalTimeFilename="timefile.csv", \
                        writeRandomSeedsFilename="randomseed.csv", useCallLogs=False)    
        ''' add extra constraint'''
        #print extraConstraint
        s.add(extraConstraint)
        
        self.GIAAlgorithm = GuidedImprovementAlgorithm(s, metrics_variables, \
                    metrics_objective_direction, FeatureVariable, options=self.GIAOptions)
        
        self.count_sat_calls = 0
        self.count_unsat_calls = 0
        self.count_paretoPoints = 0
        self.startTime = time.time()

    def run(self):
        while True:
            if self.task_queue[self.index].empty() == True:
                break
            else:
                next_task = self.task_queue[self.index].get(False)
                if next_task is None:
                    self.task_queue[self.index].task_done()
                    self.totalTime.put(str(time.time()-self.startTime))
                    outputFileChild = open(str(str(self.outputFileParentName)+'C'+str(self.index)+'.csv'), 'a')
                    try:
                        outputFileChild.writelines(str(self.index)+','+
                                                   str(self.count_paretoPoints) + ',' +
                                                   str(self.count_sat_calls) + ',' +
                                                   str(self.count_unsat_calls) + ',' +
                                                   str(time.time()-self.startTime) +',' +
                                                   '\n')
                    finally:
                        outputFileChild.close()
                    
                    
                    break
                
                start_time = time.time()
            
                if self.GIAAlgorithm.s.check() != sat:
                    self.count_unsat_calls += 1
                    self.task_queue[self.index].put(None)
                else:
                    self.count_sat_calls += 1
                    self.task_queue[self.index].put("Task")      
                    prev_solution = self.GIAAlgorithm.s.model()
                    self.GIAAlgorithm.s.push()
                    NextParetoPoint, local_count_sat_calls, local_count_unsat_calls = self.GIAAlgorithm.ranToParetoFront(prev_solution)
                    end_time = time.time()
                    self.count_sat_calls += local_count_sat_calls
                    self.count_unsat_calls += local_count_unsat_calls
                    self.count_paretoPoints += 1
                 
                    self.GIAAlgorithm.s.pop()
                    tmpNotDominatedByNextParetoPoint = self.GIAAlgorithm.ConstraintNotDominatedByX(NextParetoPoint)
                    self.GIAAlgorithm.s.add(tmpNotDominatedByNextParetoPoint)
                    
                    # picklize and store Pareto point and constraints
                    strNextParetoPoint = list((d.name(), str(NextParetoPoint[d])) for d in NextParetoPoint.decls())
                    self.result_queue.put(strNextParetoPoint)
                    
                    # RecordPoint
                    if RECORDPOINT:
                        strNextParetoPoint = list((d.name(), str(NextParetoPoint[d])) for d in NextParetoPoint.decls())
                        outputFileChild = open(str(str(self.outputFileParentName)+'C'+str(self.index)+'.points'), 'a')
                        try:
                            outputFileChild.writelines(str(self.index)+','+
                                                       str(self.count_paretoPoints) + ',' +
                                                       str(self.count_sat_calls) + ',' +
                                                       str(end_time-start_time) +',' +
                                                       str(strNextParetoPoint) +',' +
                                                       '\n')
                        finally:
                            outputFileChild.close()
                    

                    self.task_queue[self.index].task_done()
        return 0



def getConstraintFromFile(s, infilename, constraint_index):
    infile = open(infilename,'r')
    lines=infile.readlines()
    myvars = lines[constraint_index].split(",")
    myvars = [i.strip() for i in myvars]
    mynots = []
    mynewvars = []
    for var in myvars:
        if "$" in var:
            mynots.append(1)
            var = var.split("$")[1]
            mynewvars.append(var)
        else:
            mynots.append(0)
            mynewvars.append(var)
    myvars = mynewvars
    #print myvars
    #print mynots
    
    new_desired_features= []
    for i in myvars:
        for j in s.assertions():
            result = getZ3Feature(i, j)
            if result:
                new_desired_features.append(result)
                break
    desired_features = new_desired_features      
    #print desired_features
    assert(len(desired_features) == len(myvars))
    cons = []
    for i in zip(desired_features, mynots):
        (f, mynot) = i
        if mynot == 1:
            cons.append(z3.Not(f))
        else:
            cons.append(f)
    cons = And(cons)
    print cons
    infile.close()
    return cons

def generateConsumerConstraints(features):
    list_of_list_of_perms = [itertools.combinations(features, i) for i in range(len(features)+1)]
    conds = []
    for list_of_perms in list_of_list_of_perms:
        for perm in list_of_perms:
            str_perm = [str(i) for i in perm]
            cond = []
            for feature in features:
                if str(feature) in str_perm:
                    cond.append(feature)
                else:
                    cond.append(Not(feature))
            conds.append(And(*cond))
    return conds    


def getWeightRanges(weights):
    Max = {}
    Min = {}
    for i in weights:
        (objective, weight, feature) = i
        if Max.get(str(objective)):
            currMin = Min.get(str(objective))
            currMax = Max.get(str(objective))
            Min[str(objective)] = currMin if weight > currMin else weight
            Max[str(objective)] = currMax if weight < currMax else weight
        else:
            Min[str(objective)] = weight
            Max[str(objective)] = weight
    #print Max
    #print Min
    return (Max, Min)


def replicateSolver(solver, num_consumers):
    solvers = []
    for i in range(num_consumers):
        newSolver =Solver()
        for j in solver.assertions():
            newSolver.add(j)
        solvers.append(newSolver)
    return solvers    


def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)
'''
def extractWeights(c, weights = [], curr_objective=None):    
    
    
    
    k = c.decl().kind()
    if k == Z3_OP_MUL:
        #print(c.children()[0])
        try:
            print str(c.children()[0])
            weights.append((curr_objective, 
                            int(str(c.children()[0])), 
                            c.children()[1].children()[0]))
            
        except:
            print("Not handling multiplicative")
            #return weights
            pass
    if k == Z3_OP_EQ and (str(c.children()[0].sort()) == "Int" or str(c.children()[0].sort()) == "Real"):
        curr_objective = c.children()[0]
    for child in c.children():
        weights = extractWeights(child, weights, curr_objective)
    return weights
'''

#(objective, weight, feature)
def extractWeights(csvfile):
    weights = []
    ifile  = open(csvfile, "rb")
    reader = csv.reader(ifile)
    for row in reader:
        if row[2]==  'false':
            row[2] = 0
        elif row[2] == 'true':
            row[2] = 1
        weights.append((row[1], float(row[2]), row[0]))
    return weights

def getBestForGreatestTotalWeight(num_consumers):
    '''
    weights is a list of triples: (objective, weight, feature)
    
    Sort features according to weights, 
    where the weight of a feature is defined as:
      
    weight(f:feature) = abs(Sum("f's weights in maximize objectives") 
                            - Sum("f's weights in minimize objectives"))
    
    ...might be better to look at std dev.
    ''' 
    weights =[] # this used to be different....
    features = {}
    features_str = {}
    metrics_variables_string = [str(i) for i in metrics_variables]
    for i in weights:
        (objective, weight, feature) = i
        if features.get(str(feature)):
            currWeight = features[str(feature)]
        else:
            currWeight = 0
            features_str[str(feature)] = feature
        polarity = metrics_objective_direction[metrics_variables_string.index(str(objective))]
        if(polarity == METRICS_MINIMIZE):
            polarity = -1
        currWeight = currWeight + polarity * weight
        features[str(feature)] = currWeight
    
    sorted_features = sorted(features.iteritems(), key=operator.itemgetter(1))
    sorted_features = [(features_str[f],abs(w)) for (f, w) in sorted_features]
    #sorted_features.reverse()
    return sorted_features

def getBestForAbsoluteNormalized(weights, ranges, num_consumers):
    '''
    weights is a list of triples: (objective, weight, feature)
    
    Sort features according to weights, 
    where the weight of a feature is defined as:
      
    weight(f:feature) = abs(Sum("f's weights in maximize objectives") 
                            - Sum("f's weights in minimize objectives"))
    
    ...might be better to look at std dev.
    ''' 
    features = {}
    features_str = {}
    #print weights
    (maxes, mins) = ranges
    metrics_variables_string = [str(i) for i in metrics_variables]
    
    #print weights
    for i in weights:
        (objective, weight, feature) = i
        if features.get(str(feature)):
            currWeight = features[str(feature)]
        else:
            currWeight = 0
            features_str[str(feature)] = feature
            #print objective
        polarity = metrics_objective_direction[metrics_variables_string.index(str(objective))]
        #print objective
        if maxes[str(objective)] - mins[str(objective)] == 0:
            currWeight = currWeight + 1
        elif(polarity == METRICS_MAXIMIZE):
            currWeight = currWeight + (float(weight) - mins[str(objective)]) / (maxes[str(objective)] - mins[str(objective)]) 
        else:
            currWeight = currWeight + (maxes[str(objective)] - float(weight)) / (maxes[str(objective)] - mins[str(objective)]) 
        features[str(feature)] = currWeight
    
    sorted_features = sorted(features.iteritems(), key=operator.itemgetter(1))
    sorted_features = [(features_str[f],abs(w)) for (f, w) in sorted_features]
    #print sorted_features
    #sorted_features.reverse()
    return sorted_features

def getBestMinusWorst(weights, ranges, num_consumers, metric_vars ,metrics_dirs):
     
    features = {}
    features_str = {}
    #print weights
    (maxes, mins) = ranges
    metrics_variables_string = [str(i) for i in metric_vars]
    
    #print weights
    for i in weights:
        (objective, weight, feature) = i
        if features.get(str(feature)):
            currWeight = features[str(feature)]
        else:
            currWeight = (1, 0)
            features_str[str(feature)] = feature
            #print objective
        (currMin, currMax) = currWeight
        
        polarity = metrics_dirs[metrics_variables_string.index("total_" + str(objective))]
        #print objective
        if maxes[str(objective)] - mins[str(objective)] == 0:
            denom = 1
        else:
            denom = (maxes[str(objective)] - mins[str(objective)])
        if(polarity == METRICS_MAXIMIZE):
            newWeight =  (float(weight) - mins[str(objective)]) /denom
        else:
            newWeight =  (maxes[str(objective)] - float(weight)) / denom
        #print features
        #print(newWeight if newWeight < currMin else currMin)
        #print newWeight
        features[str(feature)] = (newWeight if newWeight < currMin else currMin, newWeight if newWeight > currMax else currMax)
    
    for i in features.keys():
        (l, r) = features.get(i)
        features[i] = r - l 
    sorted_features = sorted(features.iteritems(), key=operator.itemgetter(1))
    sorted_features = [(features_str[f],abs(w)) for (f, w) in sorted_features]
    #print sorted_features
    #sorted_features.reverse()
    return sorted_features
    
def getBestByName(num_consumers, weights, names):
    #need to clean
    
    
    features=[]
    for i in weights:
        (name, weight) = i
        if str(name) in names:
            #print name
            features.append((name,weight))
    '''
    while names:
        for i in weights:
            
            (_, _, feature) = i
            if str(feature) == names[0]:
                print names[0]
                features.append((feature,1))
                names.pop(0)
                break
                '''
    #print features
    return features



def getBestFeatures(heuristic, weights, ranges, num_consumers, names, metric_vars, metrics_dirs):
    
    if heuristic == GREATEST_TOTAL_WEIGHT:
        print("Obsolete, do not use. ")
        #sys.exit()
        return getBestForGreatestTotalWeight(num_consumers)
    elif heuristic == ABSOLUTE_NORMALIZED:
        return getBestForAbsoluteNormalized(weights, ranges, num_consumers)
    elif heuristic == BY_NAME:
        #initial_list = getBestForAbsoluteNormalized(weights, ranges, num_consumers)
        #initial_list.reverse()
        initial_list = getBestMinusWorst(weights, ranges, num_consumers, metric_vars, metrics_dirs)
        return getBestByName(num_consumers, initial_list, names)
    


def getZ3Feature(feature, expr):
    #print("B")
    if(str(expr) == feature):
        return expr
    for child in expr.children():
        result = getZ3Feature(feature, child)
        if result:
            return result
    
    return []

ABSOLUTE_NORMALIZED = 1
GREATEST_TOTAL_WEIGHT = 2
BY_NAME = 3
CONFIG=False



def oldway():
    """
    #dead code....
    #oldway()
   
    if len(sys.argv) != 5:
        print "Usage: python featuresplit testID outputFile numCores config(1/0)"
        print("running defaults: ERS out 2 1")
        sys.argv.append("ESH")
        sys.argv.append("out")
        sys.argv.append("2")
        sys.argv.append("2")
        
    print("Running: " + str(sys.argv))

    if sys.argv[4] == "1":
        CONFIG = True
    else:
        CONFIG = False
    if sys.argv[4] == "2":
        BETTER_CONFIG = True
    else:
        BETTER_CONFIG = False
    #print CONFIG

    if sys.argv[1] == "BDB":
        RECORDPOINT=True
        from Z3ModelBerkeleyDB import *
        csvfile = './bdb_attributes.csv'
        if CONFIG:
            names = bdb_config_split_names
        elif BETTER_CONFIG:
            sys.exit("bdb not set up for better config.")
        else:
            names = bdb_optional_names
    elif sys.argv[1] == "ERS":
        csvfile = './ers_attributes.csv'
        #RECORDPOINT=True
        from Z3ModelEmergencyResponseOriginal import * 
        if CONFIG:
            names = ers_config_split_names
        elif BETTER_CONFIG:
            names = ers_better_config_names
        else:
            names = ers_optional_names

    elif sys.argv[1] == "ESH":
        RECORDPOINT=True
        from Z3ModelEShopUpdateAllMin import * 
        csvfile = './eshop_attributes.csv'
        if CONFIG:
            names = eshop_config_split_names
        elif BETTER_CONFIG:
            names = eshop_better_config_names
        else:
            names = eshop_optional_names
    elif sys.argv[1] == "WPT":
        csvfile = './wpt_attributes.csv'
        from Z3ModelWebPortalUpdate import * 
        #names=["ban_flash", "keyword", "popups", "text"]
        if CONFIG:
            names = webportal_config_split_names
        elif BETTER_CONFIG:
            names = webportal_better_config_names

        else:
            names = webportal_optional_names
    else:
        print("passed")
        sys.exit()
    outputFileParentName = sys.argv[2]
    num_consumers = int(sys.argv[3])
    if not is_power2(num_consumers):
        sys.exit("Number of consumers must be a power of 2.")
    
    
    weights = extractWeights(csvfile)
    #print weights
    
  
    ranges = getWeightRanges(weights)
    
    #print(weights) 
    #print(ranges)
    
    sorted_features = getBestFeatures(BY_NAME, weights, ranges, num_consumers, names, metrics_variables, metrics_objective_direction)
    num_desired_features = int(math.log(num_consumers, 2))
    #i didnt reverse, but also try middle of the pack
    sorted_features.reverse()
    print sorted_features
    #random.shuffle(sorted_features)
    desired_features = [i for (i, _) in sorted_features][:num_desired_features]
    #desired_features = [i for (i, _) in sorted_features][(len(sorted_features)-num_desired_features)/2:
    #                                                     (len(sorted_features)-num_desired_features)/2 + num_desired_features]
    
    #print desired_features
    new_desired_features= []
    for i in desired_features:
        for j in s.assertions():
            result = getZ3Feature(i, j)
            if result:
                new_desired_features.append(result)
                break
    desired_features = new_desired_features      
    print desired_features
    consumerConstraints = generateConsumerConstraints(desired_features)
    """
    
if __name__ == '__main__':
    
    sys.argv.append("ERS")
    sys.argv.append("bestvars")
    sys.argv.append("out")
    sys.argv.append(16) 
    sys.argv.append("recordpointfile")
    ########################
    recordpointfile = sys.argv[5]
    experiment = sys.argv[1]
    num_consumers = int(sys.argv[4])
    file_ext = str(int(math.log(int(sys.argv[4]),2)))
    outfile=sys.argv[3]
    infilename = sys.argv[2]
    ########################
    if experiment == "SHP":
        from Z3ModelEShopUpdate import * 
        INPUT = SHP_Min
        RECORDPOINT = True
    elif experiment == "WPT":
        from Z3ModelWebPortalUpdate import * 
        INPUT = WPT_Min
    elif experiment == "ERS":
        from Z3ModelEmergencyResponseUpdate import * 
        INPUT = ERS_Min    
    
    consumerConstraints = [getConstraintFromFile(INPUT.s, infilename, i) for i in range(num_consumers)]
    #print consumerConstraints
    #sys.exit()
    #INPUT.s.add(consumerConstraints)
    solvers = replicateSolver(s, num_consumers)
    
    mgr = multiprocessing.Manager()
    taskQueue = []
    for i in xrange(num_consumers):
        taskQueue.append(mgr.Queue())
    ParetoFront = mgr.Queue()
    totalTime = mgr.Queue()
    
    # Enqueue initial tasks
    for i in xrange(num_consumers):
        taskQueue[i].put("Task")
        
    # Start consumers
    #print 'Creating %d consumers' % num_consumers
    consumersList = [ Consumer(taskQueue, ParetoFront, totalTime, i, outfile, num_consumers, j, k)
                    for i,j,k in zip(xrange(num_consumers), solvers, consumerConstraints)]
    
    for w in consumersList:
        w.start()            
    
    for w in consumersList:
        w.join()  
        
    TotalOverlappingParetoFront = ParetoFront.qsize()
 
    
    runningtime = 0.0
    
    while totalTime.qsize() > 0:
        time = totalTime.get()
        if (float(time) > runningtime): 
            runningtime = float(time)
    
    outputFileParent = open(str(outfile+'.csv'), 'a')
    try:
        outputFileParent.writelines(str(num_consumers) + ',' + str(TotalOverlappingParetoFront) +',' + '0' + ',' + str(runningtime) + ',' + '\n')
    finally:
        outputFileParent.close()
    
