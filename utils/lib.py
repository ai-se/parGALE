"""
Standard library files and operators
"""
from __future__ import print_function, division
import random
import sys, os
sys.path.append(os.path.abspath("."))
import math
import numpy as np

# Constants
EPS = 0.00001
PI = math.pi



class O:
  """
  Default class which everything extends.
  """
  def __init__(self,**d): self.has().update(**d)
  def has(self): return self.__dict__
  def update(self,**d) : self.has().update(d); return self
  def __repr__(self)   :
    show=[':%s %s' % (k,self.has()[k])
          for k in sorted(self.has().keys() )
          if k[0] is not "_"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show=map(lambda x: '\t'+x+'\n',show)
    return '{'+' '.join(show)+'}'
  def __getitem__(self, item):
    return self.has().get(item)

def norm(x, low, high):
  """
  Normalize Value
  :param x: Value to be normalized
  :param low: Minimum value
  :param high: Maximum value
  :return: Normalized value
  """
  nor = (x - low)/(high - low + EPS)
  if nor > 1:
    return 1
  elif nor < 0:
    return 0
  return nor


def de_norm(x, low, high):
  """
  De-normalize value
  :param x: Value to be denormalized
  :param low: Minimum value
  :param high: Maximum value
  :return:
  """
  de_nor = x*(high-low) + low
  if de_nor > high:
    return high
  elif de_nor < low:
    return low
  return de_nor

def uniform(low, high):
  """
  Uniform value between low and high
  :param low: minimum of distribution
  :param high: maximum of distribution
  :return: Uniform value in the uniform distribution
  """
  return random.uniform(low, high)

def seed(val=None):
  random.seed(val)

def say(*lst):
  """
  Print value on the same line
  :param lst:
  :return:
  """
  print(*lst, end="")
  sys.stdout.flush()

def choice(lst):
  """
  Return random value from list
  :param lst: list to search in
  :return:
  """
  return random.choice(lst)

def rand():
  """
  Returns a random number.
  """
  return random.random()

def more(x,y):
  """
  Check if x > y
  :param x: Left Comparative Value
  :param y: Right Comparative Value
  :return: Boolean
  """
  return x > y

def less(x,y):
  """
  Check if x < y
  :param x: Left Comparative Value
  :param y: Right Comparative Value
  :return: Boolean
  """
  return x < y

def avg(lst):
  """
  Average of list
  :param lst:
  :return:
  """
  return sum(lst)/float(len(lst))

def cos(val):
  """
  Return cosine of a value
  :param val: Value in radians
  :return:
  """
  return math.cos(val)

def sin(val):
  """
  Return sine of a value
  :param val: Value in radians
  :return:
  """
  return math.sin(val)

def clone(lst):
  if lst is None:
    return None
  return lst[:]

class Point(O):

  def __init__(self, decisions, problem=None):
    """
    Represents a point in the frontier for NSGA
    :param decisions: Set of decisions
    :param problem: Instance of the problem
    """
    O.__init__(self)
    self.decisions = clone(decisions)
    if problem:
      self.objectives = problem.evaluate(decisions)
    else:
      self.objectives = []
    self.rank = 0
    self.dominated = []
    self.dominating = 0
    self.crowd_dist = 0

  def __hash__(self):
    return hash(self.decisions)

  def __eq__(self, other):
    return cmp(self.decisions, other.decisions) == 0

  def clone(self):
    """
    Method to clone a point
    :return:
    """
    new = Point(self.decisions)
    new.objectives = self.objectives
    return new

  def evaluate(self, problem):
    """
    Evaluate a point
    :param problem: Problem used to evaluate
    """
    if not self.objectives:
      self.objectives = problem.evaluate(self.decisions)
    return self.objectives


def report(lst, name):
  print("*** ", str.upper(name), " ***")
  s_lst = sorted(lst)
  low = s_lst[0]
  high = s_lst[-1]
  med = s_lst[len(lst)//2] if len(lst) % 2 else (s_lst[len(lst)//2] + s_lst[len(lst)//2 - 1])/2
  print("LOW  : ", low)
  print("HIGH : ", high)
  print("MED  : ", med)

def mkdir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
  return directory

def mean_iqr(lst):
  """
  return mean and iqr of a list.
  :param lst: List to fetch mean and iqr
  :return: (mean, iqr)
  """
  mean = np.mean(lst)
  q75, q25 = np.percentile(lst, [75, 25])
  return mean, q75 - q25

def write_objs(objs, file_name):
  with open(file_name+'.csv', 'w') as f:
    f.writelines(",".join(str(j) for j in i) + '\n' for i in objs)
