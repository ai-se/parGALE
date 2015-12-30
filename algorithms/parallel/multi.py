from __future__ import print_function, division
import sys, os, time
sys.path.append(os.path.abspath("."))
import multiprocessing
from utils.lib import O
from algorithms.parallel.gale.multi_gale import GALE
from algorithms.parallel.de.multi_de import DE

__author__ = 'panzer'



class Consumer(multiprocessing.Process):
  def __init__(self, optimizer, model, results, index, outfile, total_consumers, feature_splits = None, initial_pop = None, **settings):
    multiprocessing.Process.__init__(self)
    self.settings = Consumer.default_settings().update(**settings)
    self.results = results
    self.index = index
    self.outfile = outfile
    self.initial_pop = initial_pop
    cloned_model = model.clone()
    # if feature_splits:
    #   cloned_model.solver.add(feature_splits[index])
    #   cloned_model.base_solver.add(feature_splits[index])
    self.optimizer = optimizer(cloned_model)
    if optimizer == GALE:
      self.optimizer.settings.max_gens = self.settings.GALE_max_gens // total_consumers
      self.optimizer.settings.pop_size = self.settings.GALE_pop_size
    elif optimizer == DE:
      self.optimizer.settings.max_gens = self.settings.DE_max_gens
      self.optimizer.settings.pop_size = self.settings.DE_pop_size // total_consumers
    else:
      assert False, "Invalid optimizer "+optimizer
    self.start_time =  time.time()
    self.total_time = 0

  @staticmethod
  def default_settings():
    return O(
      seed = 0,
      GALE_max_gens = 160,
      GALE_pop_size = 50,
      DE_max_gens = 50,
      DE_pop_size = 160,
    )

  def run(self):
    best_solutions, evals = self.optimizer.run(self.initial_pop)
    self.results[self.index] = best_solutions
    self.total_time = time.time() - self.start_time
    child_outfile = open(str(str(self.outfile)+'C'+str(self.index)+'.csv'), 'a')
    front_size = len(best_solutions)
    try:
      child_outfile.writelines(
        str(self.index) + ',' +
        str(front_size) + ',' +
        str(self.total_time) + '\n')
    finally:
      child_outfile.close()
    return 0
