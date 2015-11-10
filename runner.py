from __future__ import print_function, division
import sys
from problems.dtlz.dtlz2 import DTLZ2
from algorithms.serial.gale.gale import GALE as GALE_S
from algorithms.parallel.gale.gale import GALE as GALE_P
from algorithms.parallel.de.de import DE as DE_P
from mpi4py import MPI
from time import clock, sleep
from utils.lib import O, report


COMM = MPI.COMM_WORLD
RANK = COMM.rank
SIZE = COMM.size

settings = O(
  runs = 20
)

def _run_parallel():
  model = DTLZ2(3)
  gale = GALE_P(model)
  times, convs, dives = [], [], []
  for i in range(settings.runs):
    print(i)
    start = clock()
    goods = GALE_P.run(gale, id = i)
    if RANK == 0:
      times.append(clock() - start)
      convs.append(gale.convergence(goods))
      dives.append(gale.diversity(goods))
  if RANK == 0:
    print("Time", times)
    report(times, "Time Taken")
    print("Convergence", convs)
    report(convs, "Convergence")
    print("Diversity", dives)
    report(dives, "Diversity")



def _run_serial():
  times, convs, dives = [], [], []
  for i in range(settings.runs):
    model = DTLZ2(3)
    algo = GALE_S(model)
    start = clock()
    print(i)
    goods = algo.run()
    times.append(clock() - start)
    convs.append(algo.convergence(goods))
    dives.append(algo.diversity(goods))
    algo.solution_range(goods)
  print("Time", times)
  report(times, "Time Taken")
  print("Convergence", convs)
  report(convs, "Convergence")
  print("Diversity", dives)
  report(dives, "Diversity")

def _run_once(optimizer):
  model = DTLZ2(3)
  opt = optimizer(model)
  start = clock()
  goods = optimizer.run(opt)
  delta = clock() - start
  if RANK == 0:
    print("\nTime taken ", delta)
    print(opt.convergence(goods))
    print(opt.diversity(goods))
    opt.solution_range(goods)

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
    print("Optimizer not mentioned")
    exit()
  if args[1] == "gale":
    _run_once(GALE_P)
  elif args[1] == "de":
    _run_once(DE_P)