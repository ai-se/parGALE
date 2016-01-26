from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))

__author__ = 'panzer'

def eucledian(one, two):
  """
  Compute Eucledian Distance between
  2 vectors. We assume the input vectors
  are normalized.
  :param one: Vector 1
  :param two: Vector 2
  :return:
  """
  dist = 0
  for o_i, t_i in zip(one, two):
    dist += (o_i - t_i)**2
  return dist**0.5

def igd(obtained, ideals):
  """
  Compute the IGD for a
  set of solutions
  :param obtained: Obtained pareto front
  :param ideals: Ideal pareto front
  :return:
  """
  igd_val = 0
  for d in ideals:
    min_dist = sys.maxint
    for o in obtained:
      min_dist = min(min_dist, eucledian(o, d))
    igd_val += min_dist
  return igd_val/len(ideals)

