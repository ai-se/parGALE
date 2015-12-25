from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from feature_model import FeatureModel
from problems.problem import Problem, Objective

__author__ = 'panzer'

class WebPortal(FeatureModel):
  def __init__(self):
    FeatureModel.__init__(self, "problems/spl/references/web_portal.xml", "web_portal")
    self.objectives = [Objective("costs", to_minimize=True, low=0, high=273),
                       Objective("defects", to_minimize=True, low=0, high=106),
                       Objective("features", to_minimize=False, low=0, high=28)]
    self.costs = [6.2, 10.4, 8.1, 11.0, 8.9, 6.5, 11.4,
                  13.4, 5.5, 6.1, 10.3, 5.9, 13.7, 13.0,
                  10.0, 11.1, 8.6, 10.6, 13.0, 12.1, 14.1,
                  6.7, 9.6, 5.2, 12.2, 11.7, 9.1, 8.3]
    self.defects = [8, 5, 5, 4, 4, 4, 0,
                    4, 5, 5, 5, 0, 6, 6,
                    0, 3, 0, 3, 6, 5, 0,
                    5, 3, 4, 4, 0, 6, 6]

  def evaluate(self, decisions):
    total_costs, total_defects, total_features = 0, 0, 0
    for i, d in enumerate(decisions):
      if d == 1:
        total_costs += self.costs[i]
        total_defects += self.defects[i]
        total_features += 1
    return [total_costs, total_defects, total_features]
