'''
Created on Jan 17, 2014

@author: ezulkosk
'''
from z3 import Tactic, IntNumRef, BoolRef, is_not, BoolSortRef, Not, simplify
import Z3ModelERSNoObjectives as ERS
import Z3ModelEShopNoObjectives as SHP
import Z3ModelWPTNoObjectives as WPT
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
    
def convertToDimacs(goal):
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
        print("p cnf " + str(d.varcount-1) + " " + str(len(clauses)))
        for clause in clauses:
                print(" ".join([str(i) for i in clause])  + " 0")
        
if __name__ == '__main__':
    experiment = sys.argv[1]
    if experiment == "SHP":
        INPUT = SHP
    elif experiment == "WPT":
        INPUT = WPT
    elif experiment == "ERS":
        INPUT = ERS
    #print(INPUT.s)
    convertToDimacs(INPUT.s)
    