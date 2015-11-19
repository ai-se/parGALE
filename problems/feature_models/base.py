from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from z3 import *
from utils.lib import *
from problems.problem import Problem, Decision, Objective

__author__ = 'panzer'

def clone(solver):
  cloned = Solver()
  [cloned.add(assertion) for assertion in solver.assertions()]
  return cloned

class FeatureModel(Problem):
  def __init__(self, decision_vector, objective_vector, solver, highs, lows, directions=None, **settings):
    Problem.__init__(self)
    if not directions:
      directions = [True]*len(objective_vector)
    self.decisions = [Decision(dec.decl().name(), is_true(False), is_true(True)) for dec in decision_vector]
    self.objectives = [Objective(obj.decl().name(), directions[i], lows[i], highs[i]) for i, obj in enumerate(objective_vector)]
    self.decision_vector = decision_vector
    self.objective_vector = objective_vector
    self.solver = solver
    self.base_solver = clone(solver)

  def dist(self, one, two, one_norm = True, two_norm = True, is_obj = True):
    if is_obj:
      return Problem.dist(self, one, two, one_norm, two_norm, is_obj)
    else:
      # Using Hamming Distance
      # https://en.wikipedia.org/wiki/Hamming_distance
      return sum(a!=b for a,b in zip(one, two))

  def manhattan_dist(self, one, two, one_norm = True, two_norm = True, is_obj = True):
    if is_obj:
      return Problem.manhattan_dist(self, one, two, one_norm, two_norm, is_obj)
    else:
      # Using Hamming Distance
      # https://en.wikipedia.org/wiki/Hamming_distance
      return sum(a!=b for a,b in zip(one, two))

  def generate(self, generator=uniform):

    if self.solver.check() == sat:
      self.solver.set('random_seed', 400)
      model = self.solver.model()
      decs = [model[dec] for dec in self.decision_vector]
      self.add_to_population_constraint(decs)
      return [is_true(d) for d in decs]
    else:
      assert False, "Unsatisfiability reached"

  def check_constraints(self, decisions):
    cloned = clone(self.base_solver)
    assumptions = [decision == val for decision, val in zip(self.decision_vector, decisions)]
    [cloned.add(a) for a in assumptions]
    return cloned.check() == sat

  def add_to_population_constraint(self, decisions):
    pop_constraint = []
    for decision, val in zip(self.decision_vector, decisions):
      pop_constraint.append(decision != val)
    self.solver.add(Or(pop_constraint))

  def evaluate(self, decisions):
    cloned = clone(self.base_solver)
    assumptions = [decision == val for decision, val in zip(self.decision_vector, decisions)]
    [cloned.add(a) for a in assumptions]
    if cloned.check() == unsat:
      assert False, "Invalid Decisions. How did this come here?"
    model = cloned.model()
    objs = [FeatureModel.format_objective(model[obj]) for obj in self.objective_vector]
    return objs

  @staticmethod
  def format_objective(val):
    if isinstance(val, RatNumRef):
      return val.numerator_as_long()/val.denominator_as_long()
    elif isinstance(val, IntNumRef):
      return val.as_long()
    elif isinstance(val, AlgebraicNumRef):
      return FeatureModel.format_objective(val.approx())
    else:
      assert False, "Invalid Objective Type"