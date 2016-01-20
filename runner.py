from __future__ import print_function, division
import sys, os, datetime
sys.path.append(os.path.abspath("."))
from problems.feature_models.webportal import WebPortal
from problems.feature_models.emergency_response import EmergencyResponse
from algorithms.parallel.multi import *
from algorithms.parallel.gale.multi_gale import GALE
from algorithms.parallel.de.multi_de import DE
from utils.lib import mkdir, mean_iqr, write_objs
from utils.nsga2 import select as sel_nsga2

REPEATS = 5

def _multi_test():
  if str(sys.argv[1]) == "WPT":
    model = WebPortal()
  elif str(sys.argv[1]) == "ERS":
    model = EmergencyResponse()
  else:
    assert False, "Invalid Argument"
  if str(sys.argv[2]) == "DE":
    optimizer = DE
  elif str(sys.argv[2]) == "GALE":
    optimizer = GALE
  else:
    assert False, "Invalid Argument"
  new_dir = mkdir("results/"+str(datetime.date.today())+"/")
  outfile = new_dir+str(sys.argv[3]).strip()
  num_consumers = int(str(sys.argv[4]).strip())
  do_feature_split = sys.argv[5]
  manager = multiprocessing.Manager()
  runtimes = []
  result_count = 0
  for rep in xrange(REPEATS):
    results = manager.dict()
    features_splits = None
    if num_consumers > 1 and do_feature_split == 'y':
      features_splits = model.split_features(num_consumers)
    consumers = [Consumer(optimizer, model, results, i, outfile, num_consumers, features_splits = features_splits) for i in range(num_consumers)]
    start_time = time.time()
    for consumer in consumers:
      consumer.start()
    for consumer in consumers:
      consumer.join()
    total_time = time.time() - start_time
    all_results = []
    seen = []
    for i in range(num_consumers):
      for result in results[i]:
        for r in result:
          if r.objectives not in seen:
            all_results.append(r)
            seen.append(r.objectives)
    if len(all_results) > consumers[0].settings.GALE_pop_size:
      all_results = sel_nsga2(model, all_results, consumers[0].settings.GALE_pop_size)
    objs = [result.objectives for result in all_results]
    obj_file = mkdir(new_dir+"/repeat_"+str(rep)+"/")+str(sys.argv[3]).strip()
    write_objs(objs, obj_file)
    runtimes.append(total_time)
    result_count += len(all_results)
    print("")
  outfile_main = open(str(outfile+'.csv'), 'a')
  result_count //= REPEATS
  total_time_mean, total_time_iqr = mean_iqr(runtimes)
  try:
    outfile_main.writelines(
        str(num_consumers) + ',' +
        str(result_count) + ',' +
        str(total_time_mean) + ',' +
        str(total_time_iqr) + '\n'
    )
  finally:
    outfile_main.close()


def _single_test():
  if str(sys.argv[1]) == "WPT":
    model = WebPortal()
  elif str(sys.argv[1]) == "ERS":
    model = EmergencyResponse()
  else:
    assert False, "Invalid Argument"
  if str(sys.argv[2]) == "DE":
    optimizer = DE
  elif str(sys.argv[2]) == "GALE":
    optimizer = GALE
  else:
    assert False, "Invalid Argument"
  new_dir = mkdir("results/"+str(datetime.date.today())+"/")
  outfile = new_dir+str(sys.argv[3]).strip()
  num_consumers = int(str(sys.argv[4]).strip())
  do_feature_split = sys.argv[5]
  manager = multiprocessing.Manager()
  results = manager.dict()
  features_splits = None
  if num_consumers > 1 and do_feature_split == 'y':
    features_splits = model.split_features(num_consumers)
  consumers = [Consumer(optimizer, model, results, i, outfile, num_consumers, features_splits = features_splits) for i in range(num_consumers)]
  start_time = time.time()
  for consumer in consumers:
    consumer.start()
  for consumer in consumers:
    consumer.join()
  total_time = time.time() - start_time
  all_results = []
  seen = []
  for i in range(num_consumers):
    for result in results[i]:
      for r in result:
        if r.objectives not in seen:
          all_results.append(r)
          seen.append(r.objectives)
  if len(all_results) > consumers[0].settings.GALE_pop_size:
    all_results = sel_nsga2(model, all_results, consumers[0].settings.GALE_pop_size)
  objs = [result.objectives for result in all_results]
  write_objs(objs, outfile+"_"+str(num_consumers)+"_objs")
  result_count = len(all_results)
  outfile_main = open(str(outfile+'.csv'), 'a')
  try:
    outfile_main.writelines(
        str(num_consumers) + ',' +
        str(result_count) + ',' +
        str(total_time) + '\n'
    )
  finally:
    outfile_main.close()



if __name__ == "__main__":
  _multi_test()