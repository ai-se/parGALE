from __future__ import print_function, division
import sys, os, datetime
sys.path.append(os.path.abspath("."))
from problems.feature_models.webportal import WebPortal
from problems.feature_models.emergency_response import EmergencyResponse
from algorithms.parallel.multi import *
from algorithms.parallel.gale.multi_gale import GALE

if __name__ == "__main__":
  if str(sys.argv[1]) == "WPT":
    model = WebPortal()
  elif str(sys.argv[1]) == "ERS":
    model = EmergencyResponse()
  else:
    assert False, "Invalid Argument"
  outfile = str(sys.argv[2]).strip()+"_"+str(datetime.date.today())
  num_consumers = int(str(sys.argv[3]).strip())
  manager = multiprocessing.Manager()
  results = manager.dict()
  optimizer = GALE
  consumers = [Consumer(optimizer, model, results, i, outfile, num_consumers) for i in range(num_consumers)]
  start_time = time.time()
  for consumer in consumers:
    consumer.start()
  for consumer in consumers:
    consumer.join()
  total_time = time.time() - start_time
  outfile_main = open(str("results/"+outfile+'.csv'), 'a')
  result_count = sum([len(soln) for i in range(num_consumers) for soln in results[i]])
  print("")
  try:
    outfile_main.writelines(
        str(num_consumers) + ',' +
        str(result_count) + ',' +
        str(total_time) + '\n'
    )
  finally:
    outfile_main.close()