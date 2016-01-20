from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
__author__ = 'panzer'

def loo(points):
  for i in range(len(points)):
    one = points[i]
    rest = points[:i] + points[i+1:]
    yield one, rest

def select(problem, population, k):
  fronts = sort_non_dominated(problem, population)
  pop_next = []
  for i, front in enumerate(fronts):
    if len(pop_next) + len(fronts[i]) >= k:
      fronts[i] = assign_crowd_dist(problem, front)
      pop_next += sorted(fronts[i], key=lambda x:x.crowd_dist, reverse=True)[:(k - len(pop_next))]
      break
    else:
      pop_next += fronts[i]
  return pop_next

def sort_non_dominated(problem, population):
  frontiers = []
  front1 = []
  i=1
  for one, rest in loo(population):
    i+=1
    for two in rest:
      domination_status = domination(problem, one, two)
      if domination_status == 1:
        one.dominated.append(two)
      elif domination_status == 2:
        one.dominating += 1
    if one.dominating == 0:
      one.rank = 1
      front1.append(one)
  current_rank = 1
  frontiers.append(front1)
  while True:
    front2 = []
    for one in front1:
      for two in one.dominated:
        two.dominating -= 1
        if two.dominating == 0:
          two.rank =  current_rank + 1
          front2.append(two)
    current_rank += 1
    if len(front2) == 0 :
      break
    else :
      frontiers.append(front2)
      front1 = front2
  return frontiers


def domination(problem, one, two):
    """
    Domination is defined as follows:
    for all objectives a in "one" and
    all objectives b in "two"
    every a <= b
    for all objectives a in "one" and
    all objectives b in "two"
    at least one a < b
    Check if one set of decisions ("one")
    dominates other set of decisions ("two")
    Returns:
      0 - one and two are not better each other
      1 - one better than two
      2 - two better than one
    """
    one_status, one_offset = problem.evaluate_constraints(one.decisions)
    two_status, two_offset = problem.evaluate_constraints(two.decisions)
    if one_status and two_status:
      # Return the better solution if both solutions satisfy the constraints
      return problem.better(one, two)
    elif one_status:
      # Return 1, if 1 satisfies the constraints
      return 1
    elif two_status:
      #Return 2, if 2 satisfies the constraints
      return 2
    # both fail the constraints
    elif one_offset <= two_offset:
      # one has a lesser offset deviation
      return 1
    else:
      # two has a lesser offset deviation
      return 2

def assign_crowd_dist(problem, frontier):
  """
  Crowding distance between each point in
  a frontier.
  """
  l = len(frontier)
  for m in range(len(problem.objectives)):
    frontier = sorted(frontier, key=lambda x:x.objectives[m])
    frontier[0].crowd_dist = float("inf")
    frontier[-1].crowd_dist = float("inf")
    for i in range(1,l-1):
      frontier[i].crowd_dist += (frontier[i+1].objectives[m] - frontier[i-1].objectives[m])
  return frontier


def _test():
  from problems.feature_models.webportal import WebPortal
  from problems.problem import Point
  problem = WebPortal()
  points = [Point(one, problem) for one in problem.populate(50)]
  print(len(points))
  selected = select(problem, points, 25)
  print(len(selected))

if __name__ == "__main__":
  _test()
