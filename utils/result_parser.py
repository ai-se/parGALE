from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.feature_models import emergency_response, webportal
from problems.problem import Point
from utils.nsga2 import select as sel_nsga2
from measures.igd import igd
from utils.lib import mean_iqr

__author__ = 'panzer'

FOLDER      = "results/2016-01-20"
MODEL       = "ers"
ALGOS       = ["gale", "galefs", "gia"]
REPEATS     = 5
PROCESSORS  = 16
MEASURE     = igd

def read(model_name, algo, repeat, processor):
  file_name = FOLDER + "/repeat_" + str(repeat) + "/" + model_name + "_" + algo + "_" + str(processor) + "_objs.csv"
  with open(file_name, 'r') as f:
    lines = f.readlines()
    objs = [map(float, line.strip().split(",")) for line in lines]
  return objs

def compare_algos(model, model_name, repeat, processor):
  algo_objs = []
  for algo in ALGOS:
    algo_objs.append(read(model_name, algo, repeat, processor))
  reference = compute_reference(model, algo_objs)
  measures = []
  for objs in algo_objs:
    measures.append(MEASURE(objs, reference))
  return measures

def compare_processor(model, model_name, processor):
  repeats = []
  for repeat in range(REPEATS):
    repeats.append(compare_algos(model, model_name, repeat, processor))
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
  processor_stats = evaluate_model(MODEL)
  # TODO plot bar charts

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

def _test():
  evaluate_model(MODEL)

if __name__ == "__main__":
  _test()