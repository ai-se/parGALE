from __future__ import print_function, division
import sys, os, time
sys.path.append(os.path.abspath("."))
import multiprocessing
from utils.lib import O


__author__ = 'panzer'



class Consumer(multiprocessing.Process):
  def __init__(self, optimizer, results, index, outfile, total_consumers, initial_pop = None, **settings):
    multiprocessing.Process.__init__(self)
    self.settings = Consumer.default_settings().update(**settings)
    self.results = results
    self.index = index
    self.outfile = outfile
    self.optimizer = optimizer
    self.initial_pop = initial_pop
    if index == total_consumers - 1:
      self.optimizer.settings.max_gens = self.settings.max_gens / total_consumers
    else:
      self.optimizer.settings.max_gens = self.settings.max_gens - (total_consumers - 1) * self.settings.max_gens / total_consumers
    self.start_time =  time.time()
    self.total_time = 0

  @staticmethod
  def default_settings():
    return O(
      seed = 0,
      max_gens = 160
    )

  def run(self):
    best_solutions, evals = self.optimizer.run(self.initial_pop)
    self.results[self.index] = best_solutions
    self.total_time = time.time() - self.start_time
    child_outfile = open(str("results/"+str(self.outfile)+'C'+str(self.index)+'.csv'), 'a')
    front_size = sum([len(solns) for solns in best_solutions])
    try:
      child_outfile.writelines(
        str(self.index) + ',' +
        str(front_size) + ',' +
        str(self.total_time) + '\n')
    finally:
      child_outfile.close()
    return 0
