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
sys.path.append(os.path.abspath("."))
import time, datetime
import math
from problems.feature_models.emergency_response import EmergencyResponse
from problems.feature_models.webportal import WebPortal
from utils.nsga2 import select as sel_nsga2
from algorithms.parallel.multi import Consumer as Cons
from utils.lib import mkdir, write_objs

#from Z3ModelEmergencyResponseUpdateAllMin import *
#from Z3ModelWebPortal import *

'''
INPUT: experiment outfile num_consumers
'''

WRITE_LOCALLY = False

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
                    if WRITE_LOCALLY:
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

def _single_test(repeat=0):
    experiment = sys.argv[1]
    problem = None
    if experiment == "SHP":
        INPUT = SHP_Min
        setRecordPoint(True)
        return
    elif experiment == "WPT":
        INPUT = WPT_Min
        problem = WebPortal()
    elif experiment == "ERS":
        INPUT = ERS_Min
        problem = EmergencyResponse()
    else:
      return

    num_consumers = int(str(sys.argv[3]).strip())
    solvers = replicateSolver(INPUT.s, num_consumers)
    outputFileParentName = str(sys.argv[2]).strip()

    # Establish communication queues
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
    consumersList = [ Consumer(taskQueue, ParetoFront, totalTime, i, outputFileParentName, num_consumers, solvers[i], INPUT)
                    for i in xrange(num_consumers)]
    starttime = time.time()
    for w in consumersList:
        w.start()

    for w in consumersList:
        w.join()

    runningtime = 0.0
    while totalTime.qsize() > 0:
        ttime = totalTime.get()
        if (float(ttime) < runningtime):
            runningtime = float(ttime)

    endtime = time.time()

    TotalOverlappingParetoFront = ParetoFront.qsize()
    pf = []
    while not ParetoFront.empty():
        pf.append(ParetoFront.get())
    pf = problem.convert_to_points(pf)
    pf = sel_nsga2(problem, pf, Cons.default_settings().GALE_pop_size)
    new_dir = mkdir("results/"+str(datetime.date.today())+"/")
    outputFileParent = open(new_dir+str(outputFileParentName+'.csv'), 'a')
    try:
        # keep a zero position for the same merging program as opGIA
        # in fact, here zero should be 356, as we already check it using the above code
        outputFileParent.writelines(str(num_consumers) + ',' + str(TotalOverlappingParetoFront) +',' + '0' + ',' + str(endtime - starttime) + '\n')
    finally:
        outputFileParent.close()
    obj_file = mkdir(new_dir+"/repeat_"+str(repeat)+"/") + str(outputFileParentName)+"_"+str(num_consumers)+"_objs"
    write_objs([one.objectives for one in pf], obj_file)

REPEATS = 5
def _multi_test():
  for i in xrange(REPEATS):
    _single_test(i)

if __name__ == '__main__':
    _multi_test()
    
    
