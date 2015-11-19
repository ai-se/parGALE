'''
Created on Jan 17, 2014

@author: ezulkosk
'''
from string import split
from z3 import Tactic, IntNumRef, BoolRef, is_not, BoolSortRef, Not, simplify
import Z3ModelERSNoObjectives as ERS
import Z3ModelEShopNoObjectives as SHP
import Z3ModelWPTNoObjectives as WPT
import os
import sys
import z3


class DimacsConverter():
    
    def __init__(self):
        self.vars = {}
        self.varcount = 1
        
    
    
    
    def toDimacs(self, clause, neg=False):
        variables = []
        #print(clause)
        if z3.is_const(clause):
            if not isinstance(clause, IntNumRef):
                variables.append(self.getVarIndex(str(clause)))
            else:
                sys.exit("shouldn't get here")
        for c in clause.children():
            if is_not(c):
                print("AAAA");
                
            variables = variables + self.toDimacs(c)
        return variables
    
    
    def getVarIndex(self, variable):
            if self.vars.get(variable):
                return self.vars[variable]
            else:
                self.vars[variable] = self.varcount
                self.varcount = self.varcount + 1
                return self.vars[variable]
    
def convertToDimacs(goal, file):
        #f_n = open(Options.DIMACS_FILE, 'w')
        d = DimacsConverter()
        t = Tactic("tseitin-cnf")
        cnf = t(goal)
        #print cnf
        clauses = []
        #print(cnf)
        for i in cnf:
            for j in i:
                variables = []
                #print (j)
                #print j.__class__
                if len(j.children()) == 0:
                    variables.append(str(d.getVarIndex(str(j))))
                for k in j.children():
                    #print k
                    if is_not(k):
                        neg="-"
                        newk = (simplify(Not(k)))
                    else:
                        neg=""
                        newk = k
                    variables.append(neg + str(d.getVarIndex(str(newk))))
                clauses.append(variables)
        
        inv_map = {v:k for k, v in d.vars.items()}
        #print(inv_map)
        f = open(file, 'r')
        for line in f:
            [var, val] = split(line)
            print("\"" + str(inv_map[int(var)])+"\",")
 

def getDimacsMap(goal): 
    d = DimacsConverter()
    t = Tactic("tseitin-cnf")
    cnf = t(goal)
    #print cnf
    clauses = []
    #print(cnf)
    for i in cnf:
        for j in i:
            variables = []
            #print (j)
            #print j.__class__
            if len(j.children()) == 0:
                variables.append(str(d.getVarIndex(str(j))))
            for k in j.children():
                #print k
                if is_not(k):
                    neg="-"
                    newk = (simplify(Not(k)))
                else:
                    neg=""
                    newk = k
                variables.append(neg + str(d.getVarIndex(str(newk))))
            clauses.append(variables)
    
    inv_map = {v:k for k, v in d.vars.items()}
    return inv_map
           
def convertToDimacsBestConfigs(goal, file, outfile):
        #f_n = open(Options.DIMACS_FILE, 'w')
        inv_map = getDimacsMap(goal)
        #print(inv_map)
        f = open(file, 'r')
        try:
            os.remove(outfile)
        except:
            pass
        out = open(outfile, 'w')
        for line in f:
            myvars = split(line, ",")
            myvars = [int(var.strip()) for var in myvars]
            #print vars
            mystr = []
            for var in myvars:
                if var < 0:
                    mystr.append("Not$" + inv_map[abs(int(var))])
                else:
                    mystr.append(inv_map[int(var)])
            out.write(",".join(mystr)+"\n")
        out.close()     
        
if __name__ == '__main__':
    experiment = sys.argv[1]
    INFILE = sys.argv[2]
    OUTFILE= sys.argv[3]
    if experiment == "SHP":
        INPUT = SHP
    elif experiment == "WPT":
        INPUT = WPT
    elif experiment == "ERS":
        INPUT = ERS
    convertToDimacsBestConfigs(INPUT.s, INFILE, OUTFILE)
    #print(INPUT.s)
    #
    
    