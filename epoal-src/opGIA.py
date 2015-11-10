#from Z3ModelEmergencyResponseOriginal import *
from consts import METRICS_MAXIMIZE, METRICS_MINIMIZE
from npGIAforZ3 import GuidedImprovementAlgorithm, \
    GuidedImprovementAlgorithmOptions
from npGIAforZ3 import setRecordPoint
from z3 import *
import Z3ModelEShopOriginal as SHP
import Z3ModelEmergencyResponseOriginal as ERS
import Z3ModelWebPortalUpdate as WPT
import argparse
import multiprocessing
import os
import sys
import time

#from Z3ModelWebPortal import *
'''
INPUT: experiment outfile num_consumers
'''


class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue, CurrentNotDomConstraints_queuelist, index, outputFileParentName, INPUT):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.CurrentNotDomConstraints_queuelist = CurrentNotDomConstraints_queuelist
        self.index = index
        self.outputFileParentName = outputFileParentName
        
        self.GIAOptions = GuidedImprovementAlgorithmOptions(verbosity=0, \
                        incrementallyWriteLog=False, \
                        writeTotalTimeFilename="timefile.csv", \
                        writeRandomSeedsFilename="randomseed.csv", useCallLogs=False)    

        self.GIAAlgorithm = GuidedImprovementAlgorithm(INPUT.s, INPUT.metrics_variables, \
                    INPUT.metrics_objective_direction, INPUT.FeatureVariable, options=self.GIAOptions)
        
        self.count_sat_calls = 0
        self.count_unsat_calls = 0
        self.count_paretoPoints = 0
        self.startTime = time.time()

    def run(self):
        while True:
            if self.task_queue.empty() == True:
                #print self.result_queue.qsize()
                #print '%s : Exiting' % multiprocessing.current_process().pid
                #self.task_queue.task_done()
                #print multiprocessing.current_process().is_alive()
                #os.exit(0)
                #print multiprocessing.current_process().is_alive()
                break
            else:
                next_task = self.task_queue.get(False)
                if next_task is None:
                    # Poison pill means shutdown
                    #print self.result_queue.qsize()
                    #print '%s : Exiting' % multiprocessing.current_process().pid
    #                 while self.result_queue.empty() != True:
    #                     print self.result_queue.get()
                    #multiprocessing.current_process().terminate()
                    self.task_queue.task_done()
                    #print count_paretoPoints, count_sat_calls, count_sat_calls
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
                    #print multiprocessing.current_process().is_alive()
                    #os.exit(0)
                    #print multiprocessing.current_process().is_alive()
    #                 multiprocessing.current_process().terminate()
    #                 print multiprocessing.current_process().is_alive()
                    break
                # execute a task, i.e., find a Pareto point
                # 1) update CurrentNotDomConstraints
                while self.CurrentNotDomConstraints_queuelist[self.index].empty() != True:
                    strconstraintlist = self.CurrentNotDomConstraints_queuelist[self.index].get()
                    ConvertedZ3ConstraintList  = list()
                    for constraint in strconstraintlist:
                        #print constraint
                        # eval() may lose precision, for example, eval(9962778141/19531250000) = 0
                        # that's why we need repr(), but not work for z3
                        # split constraint via > or <
                        constraintSplitList = []
                        if constraint.find('>') != -1:
                            constraintSplitList = constraint.split('>')                    
                            #print constraintSplitList
                            if constraintSplitList[1].find('/') != -1:
                                ConvertedZ3ConstraintList.append( Real(constraintSplitList[0].strip()) > RealVal(constraintSplitList[1].strip()))
                            else:
                                ConvertedZ3ConstraintList.append( Int(constraintSplitList[0].strip()) > IntVal(constraintSplitList[1].strip()))
                            #print ConvertedZ3ConstraintList
                        else:
                            constraintSplitList = constraint.split('<') 
                            #print constraintSplitList
                            if constraintSplitList[1].find('/') != -1:
                                ConvertedZ3ConstraintList.append( Real(constraintSplitList[0].strip()) < RealVal(constraintSplitList[1].strip()))
                            else:
                                ConvertedZ3ConstraintList.append( Int(constraintSplitList[0].strip()) < IntVal(constraintSplitList[1].strip()))
                            #print ConvertedZ3ConstraintList                   
                    #print Or(ConvertedZ3ConstraintList)
                    tmpNotDominatedByNextParetoPoint = Or(ConvertedZ3ConstraintList)
                    #print tmpNotDominatedByNextParetoPoint            
                    self.GIAAlgorithm.s.add(tmpNotDominatedByNextParetoPoint)
                
                # 2) if find all Pareto points, add a poison pill; otherwise find a Pareto point
                if self.GIAAlgorithm.s.check() != sat:
                    self.count_unsat_calls += 1
                    self.task_queue.put(None)
                else:
                    self.count_sat_calls += 1
                    self.task_queue.put("Task")      
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
                    
                    constraintlist = self.GIAAlgorithm.EtractConstraintListNotDominatedByX(NextParetoPoint)
                    strconstraintlist = list(str(item) for item in constraintlist)
                    for j in xrange(len(self.CurrentNotDomConstraints_queuelist)):
                        if j != self.index:
                            self.CurrentNotDomConstraints_queuelist[j].put(strconstraintlist)
                    self.task_queue.task_done()
        return 0

# def NonParallelAlgo():
#     # Non-Parallel    
#     GIAOptionsNP = GuidedImprovementAlgorithmOptions(verbosity=0, \
#         incrementallyWriteLog=False, \
#         writeTotalTimeFilename="timefile.csv", \
#         writeRandomSeedsFilename="randomseed.csv", useCallLogs=False)    
#       
#     GIAAlgorithmNP = GuidedImprovementAlgorithm(s, metrics_variables, \
#             metrics_objective_direction, FeatureVariable, options=GIAOptionsNP)
#     
#     start1 = time.time()
#     GIAAlgorithmNP.ExecuteGuidedImprovementAlgorithm()
#     runningtime = time.time() - start1
#       
#     outputFile = open('EmergencyResponseParallelResults.txt', 'a')
#     try:
#         outputFile.writelines('Non-Parallel running time is ' + str(runningtime) + '\n')
#         outputFile.writelines('\n')
#     finally:
#         outputFile.close()    
# 
# def ParallelAlgo():
#     total_consumers = multiprocessing.cpu_count()
#     
#     for num_consumers in range(2, total_consumers+1):
# #     for num_consumers in range(2, 4):
#         
#         # Establish communication queues
#         mgr = multiprocessing.Manager()
#         taskQueue = mgr.Queue()
#         ParetoFront = mgr.Queue()
#         CurrentNotDomConstraintsQueueList = []
#         for i in xrange(num_consumers):
#             # print i
#             CurrentNotDomConstraintsQueueList.append(mgr.Queue())
#         
#         # Enqueue initial tasks
#         for i in xrange(num_consumers):
#             taskQueue.put("Task")
#             
#         # Start consumers
#         # print 'Creating %d consumers' % num_consumers
#         consumersList = [ Consumer(taskQueue, ParetoFront, CurrentNotDomConstraintsQueueList, i)
#                         for i in xrange(num_consumers)]
#         
#         start2 = time.time()
# 
#         for w in consumersList:
#             w.start()            
#         
#     #     for i in xrange(num_consumers):
#     #         taskQueue.put(None)
#         
#     #    Wait for all of the tasks to finish
#     #    if taskQueue.empty() != True:
#     #    taskQueue.join()
#         for w in consumersList:
#             w.join()  
#         
#         runningtime = time.time() - start2
#         
# #         print "The number of all found Pareto Points (may overlapping) ", ParetoFront.qsize()
#         TotalOverlappingParetoFront = ParetoFront.qsize()
#         
#         tmpDict=[]
#         while ParetoFront.qsize() > 0:
#             point = ParetoFront.get()
#             if point in tmpDict:
#                 pass
#             else:
#                 tmpDict.append(point)
# 
#         TotalUniqueParetoFront = len(tmpDict)
#         
#         outputFile = open('EmergencyResponseParallelResults.txt', 'a')
#         try:
#             outputFile.writelines('The number of sub-processes is ' + str(num_consumers) + '\n')
#             outputFile.writelines('The number of all overlapping Pareto points is ' + str(TotalOverlappingParetoFront) + '\n')
#             outputFile.writelines('The number of all unique Pareto points is ' + str(TotalUniqueParetoFront) + '\n')
#             outputFile.writelines('Parallel running time is ' + str(runningtime) + '\n')
#             outputFile.writelines('\n')
#         finally:
#             outputFile.close()
                
if __name__ == '__main__':

    # create log file
#     outputFile = open('/home/gjm/ERParallelResults.txt', 'a')
#     outputFile.close()
        
#    Parallel with different number of consumbers
#    total_consumers = sys.argv[1]
    experiment = sys.argv[1]
    if experiment == "SHP":
        INPUT = SHP
        setRecordPoint(True)
    elif experiment == "WPT":
        INPUT = WPT
    elif experiment == "ERS":
        INPUT = ERS

    num_consumers = int(str(sys.argv[3]).strip())
    outputFileParentName = str(sys.argv[2]).strip()
    
#     for num_consumers in range(2, total_consumers+1):
#     for num_consumers in range(2, 4):
        
    # Establish communication queues
    mgr = multiprocessing.Manager()
    taskQueue = mgr.Queue()
    ParetoFront = mgr.Queue()
    CurrentNotDomConstraintsQueueList = []
    for i in xrange(num_consumers):
        #print i
        CurrentNotDomConstraintsQueueList.append(mgr.Queue())
    
    # Enqueue initial tasks
    for i in xrange(num_consumers):
        taskQueue.put("Task")
        
    # Start consumers
    #print 'Creating %d consumers' % num_consumers
    consumersList = [ Consumer(taskQueue, ParetoFront, CurrentNotDomConstraintsQueueList, i, outputFileParentName, INPUT)
                    for i in xrange(num_consumers)]
    
    start2 = time.time()

    for w in consumersList:
        w.start()            
    
#     for i in xrange(num_consumers):
#         taskQueue.put(None)
    
#    Wait for all of the tasks to finish
#    if taskQueue.empty() != True:
#    taskQueue.join()
    for w in consumersList:
        w.join()  
    
    runningtime = time.time() - start2
    
#         print "The number of all found Pareto Points (may overlapping) ", ParetoFront.qsize()
    TotalOverlappingParetoFront = ParetoFront.qsize()
    
    tmpDict=[]
    while ParetoFront.qsize() > 0:
        point = ParetoFront.get()
        if point in tmpDict:
            pass
        else:
            tmpDict.append(point)

    TotalUniqueParetoFront = len(tmpDict)
    
    outputFileParent = open(str(outputFileParentName+'.csv'), 'a')
    try:
        outputFileParent.writelines(str(num_consumers) + ',' + str(TotalOverlappingParetoFront) +',' + str(TotalUniqueParetoFront) + ',' + str(runningtime) + ',' + '\n')
    finally:
        outputFileParent.close()
            
#     print "Parallel Done"
    
    
