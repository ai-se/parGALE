from consts import METRICS_MAXIMIZE, METRICS_MINIMIZE
from npGIAforZ3 import GuidedImprovementAlgorithm, \
    GuidedImprovementAlgorithmOptions
from npGIAforZ3 import setRecordPoint
from z3 import *
import Z3ModelEShopUpdateAllMin as SHP_Min
import Z3ModelEmergencyResponseUpdateAllMin as ERS_Min
import Z3ModelWebPortalUpdateAllMin as WPT_Min
import argparse
import multiprocessing
import os
import sys
import time
import math

#from Z3ModelEmergencyResponseUpdateAllMin import *
#from Z3ModelWebPortal import *

'''
INPUT: experiment outfile num_consumers
'''

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue, totalTime, index, outputFileParentName, num_consumers, s, INPUT):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
#         self.CurrentNotDomConstraints_queuelist = CurrentNotDomConstraints_queuelist
        self.totalTime = totalTime
        self.index = index
        self.outputFileParentName = outputFileParentName
        self.num_consumers = num_consumers
        
        # split the objective space
        # maximum 30 cores -> minimum 3 degrees, so we use range [degree-1, degree+1)
        degree = 90.0 / self.num_consumers
        # radian = degree * math.pi / 180.0
        splitRuleList = []
        if sys.argv[1]  == "ERS":
            if (self.index == 0):
                # from the reference point with a larger angle -> a bigger range
    #             radian_higher = (degree + 1) * math.pi / 180.0
                radian_higher = (degree) * math.pi / 180.0
                gradient_higher = int(1000*round(math.tan(radian_higher), 3))
                # squarization
                # choosing "the two best" dimensions of the projective plane could be an interesting problem
                # try to use Shannon Diversity Index, but seems not working; i think it only works when we normalize all values into [0, 1]
                # so, still use the two dimensions with the maximum value range
                # the challenge is how to know the scattering of configurations in the objective space, given the quality attributes of each feature? 
    #             splitRuleList.append( 1000 * (total_rampuptime - 130) * 121 >= IntVal(gradient_higher) * (total_batteryusage - 121) * 130 )
                splitRuleList.append( 1000 * (INPUT.total_responsetime - 2070) * 629 >= IntVal(gradient_higher) * (INPUT.total_cost - 3145) * 414 )
                tmpsplitRuleList = And(splitRuleList)
                print str(self.index) + " >= " + str(gradient_higher)            
                print tmpsplitRuleList
                s.add(tmpsplitRuleList)
            elif (self.index == self.num_consumers-1):
                # from the reference point with a smaller angle -> a bigger range
    #             radian_lower = (degree * self.index - 1) * math.pi / 180.0
                radian_lower = (degree * self.index) * math.pi / 180.0
                gradient_lower = int(1000*round(math.tan(radian_lower), 3))
    #             splitRuleList.append( 1000 * (total_rampuptime - 130) * 121 < IntVal(gradient_lower) * (total_batteryusage - 121) * 130 ) 
                splitRuleList.append( 1000 * (INPUT.total_responsetime - 2070) * 629 < IntVal(gradient_lower) * (INPUT.total_cost - 3145) * 414 )
                tmpsplitRuleList = And(splitRuleList)
                print str(self.index) + " < " + str(gradient_lower)
                print tmpsplitRuleList
                s.add(tmpsplitRuleList)   
            else:
    #             radian_lower = (degree * self.index - 1) * math.pi / 180.0
                radian_lower = (degree * self.index) * math.pi / 180.0
                gradient_lower = int(1000*round(math.tan(radian_lower), 3))
    #             splitRuleList.append( 1000 * (total_rampuptime - 130) * 121 < IntVal(gradient_lower) * (total_batteryusage - 121) * 130 )
                splitRuleList.append( 1000 * (INPUT.total_responsetime - 2070) * 629 < IntVal(gradient_lower) * (INPUT.total_cost - 3145) * 414 )
    #             radian_higher = (degree * (self.index+1) + 1) * math.pi / 180.0
                radian_higher = (degree * (self.index+1)) * math.pi / 180.0
                gradient_higher = int(1000*round(math.tan(radian_higher), 3))
    #             splitRuleList.append( 1000 * (total_rampuptime - 130) * 121 >= IntVal(gradient_higher) * (total_batteryusage - 121) * 130 )
                splitRuleList.append( 1000 * (INPUT.total_responsetime - 2070) * 629 >= IntVal(gradient_higher) * (INPUT.total_cost - 3145) * 414 )  
                tmpsplitRuleList = And(splitRuleList)
                print str(self.index) + " >= " + str(gradient_higher) + " < " + str(gradient_lower)          
                print tmpsplitRuleList
                s.add(tmpsplitRuleList)   
        elif sys.argv[1] == "WPT":
            if (self.index == 0):
                # from the reference point with a larger angle -> a bigger range
    #             radian_higher = (degree + 1) * math.pi / 180.0
                radian_higher = (degree) * math.pi / 180.0
                gradient_higher = int(1000*round(math.tan(radian_higher), 3))
    #             print str(self.index) + ">=" + str(gradient_higher)
                # squarization
                # choosing "the two best" dimensions of the projective plane could be an interesting problem
                # try to use Shannon Diversity Index, but seems not working; i think it only works when we normalize all values into [0, 1]
                # so, still use the two dimensions with the maximum value range
                # the challenge is how to know the scattering of configurations in the objective space, given the quality attributes of each feature? 
    #             splitRuleList.append( 1000 * (total_rampuptime - 13) * 10 >= IntVal(gradient_higher) * (total_batteryusage - 10) * 13 )
                splitRuleList.append( 1000 * (INPUT.total_Cost - 422) * 145 >= IntVal(gradient_higher) * (INPUT.total_Defects - 145) * 422 )
                tmpsplitRuleList = And(splitRuleList)
                s.add(tmpsplitRuleList)
            elif (self.index == self.num_consumers-1):
                # from the reference point with a smaller angle -> a bigger range
    #             radian_lower = (degree * self.index - 1) * math.pi / 180.0
                radian_lower = (degree * self.index) * math.pi / 180.0
                gradient_lower = int(1000*round(math.tan(radian_lower), 3))
    #             print str(self.index) + "<" + str(gradient_lower)
    #             splitRuleList.append( 1000 * (total_rampuptime - 13) * 10 < IntVal(gradient_lower) * (total_batteryusage - 10) * 13 ) 
                splitRuleList.append( 1000 * (INPUT.total_Cost - 422) * 145 < IntVal(gradient_lower) * (INPUT.total_Defects - 145) * 422 )
                tmpsplitRuleList = And(splitRuleList)
                s.add(tmpsplitRuleList)   
            else:
    #             radian_lower = (degree * self.index - 1) * math.pi / 180.0
                radian_lower = (degree * self.index) * math.pi / 180.0
                gradient_lower = int(1000*round(math.tan(radian_lower), 3))
    #             splitRuleList.append( 1000 * (total_rampuptime - 13) * 10 < IntVal(gradient_lower) * (total_batteryusage - 10) * 13 )
                splitRuleList.append( 1000 * (INPUT.total_Cost - 422) * 145 < IntVal(gradient_lower) * (INPUT.total_Defects - 145) * 422 )
    #             radian_higher = (degree * (self.index+1) + 1) * math.pi / 180.0
                radian_higher = (degree * (self.index+1)) * math.pi / 180.0
                gradient_higher = int(1000*round(math.tan(radian_higher), 3))
    #             splitRuleList.append( 1000 * (total_rampuptime - 13) * 10 >= IntVal(gradient_higher) * (total_batteryusage - 10) * 13 )
                splitRuleList.append( 1000 * (INPUT.total_Cost - 422) * 145 >= IntVal(gradient_higher) * (INPUT.total_Defects - 145) * 422 )  
    #             print str(self.index) + ">=" + str(gradient_higher) + "<" + str(gradient_lower)          
                tmpsplitRuleList = And(splitRuleList)
                s.add(tmpsplitRuleList)   
        else:
            print "Messed up"
            sys.exit()
        
        self.GIAOptions = GuidedImprovementAlgorithmOptions(verbosity=0, \
                        incrementallyWriteLog=False, \
                        writeTotalTimeFilename="timefile.csv", \
                        writeRandomSeedsFilename="randomseed.csv", useCallLogs=False)    

        self.GIAAlgorithm = GuidedImprovementAlgorithm(s, INPUT.metrics_variables, \
                    INPUT.metrics_objective_direction, INPUT.FeatureVariable, options=self.GIAOptions)
        
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
                
                # execute a task, i.e., find a Pareto point
                # 1) update CurrentNotDomConstraints
#                 while self.CurrentNotDomConstraints_queuelist[self.index].empty() != True:
#                     strconstraintlist = self.CurrentNotDomConstraints_queuelist[self.index].get()
#                     ConvertedZ3ConstraintList  = list()
#                     for constraint in strconstraintlist:
#                         #print constraint
#                         # eval() may lose precision, for example, eval(9962778141/19531250000) = 0
#                         # that's why we need repr(), but not work for z3
#                         # split constraint via > or <
#                         constraintSplitList = []
#                         if constraint.find('>') != -1:
#                             constraintSplitList = constraint.split('>')                    
#                             #print constraintSplitList
#                             if constraintSplitList[1].find('/') != -1:
#                                 ConvertedZ3ConstraintList.append( Real(constraintSplitList[0].strip()) > RealVal(constraintSplitList[1].strip()))
#                             else:
#                                 ConvertedZ3ConstraintList.append( Int(constraintSplitList[0].strip()) > IntVal(constraintSplitList[1].strip()))
#                             #print ConvertedZ3ConstraintList
#                         else:
#                             constraintSplitList = constraint.split('<') 
#                             #print constraintSplitList
#                             if constraintSplitList[1].find('/') != -1:
#                                 ConvertedZ3ConstraintList.append( Real(constraintSplitList[0].strip()) < RealVal(constraintSplitList[1].strip()))
#                             else:
#                                 ConvertedZ3ConstraintList.append( Int(constraintSplitList[0].strip()) < IntVal(constraintSplitList[1].strip()))
#                             #print ConvertedZ3ConstraintList                   
#                     #print Or(ConvertedZ3ConstraintList)
#                     tmpNotDominatedByNextParetoPoint = Or(ConvertedZ3ConstraintList)
#                     #print tmpNotDominatedByNextParetoPoint            
#                     self.GIAAlgorithm.s.add(tmpNotDominatedByNextParetoPoint)
                
                # 2) if find all Pareto points, add a poison pill; otherwise find a Pareto point
                
                if self.GIAAlgorithm.s.check() != sat:
                    self.count_unsat_calls += 1
                    self.task_queue[self.index].put(None)
                else:
                    self.count_sat_calls += 1
                    self.task_queue[self.index].put("Task")      
                    prev_solution = self.GIAAlgorithm.s.model()
                    self.GIAAlgorithm.s.push()
                    NextParetoPoint, local_count_sat_calls, local_count_unsat_calls = self.GIAAlgorithm.ranToParetoFront(prev_solution)
                    self.count_sat_calls += local_count_sat_calls
                    self.count_unsat_calls += local_count_unsat_calls
                    self.count_paretoPoints += 1
                    #                 #for EShop
#                   outputFile = open(outfilename, 'a')
#                   try:
#                       outputFile.writelines('Found Pareto Points ' + str(count_paretoPoints) + ',' +
#                                         '\n')
#                   finally:
#                       outputFile.close()
                    self.GIAAlgorithm.s.pop()
                    tmpNotDominatedByNextParetoPoint = self.GIAAlgorithm.ConstraintNotDominatedByX(NextParetoPoint)
                    self.GIAAlgorithm.s.add(tmpNotDominatedByNextParetoPoint)
                    
                    # picklize and store Pareto point and constraints
                    strNextParetoPoint = list((d.name(), str(NextParetoPoint[d])) for d in NextParetoPoint.decls())
                    self.result_queue.put(strNextParetoPoint)
                    
#                     constraintlist = self.GIAAlgorithm.EtractConstraintListNotDominatedByX(NextParetoPoint)
#                     strconstraintlist = list(str(item) for item in constraintlist)
#                     for j in xrange(len(self.CurrentNotDomConstraints_queuelist)):
#                         if j != self.index:
#                             self.CurrentNotDomConstraints_queuelist[j].put(strconstraintlist)
                    self.task_queue[self.index].task_done()
        return 0

   
def replicateSolver(solver, num_consumers):
    solvers = []
    for i in range(num_consumers):
        newSolver =Solver()
        for j in solver.assertions():
            newSolver.add(j)
        solvers.append(newSolver)
    return solvers    
   
   
if __name__ == '__main__':

    experiment = sys.argv[1]
    if experiment == "SHP":
        INPUT = SHP_Min
        setRecordPoint(True)
    elif experiment == "WPT":
        INPUT = WPT_Min
    elif experiment == "ERS":
        INPUT = ERS_Min

    num_consumers = int(str(sys.argv[3]).strip())
    solvers = replicateSolver(INPUT.s, num_consumers)
    #num_consumers = 3
    outputFileParentName = str(sys.argv[2]).strip()
    #outputFileParentName = "testPPGIA_ERS_P3"
    
    # Establish communication queues
    mgr = multiprocessing.Manager()
    taskQueue = []
    for i in xrange(num_consumers):
        taskQueue.append(mgr.Queue())
    ParetoFront = mgr.Queue()
    totalTime = mgr.Queue()
#     CurrentNotDomConstraintsQueueList = []
#     for i in xrange(num_consumers):
#         CurrentNotDomConstraintsQueueList.append(mgr.Queue())
    
    # Enqueue initial tasks
    for i in xrange(num_consumers):
        taskQueue[i].put("Task")
        
    # Start consumers
    #print 'Creating %d consumers' % num_consumers
    consumersList = [ Consumer(taskQueue, ParetoFront, totalTime, i, outputFileParentName, num_consumers, solvers[i], INPUT)
                    for i in xrange(num_consumers)]
    starttime = time.time()
    for w in consumersList:
        w.start()            
    
    for w in consumersList:
        w.join()  
        
#         print "The number of all found Pareto Points (may overlapping) ", ParetoFront.qsize()
    TotalOverlappingParetoFront = ParetoFront.qsize()
 
######## Verify whether the algorithm finds all true Pareto Points? Yes    
#     print TotalOverlappingParetoFront;
#     
#     ParetoPointsList=[]
#     while ParetoFront.qsize() > 0:
#         paretoPoint = ParetoFront.get()
#         if paretoPoint in ParetoPointsList:
#             pass
#         else:
#             ParetoPointsList.append(paretoPoint)
#  
#     TotalUniqueParetoFront = len(ParetoPointsList)
#     
#     print TotalUniqueParetoFront;
#          
#     ParetoPointsList2 = []
#     for paretoPoint in ParetoPointsList:
#         dict = {}
#         for item in paretoPoint:
#              if( item[0] == 'total_batteryusage' or item[0] == 'total_cost' or item[0] == 'total_deploymenttime' or
#                  item[0] == 'total_developmenttime' or item[0] == 'total_rampuptime' or item[0] == 'total_reliability' or
#                  item[0] == 'total_responsetime' ):
#                  dict[str(item[0])] = str(item[1])
#         ParetoPointsList2.append(dict)
#      
#     ParetoPointsList1 = []
#     f = open('ERS_ParetoFront.csv', 'r')
#     for line in f:
#         dict = {}
#         #print line
#         itemlist = str(line).split(";")
#         for item in itemlist:
#             #print item
#             if item.strip() <> "":
#                 stritem = str(item).split(",")
#                 #print stritem[0].strip()[2:-1]
#                 #print stritem[1].strip()[1:-2]
#                 dict[str( stritem[0].strip()[2:-1] )] = str( stritem[1].strip()[1:-2] )
#         ParetoPointsList1.append(dict)
#     
#     # Are all true points found?
#     truePoints = 0
#     for item in ParetoPointsList1:
#         if item in ParetoPointsList2:
#             truePoints += 1
#     print "True standard points: " + str(truePoints)
#     
#     # how many points are in Standard front?
#     foundtruePoints = 0
#     for item in ParetoPointsList2:
#         if item in ParetoPointsList1:
#             foundtruePoints += 1
#     print "Found true standard points: " + str(foundtruePoints)
#     
#     # how many points are not in standard front?
#     print "Found false points: " + str(len(ParetoPointsList2) - foundtruePoints)
########        
            
    # recalculate ParetoFront -> does not work, because
    # Z3 using string to represent Rational number and compare Rational numbers using exact string representations,
    # so, converting Rational number to float cannot obtain the same results as Z3.
    # to this end, we can verify results using the above code to find true points
#     for i in xrange(len(ParetoPointsList2)):
#         isDominated = False
#         for j in xrange(i+1, len(ParetoPointsList2)):
#                 strlist1 = ParetoPointsList2[i]['total_reliability'].split("/")
#                 #print strlist1
#                 strlist2 = ParetoPointsList2[j]['total_reliability'].split("/")
#                 #print strlist2
#                 if (int(ParetoPointsList2[i]['total_cost']) >= int(ParetoPointsList2[j]['total_cost']) and 
#                     int(ParetoPointsList2[i]['total_responsetime']) >= int(ParetoPointsList2[j]['total_responsetime']) and
#                     int(ParetoPointsList2[i]['total_batteryusage']) >= int(ParetoPointsList2[j]['total_batteryusage']) and 
#                     int(ParetoPointsList2[i]['total_deploymenttime']) >= int(ParetoPointsList2[j]['total_deploymenttime']) and 
#                     int(ParetoPointsList2[i]['total_developmenttime']) >= int(ParetoPointsList2[j]['total_developmenttime']) and
#                     int(ParetoPointsList2[i]['total_rampuptime']) >= int(ParetoPointsList2[j]['total_rampuptime']) and
#                     # precision of reliability is 1/1000 
#                     round(float(strlist1[0])/float(strlist1[1]),12) >= round(float(strlist2[0])/float(strlist2[1]), 12)):
#                     isDominated = True
# #                     print str(i) + " dominated by " + str(j)
# #                     print str(int(ParetoPointsList2[i]['total_cost'])) + " cost >=" + str(int(ParetoPointsList2[j]['total_cost']))
# #                     print str(int(ParetoPointsList2[i]['total_responsetime'])) + "response >=" + str(int(ParetoPointsList2[j]['total_responsetime']))
# #                     print str(int(ParetoPointsList2[i]['total_batteryusage'])) + "battery >=" + str(int(ParetoPointsList2[j]['total_batteryusage']))
# #                     print str(int(ParetoPointsList2[i]['total_deploymenttime'])) + "deploy >=" + str(int(ParetoPointsList2[j]['total_deploymenttime']))
# #                     print str(int(ParetoPointsList2[i]['total_developmenttime'])) + "develp >=" + str(int(ParetoPointsList2[j]['total_developmenttime']))
# #                     print str(int(ParetoPointsList2[i]['total_rampuptime'])) + "rampup >=" + str(int(ParetoPointsList2[j]['total_rampuptime']))
# #                     print str(strlist1[0]) + "/" + str(strlist1[1])  + "reliability >=" + str(strlist2[0]) + "/" + str(strlist2[1])
# #                     print str(round(float(strlist1[0])/float(strlist1[1]),3)) +"reliability >=" + str(round(float(strlist2[0])/float(strlist2[1]), 3))
#                     break;
#         if isDominated == True: 
#             TotalUniqueParetoFront -= 1
#     
#     print TotalUniqueParetoFront
    
#     print "3"
    
    runningtime = 0.0
#     print totalTime.qsize()
    while totalTime.qsize() > 0:
        ttime = totalTime.get()
        if (float(ttime) < runningtime):
            runningtime = float(ttime)
    
#     print str(runningtime)
    endtime = time.time()
    outputFileParent = open(str(outputFileParentName+'.csv'), 'a')
    try:
        # keep a zero position for the same merging program as opGIA
        # in fact, here zero should be 356, as we already check it using the above code
        outputFileParent.writelines(str(num_consumers) + ',' + str(TotalOverlappingParetoFront) +',' + '0' + ',' + str(endtime - starttime) + '\n')
    finally:
        outputFileParent.close()
            
#     print "Parallel Done"
    
    
