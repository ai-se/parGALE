from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.feature_models import emergency_response, webportal
from problems.problem import Point
from utils.nsga2 import select as sel_nsga2
from measures.igd import igd
from measures.hypervolume import HyperVolume
from utils.lib import mean_iqr, mkdir
from matplotlib import pyplot as plt
import numpy as np
COLORS = ["blue", "green", "red", "cyan", "magenta", "yellow", "saddlebrown", "orange", "darkgreen"]

__author__ = 'panzer'

def igd_wrapper(model, model_name, repeat, processor):
  algo_objs = []
  for algo in ALGOS:
    algo_objs.append(read(model_name, algo, repeat, processor))
  reference = compute_reference(model, algo_objs)
  measures = []
  for objs in algo_objs:
    measures.append(igd(objs, reference))
  return measures

def hv_wrapper(model, model_name, repeat, processor):
  algo_objs = []
  for algo in ALGOS:
    algo_objs.append(read(model_name, algo, repeat, processor))
  all_objs = []
  for objs in algo_objs: all_objs += objs
  reference = HyperVolume.get_reference_point(model, all_objs)
  hv = HyperVolume(model, reference)
  measures = []
  for objs in algo_objs:
    measures.append(hv.compute(objs))
  return measures




FOLDER      = "results/2016-01-20"
MODEL       = "wpt"
ALGOS       = ["gale", "galefs", "gia"]
REPEATS     = 5
PROCESSORS  = 16
MEASURE     = hv_wrapper

def read(model_name, algo, repeat, processor):
  file_name = FOLDER + "/repeat_" + str(repeat) + "/" + model_name + "_" + algo + "_" + str(processor) + "_objs.csv"
  with open(file_name, 'r') as f:
    lines = f.readlines()
    objs = [map(float, line.strip().split(",")) for line in lines]
  return objs

def compare_processor(model, model_name, processor):
  repeats = []
  for repeat in range(REPEATS):
    repeats.append(MEASURE(model, model_name, repeat, processor))
  processor_stats = {}
  for i, algo in enumerate(ALGOS):
    algo_stats = {}
    vals = []
    for repeat in range(REPEATS):
      vals.append(repeats[repeat][i])
    mean, iqr = mean_iqr(vals)
    algo_stats["mean"] = mean
    algo_stats["iqr"] = iqr
    processor_stats[algo] = algo_stats
  return processor_stats

def evaluate_model(model_name):
  model = get_model(model_name)
  processors = {}
  for i in range(1, PROCESSORS+1):
    processors[i] = compare_processor(model, model_name, i)
  return processors

def report():
  def autolabel(rect_s):
      # attach some text labels
      for rect in rect_s:
          height = rect.get_height()
          ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                  '%0.2f' % height,
                  ha='center', va='bottom')
  processors_stats = evaluate_model(MODEL)
  width = 0.6
  size = len(ALGOS)+1
  ind = np.arange(start=0, step=size*width, stop=PROCESSORS*size*width, dtype=float)
  fig, ax = plt.subplots()
  rects = ()
  algos = ()
  for index, algo_name in enumerate(ALGOS):
    means = ()
    iqrs = ()
    for p_i in range(1, PROCESSORS+1):
      means += (processors_stats[p_i][algo_name]["mean"], )
      iqrs += (processors_stats[p_i][algo_name]["iqr"], )
    rect = ax.bar(ind + index*width, means, width, color=COLORS[index], yerr=iqrs, ecolor='black')
    rects += (rect, )
    algos += (algo_name, )
  measure = MEASURE.__name__.split("_")[0].upper()
  ax.set_ylabel(measure)
  ax.set_title(measure)
  ax.set_xticks(ind + len(ALGOS)*width/2)
  ax.set_xticklabels(tuple(range(1, PROCESSORS+1)))
  ax.legend(rects, algos)

  #for rect in rects:autolabel(rect)
  folder = mkdir(FOLDER+"/figures/")
  plt.savefig(folder+"%s_%s.png"%(MODEL, MEASURE.__name__.split("_")[0]))

def compute_reference(model, algo_objs):
  all_objs = []
  for objs in algo_objs: all_objs += objs
  k = int(len(all_objs)/len(algo_objs))
  points = []
  for objs in all_objs:
    point = Point(None)
    point.objectives = objs
    points.append(point)
  points = sel_nsga2(model, points, k)
  return [point.objectives for point in points]

def get_model(model_name):
  if model_name == "ers":
    return emergency_response.EmergencyResponse()
  elif model_name == "wpt":
    return webportal.WebPortal()
  else:
    assert False, "Invalid model name : %s"%model_name

if __name__ == "__main__":
  report()