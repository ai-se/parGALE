from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from z3 import *
from utils.lib import *
from problems.problem import Problem, Decision, Objective
from math import tan
from utils.exceptions import RuntimeException
from sklearn.tree import DecisionTreeRegressor as cart
import numpy as np

__author__ = 'panzer'

def compare(one, two, minimize=True):
  if one == two:
    return 0
  if minimize:
    status = 1 if one < two else -1
  else:
    status = 1 if one > two else -1
  return status

def clone(solver):
  cloned = Solver()
  [cloned.add(assertion) for assertion in solver.assertions()]
  return cloned

class FeatureModel(Problem):
  def __init__(self, decision_vector, objective_vector, solver, highs, lows, directions=None, is_empty=False, **settings):
    Problem.__init__(self)
    if is_empty:
      return
    if not directions:
      directions = [True]*len(objective_vector)
    self.decisions = [Decision(dec.decl().name(), is_true(False), is_true(True)) for dec in decision_vector]
    self.objectives = [Objective(obj.decl().name(), directions[i], lows[i], highs[i]) for i, obj in enumerate(objective_vector)]
    self.decision_vector = decision_vector
    self.objective_vector = objective_vector
    self.solver = solver
    self.base_solver = clone(solver)
    self.generation_counter = 0

  def clone(self, other):
    other.decisions = self.decisions[:]
    other.objectives = self.objectives[:]
    other.decision_vector = self.decision_vector
    other.objective_vector = self.objective_vector
    other.solver = clone(self.solver)
    other.base_solver = clone(self.base_solver)
    other.generation_counter = self.generation_counter
    return other

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
    # Randomly Set a decision
    rand_dec = choice(self.decision_vector)
    val = choice([True, False])
    self.solver.push()
    self.solver.add(rand_dec == val)
    if self.solver.check() == sat:
      #self.solver.set('random_seed', random.randint(0, 500))
      model = self.solver.model()
      decs = [model[dec] for dec in self.decision_vector]
      self.solver.pop()
      self.add_to_population_constraint(decs)
      self.generation_counter = 0
      return [is_true(d) for d in decs]
    else:
      self.generation_counter += 1
      self.solver.pop()
      if self.generation_counter >= 10:
        raise RuntimeException("Unsatisfiability reached")
      return self.generate()

  def check_constraints(self, decisions):
    cloned = clone(self.base_solver)
    assumptions = [decision == val for decision, val in zip(self.decision_vector, decisions)]
    [cloned.add(a) for a in assumptions]
    return cloned.check() == sat

  def evaluate_constraints(self, decisions):
    return True, 0

  def better(self, one, two):
    """
    Function that checks which of the
    two decisions are dominant
    :param one:
    :param two:
    :return:
    """
    obj1 = one.objectives
    obj2 = two.objectives
    one_at_least_once = False
    two_at_least_once = False
    for index, (a, b) in enumerate(zip(obj1, obj2)):
      status = compare(a, b, self.objectives[index].to_minimize)
      if status == -1:
        #obj2[i] better than obj1[i]
        two_at_least_once = True
      elif status == 1:
        #obj1[i] better than obj2[i]
        one_at_least_once = True
      if one_at_least_once and two_at_least_once:
        #neither dominates each other
        return 0
    if one_at_least_once:
      return 1
    elif two_at_least_once:
      return 2
    else:
      return 0

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

  @staticmethod
  def region_constraints(index, total):
    """
    Method to create additional constraints
    for each processor
    :param index: Index of processor run on
    :param total: Total number of processors
    :return:
    """
    assert False

  @staticmethod
  def get_gradient(radian):
    return int(1000 * round(tan(radian), 3))

  def split_features(self, consumers, obj_index=0):
    pop = self.populate(25*consumers)
    X, y = [],[]
    for one in pop:
      X.append(one)
      y.append(self.evaluate(one)[obj_index])
    tree = cart(max_leaf_nodes=consumers)
    tree.fit(X, y)
    filtered = np.asarray(X).astype(np.float32)
    leaf_ids = tree.tree_.apply(filtered)
    leaves = {}
    for leaf_id,x in zip(leaf_ids, X):
      leaves[leaf_id] = leaves.get(leaf_id, []) + [x]
    consumer_constraints = []
    for values in leaves.values():
      matrix = np.matrix(values)
      maxs = matrix.max(0).tolist()
      mins = matrix.min(0).tolist()
      constraints = []
      for dec_vector, max_val, min_val in zip(self.decision_vector, maxs[0], mins[0]):
        if not max_val:
          constraints.append(dec_vector == False)
        elif min_val:
          constraints.append(dec_vector == True)
      consumer_constraints.append(And(constraints))
    return consumer_constraints

  def convert_to_points(self, lst):
    assert False

