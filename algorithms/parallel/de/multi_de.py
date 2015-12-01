from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from utils.lib import *
from algorithms.serial.algorithm import Algorithm
from utils.exceptions import RuntimeException


def default_settings():
  """
  Default Settings for DE
  :return: default settings
  """
  return O(
    gens = 100,
    candidates = 160,
    f = 0.75,
    cr = 0.3,
    seed = 1
  )

class DE(Algorithm):
  """
  Differential Evolution
  Storn 97
  """
  def __init__(self, problem, **settings):
    """
    Initialize DE for Algorithm
    """
    Algorithm.__init__(self, DE.__name__, problem)
    self.settings = default_settings().update(**settings)

  def dominates(self, obj1, obj2):
    """
    Static method to check if one objective
    dominate the other.
    :param obj1: List of points A
    :param obj2: List of points B
    """
    at_least = False
    for i,(a, b) in enumerate(zip(obj1, obj2)):
      if self.problem.objectives[i].better(a,b):
        at_least = True
      elif a == b:
        continue
      else:
        return False
    return at_least

  @staticmethod
  def three_others(one, pop):
    """
    Return three other points from population
    :param one: Point not to consider
    :param pop: Population to look in
    :return: two, three, four
    """
    def one_other():
      while True:
        x = choice(pop)
        if not id(x) in seen:
          seen.append(id(x))
          return x
    seen = [id(one)]
    two = one_other()
    three = one_other()
    four = one_other()
    return two, three, four

  def mutate(self, one, pop):
    """
    Function to mutate point using
    DE mutation strategy and return it
    :param one: Point to be mutated
    :param pop: Population to mutate from
    :return: Mutated point
    """
    two, three, four = DE.three_others(one, pop)
    r = choice(range(len(one.decisions)))
    mutated_decs = one.decisions[:]
    for i in range(len(one.decisions)):
      if (rand() < self.settings.cr) or (r == i):
        mutated_decs[i] = self.problem.decisions[i].limit(
          two.decisions[i] + self.settings.f * (three.decisions[i] - four.decisions[i]))
    return Point(mutated_decs)

  def generate(self, size):
    """
    Generate the population
    :return:
    """
    pop = self.problem.populate(size)
    return [Point(one) for one in pop]

  def run(self, init_pop=None):
    """
    Run DE
    :param init_pop:
    :return:
    """
    gen = 0
    max_gens = self.settings.max_gens
    population = init_pop
    total_evals = 0
    try:
      if population is None:
        population = self.generate(self.settings.pop_size)
      for one in population:
        one.evaluate(self.problem)
        total_evals+=1
      while gen < max_gens:
        say(".")
        clones = [one.clone() for one in population]
        for point in population:
          original_obj = point.evaluate(self.problem)
          mutant = self.mutate(point, population)
          if not self.problem.check_constraints(mutant):
            continue
          mutated_obj = mutant.evaluate(self.problem)
          total_evals += 1
          if self.dominates(mutated_obj, original_obj) and (not mutant in clones):
            clones.remove(point)
            clones.append(mutant)
        population = clones
        gen += 1
    except RuntimeException as e:
      e.print_trace()
      return population, total_evals
    return population, total_evals

