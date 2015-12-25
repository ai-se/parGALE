import sys, os
sys.path.append(os.path.abspath("."))
from problems.problem import *
from feature_tree import FeatureTree
from mutate_engine import MutateEngine

__author__ = 'panzer'

class FeatureModel(Problem):
  def __init__(self, url, name):
    Problem.__init__(self)
    self.name = name
    self.url = url
    self.ft = FeatureTree.load_ft_url(url)
    self.mutate_engine = MutateEngine(self.ft)
    self.decisions = [Decision(leaf.id, 0, 1) for leaf in self.ft.leaves]

def main():
  fm = FeatureModel("problems/spl/references/web_portal.xml", "web_portal")
  print(fm.mutate_engine.genValidOne())

if __name__ == "__main__":
  main()