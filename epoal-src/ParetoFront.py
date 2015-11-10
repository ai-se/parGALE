'''
Created on May 2, 2013

@author: rafaelolaechea
'''
import sys
import csv
from z3 import *

from consts import  METRICS_MAXIMIZE, METRICS_MINIMIZE, ObjectiveTypeEnum

def lookupObjectiveTypeString(typeName):    
    if typeName == 'Integer':
        typeParser = int
    elif typeName == 'IntegerFromFloat':
        typeParser = lambda x: int(float(x))
    elif typeName == 'Float' or typeName == 'Double':
        typeParser = float
    elif typeName == 'RealValForFloat':
        typeParser = RealVal
    return typeParser

def lookupObjectiveTypeToEnumString(typeName):
    if typeName == 'Integer':
        typeEnum = ObjectiveTypeEnum.INT
    elif typeName == 'IntegerFromFloat':
        typeEnum = ObjectiveTypeEnum.INTEGERFROMFLOAT
    elif typeName == 'Float' or typeName == 'Double':
        typeEnum = ObjectiveTypeEnum.FLOAT
    elif typeName == 'RealValForFloat':
        typeEnum = ObjectiveTypeEnum.REALVALFORFLOAT
    return typeEnum

class ParetoFront(object):
    def __init__(self, objectiveValuesFilename, objectiveNamesFilename):
        self.objectiveFilehandle = open(objectiveValuesFilename, "rb")
        self.objectiveNamesFilehandle = open(objectiveNamesFilename, "rb")
        
        self.parseRawObjectiveValues_(self.objectiveFilehandle)
        self.parseObjectiveNamesAndTypes_(self.objectiveNamesFilehandle)
        self.convertRawObjectiveValues_()
        
        self.objectiveFilehandle.close()    
        self.objectiveNamesFilehandle.close() 

    def parseRawObjectiveValues_(self, objectiveFilehandle):
        self.rawObjectiveValues = []
        for objectiveValueRow in csv.reader(objectiveFilehandle, delimiter=self.getObjectiveValueDelimiter()):            
            # Cleaning up trailing space
            if objectiveValueRow[-1] == '':
                objectiveValueRow = objectiveValueRow[:-1]
            # End Cleaning up trailing space    
                
            self.rawObjectiveValues.append(objectiveValueRow)

    def parseObjectiveNamesAndTypes_(self, objectiveNamesFilehandle):
        self.objectives = {}
        for objectiveNameOrTypeRow in csv.reader(objectiveNamesFilehandle, delimiter=','):
            if  objectiveNameOrTypeRow[0] == 'objectiveName':
                i = len(self.objectives.keys())
                objectiveName = objectiveNameOrTypeRow[1]
                self.objectives[objectiveName] = {}
                self.objectives[objectiveName]['position'] = i
            elif  objectiveNameOrTypeRow[0] == 'objectiveType':
                objectiveName = objectiveNameOrTypeRow[1]
                typeName = objectiveNameOrTypeRow[2]
                typeParserObject = lookupObjectiveTypeString(typeName)
                typeEnumObject = lookupObjectiveTypeToEnumString(typeName)
                self.objectives[objectiveName]['type'] = typeParserObject
                self.objectives[objectiveName]['typeEnum'] = typeEnumObject
            elif  objectiveNameOrTypeRow[0] == 'objectiveSense':
                objectiveName = objectiveNameOrTypeRow[1]
                objectiveSenseString = objectiveNameOrTypeRow[2]
                if objectiveSenseString == "Maximize":
                    objectiveSenseValue = METRICS_MAXIMIZE
                elif objectiveSenseString == "Minimize":
                    objectiveSenseValue =  METRICS_MINIMIZE
                else:
                    raise Exception("Undefined value for objective sense, when parsing row \"%s\" " % (objectiveNameOrTypeRow,) )
                self.objectives[objectiveName]['sense'] = objectiveSenseValue

            

    def convertRawObjectiveValues_(self):
        """
        We create objective values with their appropiate types (e.g float, integer)
        Requires: Raw objective values, objective names and types.
        """        
        self.objectivesValues = []
        
        for row in self.rawObjectiveValues :
            objectiveValuesRow =  {}
            for objectiveName in self.objectives.keys():
                rawValuePosition = self.objectives[objectiveName]['position']
                rawValue = row[rawValuePosition]
                objectiveValue = self.objectives[objectiveName]['type'](rawValue)
                objectiveValuesRow[objectiveName] = objectiveValue
            self.objectivesValues.append(objectiveValuesRow)

    def getParetoFront(self):
        return self.objectivesValues

    def getObjectivesNamesTypesAndPositions(self):
        return self.objectives
    
    def dumpAsObjectiveFileForJmetal(self, filename=''):
        """
        Paper XXX.
        """
        if filename != '':
            fp_out = open(filename, "w")
        else:
            fp_out = sys.stdout

        print self.objectives
        sorted_keys = sorted(self.objectives, key=lambda(x):self.objectives[x]['position'])
        print sorted_keys
        
        for row in self.objectivesValues:     
            row_with_converted_types_and_values = []   
            for objective_name in sorted_keys:
                if self.objectives[objective_name]['sense'] == METRICS_MAXIMIZE:
                    if self.objectives[objective_name]['type'] == RealVal:
                        row_with_converted_types_and_values.append(float(-row[objective_name].as_decimal(15)))
                    else:
                        row_with_converted_types_and_values.append(float(-row[objective_name]))                           
                elif self.objectives[objective_name]['sense'] == METRICS_MINIMIZE:
                    if self.objectives[objective_name]['type'] == RealVal:
                        row_with_converted_types_and_values.append(float(-row[objective_name].as_decimal(15)))
                    else:
                        row_with_converted_types_and_values.append(float(row[objective_name]))                           
                else:
                    raise Exception("Undefined objective sense encountered")

                                         
            fp_out.write( ' '.join([str(x) for x in row_with_converted_types_and_values]) + ' \n')

        if filename != '':
            fp_out.close()
        
class ApproximateParetoFront(ParetoFront):
    def getObjectiveValueDelimiter(self):
        return ' '
    def getParetoFrontProjectedToZeroViolations(self):
        """
        Gets a projection of the pareto front, with  ConstraintViolations == 0.
        The projection has ConstraintViolations removed as well. 
        """
        filteredObjectives = []
        for objectiveRow in  self.getParetoFront():
            if objectiveRow['ConstraintViolations'] == 0:
                filteredObjective = {}
                for objNames in [x for x in objectiveRow.keys() if x != 'ConstraintViolations']:
                    filteredObjective[objNames] = objectiveRow[objNames]
                filteredObjectives.append(filteredObjective)

        return filteredObjectives


class ExactParetoFrontFromJMetalLikeObjectives(ParetoFront):
    def getObjectiveValueDelimiter(self):
        return ','

def countApproxParetoFrontPointsInExactParetoFronts(approxFront, ExactFront, epsilon=0.00001):
    """
    Counts the number of pareto fronts points from the approximate front that are in the 
    exact Pareto Front. 
    """
    includedParetoPoints  = []
    for approxParetoPoint in approxFront.getParetoFrontProjectedToZeroViolations():
        isIncludedParetoPoint = False
        for exactParetoPoint in ExactFront.getParetoFront():
            areEqual = True
            for objectiveKey in ExactFront.getObjectivesNamesTypesAndPositions().keys():
                if ExactFront.getObjectivesNamesTypesAndPositions()[objectiveKey]['type'] == RealVal:                                 
                    areEqual = areEqual and abs(approxParetoPoint[objectiveKey] - float(exactParetoPoint['Cost'].as_decimal(15))  ) < epsilon
                else:
#                    print type(exactParetoPoint[objectiveKey])
#                    print exactParetoPoint[objectiveKey]
                    areEqual = areEqual and abs(exactParetoPoint[objectiveKey]) ==  abs(approxParetoPoint[objectiveKey])
            if areEqual == True:
                isIncludedParetoPoint = True
        if isIncludedParetoPoint == True:
            includedParetoPoints.append(approxParetoPoint)
    return includedParetoPoints
        
def computeSetOfParetoPointsTuplesFromListOfParetoPoints(ListOfParetoPointsAsDicts):
    """
    Given a list of pareto points encoded as a dictionary,  we compute a set of the same pareto points 
    (aka remove duplicates) encoded as tuples ordered by the order of the keys (returned by keys() method of first item) .
    """
    setOfParetoPointsTuples = set()
    if len(ListOfParetoPointsAsDicts) > 0 :
        keyset = ListOfParetoPointsAsDicts[0].keys()
        for row in ListOfParetoPointsAsDicts:
            ParetoPointQualityValues = tuple(row[QualityAttributeKey] for QualityAttributeKey in keyset)
            setOfParetoPointsTuples.add(ParetoPointQualityValues)
    return setOfParetoPointsTuples