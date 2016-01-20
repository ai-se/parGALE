from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))
from problems.feature_models.consts import METRICS_MINIMIZE, METRICS_MAXIMIZE
from collections import OrderedDict
from base import *
from math import pi, tan

__author__ = 'panzer'

FeatureIndexMap = OrderedDict()
FeatureVariable = []
FeatureIndexMap['web_portal'] = 0
web_portal = Bool('web_portal')
FeatureVariable.append(web_portal) 
FeatureIndexMap['add_services'] = 1
add_services = Bool('add_services')
FeatureVariable.append(add_services) 
FeatureIndexMap['site_stats'] = 2
site_stats = Bool('site_stats')
FeatureVariable.append(site_stats) 
FeatureIndexMap['basic'] = 3
basic = Bool('basic')
FeatureVariable.append(basic) 
FeatureIndexMap['advanced'] = 4
advanced = Bool('advanced')
FeatureVariable.append(advanced) 
FeatureIndexMap['site_search'] = 5
site_search = Bool('site_search')
FeatureVariable.append(site_search) 
FeatureIndexMap['images'] = 6
images = Bool('images')
FeatureVariable.append(images) 
FeatureIndexMap['text'] = 7
text = Bool('text')
FeatureVariable.append(text) 
FeatureIndexMap['html'] = 8
html = Bool('html')
FeatureVariable.append(html) 
FeatureIndexMap['dynamic'] = 9
dynamic = Bool('dynamic')
FeatureVariable.append(dynamic) 
FeatureIndexMap['ad_server'] = 10
ad_server = Bool('ad_server')
FeatureVariable.append(ad_server) 
FeatureIndexMap['reports'] = 11
reports = Bool('reports')
FeatureVariable.append(reports) 
FeatureIndexMap['popups'] = 12
popups = Bool('popups')
FeatureVariable.append(popups) 
FeatureIndexMap['banners'] = 13
banners = Bool('banners')
FeatureVariable.append(banners) 
FeatureIndexMap['ban_img'] = 14
ban_img = Bool('ban_img')
FeatureVariable.append(ban_img) 
FeatureIndexMap['ban_flash'] = 15
ban_flash = Bool('ban_flash')
FeatureVariable.append(ban_flash) 
FeatureIndexMap['keyword'] = 16
keyword = Bool('keyword')
FeatureVariable.append(keyword) 
FeatureIndexMap['web_server'] = 17
web_server = Bool('web_server')
FeatureVariable.append(web_server) 
FeatureIndexMap['logging'] = 18
logging = Bool('logging')
FeatureVariable.append(logging) 
FeatureIndexMap['db'] = 19
db = Bool('db')
FeatureVariable.append(db) 
FeatureIndexMap['file'] = 20
file = Bool('file')
FeatureVariable.append(file) 
FeatureIndexMap['protocol'] = 21
protocol = Bool('protocol')
FeatureVariable.append(protocol) 
FeatureIndexMap['nttp'] = 22
nttp = Bool('nttp')
FeatureVariable.append(nttp) 
FeatureIndexMap['ftp'] = 23
ftp = Bool('ftp')
FeatureVariable.append(ftp) 
FeatureIndexMap['https'] = 24
https = Bool('https')
FeatureVariable.append(https) 
FeatureIndexMap['cont'] = 25
cont = Bool('cont')
FeatureVariable.append(cont) 
FeatureIndexMap['static'] = 26
static = Bool('static')
FeatureVariable.append(static) 
FeatureIndexMap['active'] = 27
active = Bool('active')
FeatureVariable.append(active) 
FeatureIndexMap['asp'] = 28
asp = Bool('asp')
FeatureVariable.append(asp) 
FeatureIndexMap['php'] = 29
php = Bool('php')
FeatureVariable.append(php) 
FeatureIndexMap['jsp'] = 30
jsp = Bool('jsp')
FeatureVariable.append(jsp) 
FeatureIndexMap['cgi'] = 31
cgi = Bool('cgi')
FeatureVariable.append(cgi) 
FeatureIndexMap['persistence'] = 32
persistence = Bool('persistence')
FeatureVariable.append(persistence) 
FeatureIndexMap['xml'] = 33
xml = Bool('xml')
FeatureVariable.append(xml) 
FeatureIndexMap['database'] = 34
database = Bool('database')
FeatureVariable.append(database) 
FeatureIndexMap['ri'] = 35
ri = Bool('ri')
FeatureVariable.append(ri) 
FeatureIndexMap['data_storage'] = 36
data_storage = Bool('data_storage')
FeatureVariable.append(data_storage) 
FeatureIndexMap['data_transfer'] = 37
data_transfer = Bool('data_transfer')
FeatureVariable.append(data_transfer) 
FeatureIndexMap['user_auth'] = 38
user_auth = Bool('user_auth')
FeatureVariable.append(user_auth) 
FeatureIndexMap['performance'] = 39
performance = Bool('performance')
FeatureVariable.append(performance) 
FeatureIndexMap['ms'] = 40
ms = Bool('ms')
FeatureVariable.append(ms) 
FeatureIndexMap['sec'] = 41
sec = Bool('sec')
FeatureVariable.append(sec) 
FeatureIndexMap['min'] = 42
min = Bool('min')
FeatureVariable.append(min) 
s = Solver()


# Parent-Children
s.add(Implies(add_services, web_portal))
s.add(Implies(web_server, web_portal))
s.add(Implies(persistence, web_portal))
s.add(Implies(ri, web_portal))
s.add(Implies(performance, web_portal))
s.add(Implies(site_stats, add_services))
s.add(Implies(site_search, add_services))
s.add(Implies(ad_server, add_services))
s.add(Implies(basic, site_stats))
s.add(Implies(advanced, site_stats))
s.add(Implies(images, site_search))
s.add(Implies(text, site_search))
s.add(Implies(html, text))
s.add(Implies(dynamic, text))
s.add(Implies(reports, ad_server))
s.add(Implies(popups, ad_server))
s.add(Implies(banners, ad_server))
s.add(Implies(keyword, ad_server))
s.add(Implies(ban_img, banners))
s.add(Implies(ban_flash, banners))
s.add(Implies(logging, web_server))
s.add(Implies(protocol, web_server))
s.add(Implies(cont, web_server))
s.add(Implies(db, logging))
s.add(Implies(file, logging))
s.add(Implies(nttp, protocol))
s.add(Implies(ftp, protocol))
s.add(Implies(https, protocol))
s.add(Implies(static, cont))
s.add(Implies(active, cont))
s.add(Implies(asp, active))
s.add(Implies(php, active))
s.add(Implies(jsp, active))
s.add(Implies(cgi, active))
s.add(Implies(xml, persistence))
s.add(Implies(database, persistence))
s.add(Implies(data_storage, ri))
s.add(Implies(data_transfer, ri))
s.add(Implies(user_auth, ri))
s.add(Implies(ms, performance))
s.add(Implies(sec, performance))
s.add(Implies(min, performance))


# Mandatory-Children
s.add(web_server == web_portal)
s.add(basic == site_stats)
s.add(html == text)
s.add(reports == ad_server)
s.add(banners == ad_server)
s.add(ban_img == banners)
s.add(cont == web_server)
s.add(static == cont)


# Exclusive-Or Constraints
s.add(db == And(Not(file), logging))
s.add(file == And(Not(db), logging))
s.add(xml == And(Not(database), persistence))
s.add(database == And(Not(xml), persistence))
s.add(ms == And(Not(sec), Not(min), performance))
s.add(sec == And(Not(ms), Not(min), performance))
s.add(min == And(Not(ms), Not(sec), performance))


# Or Constraints
s.add(protocol == Or(nttp, ftp, https))
s.add(active == Or(asp, php, jsp, cgi))
s.add(ri == Or(data_storage, data_transfer, user_auth))


# Requires Constraints
s.add(Implies(dynamic, active))
s.add(Implies(keyword, text))
s.add(Implies(db, database))
s.add(Implies(file, ftp))
s.add(Implies(data_transfer, https))


# Excludes Constraints
s.add(Not(And(https, ms)))


# Attributes
total_Cost = Real('total_Cost')
total_UsedBefore = Int('total_UsedBefore')
total_FeatureCount = Int('total_FeatureCount')
total_Defects = Int('total_Defects')



# Sums for Attributes
s.add(total_Cost == 7.6 * If(web_portal, 1.0, 0.0) \
+ 7.5 * If(add_services, 1.0, 0.0) \
+ 14.7 * If(site_stats, 1.0, 0.0) \
+ 6.2 * If(basic, 1.0, 0.0) \
+ 10.4 * If(advanced, 1.0, 0.0) \
+ 9.8 * If(site_search, 1.0, 0.0) \
+ 8.1 * If(images, 1.0, 0.0) \
+ 13.5 * If(text, 1.0, 0.0) \
+ 11.0 * If(html, 1.0, 0.0) \
+ 8.9 * If(dynamic, 1.0, 0.0) \
+ 7.7 * If(ad_server, 1.0, 0.0) \
+ 6.5 * If(reports, 1.0, 0.0) \
+ 11.4 * If(popups, 1.0, 0.0) \
+ 7.4 * If(banners, 1.0, 0.0) \
+ 13.4 * If(ban_img, 1.0, 0.0) \
+ 5.5 * If(ban_flash, 1.0, 0.0) \
+ 6.1 * If(keyword, 1.0, 0.0) \
+ 12.3 * If(web_server, 1.0, 0.0) \
+ 5.7 * If(logging, 1.0, 0.0) \
+ 10.3 * If(db, 1.0, 0.0) \
+ 5.9 * If(file, 1.0, 0.0) \
+ 11.5 * If(protocol, 1.0, 0.0) \
+ 13.7 * If(nttp, 1.0, 0.0) \
+ 13.0 * If(ftp, 1.0, 0.0) \
+ 10.0 * If(https, 1.0, 0.0) \
+ 9.7 * If(cont, 1.0, 0.0) \
+ 11.1 * If(static, 1.0, 0.0) \
+ 12.2 * If(active, 1.0, 0.0) \
+ 8.6 * If(asp, 1.0, 0.0) \
+ 10.6 * If(php, 1.0, 0.0) \
+ 13.0 * If(jsp, 1.0, 0.0) \
+ 12.1 * If(cgi, 1.0, 0.0) \
+ 10.5 * If(persistence, 1.0, 0.0) \
+ 14.1 * If(xml, 1.0, 0.0) \
+ 6.7 * If(database, 1.0, 0.0) \
+ 5.0 * If(ri, 1.0, 0.0) \
+ 9.6 * If(data_storage, 1.0, 0.0) \
+ 5.2 * If(data_transfer, 1.0, 0.0) \
+ 12.2 * If(user_auth, 1.0, 0.0) \
+ 13.7 * If(performance, 1.0, 0.0) \
+ 11.7 * If(ms, 1.0, 0.0) \
+ 9.1 * If(sec, 1.0, 0.0) \
+ 8.3 * If(min, 1.0, 0.0) \
)

o1_wts = [7.6, 7.5, 14.7, 6.2, 10.4, 9.8, 8.1, 13.5, 11.0, 8.9, 7.7, 6.5, 11.4, 7.4, 13.4, 5.5,
          6.1, 12.3, 5.7, 10.3, 5.9, 11.5, 13.7, 13.0, 10.0, 9.7, 11.1, 12.2, 8.6, 10.6, 13.0,
          12.1, 10.5, 14.1, 6.7, 5.0, 9.6, 5.2, 12.2, 13.7, 11.7, 9.1, 8.3]

s.add(total_UsedBefore == 1 * If(web_portal, 0, 1) \
+ 1 * If(add_services, 0, 1) \
+ 0 * If(site_stats, 0, 1) \
+ 1 * If(basic, 0, 1) \
+ 1 * If(advanced, 0, 1) \
+ 1 * If(site_search, 0, 1) \
+ 1 * If(images, 0, 1) \
+ 1 * If(text, 0, 1) \
+ 1 * If(html, 0, 1) \
+ 1 * If(dynamic, 0, 1) \
+ 1 * If(ad_server, 0, 1) \
+ 1 * If(reports, 0, 1) \
+ 0 * If(popups, 0, 1) \
+ 1 * If(banners, 0, 1) \
+ 1 * If(ban_img, 0, 1) \
+ 1 * If(ban_flash, 0, 1) \
+ 1 * If(keyword, 0, 1) \
+ 1 * If(web_server, 0, 1) \
+ 0 * If(logging, 0, 1) \
+ 1 * If(db, 0, 1) \
+ 0 * If(file, 0, 1) \
+ 1 * If(protocol, 0, 1) \
+ 1 * If(nttp, 0, 1) \
+ 1 * If(ftp, 0, 1) \
+ 0 * If(https, 0, 1) \
+ 0 * If(cont, 0, 1) \
+ 1 * If(static, 0, 1) \
+ 0 * If(active, 0, 1) \
+ 0 * If(asp, 0, 1) \
+ 1 * If(php, 0, 1) \
+ 1 * If(jsp, 0, 1) \
+ 1 * If(cgi, 0, 1) \
+ 0 * If(persistence, 0, 1) \
+ 0 * If(xml, 0, 1) \
+ 1 * If(database, 0, 1) \
+ 0 * If(ri, 0, 1) \
+ 1 * If(data_storage, 0, 1) \
+ 1 * If(data_transfer, 0, 1) \
+ 1 * If(user_auth, 0, 1) \
+ 0 * If(performance, 0, 1) \
+ 0 * If(ms, 0, 1) \
+ 1 * If(sec, 0, 1) \
+ 1 * If(min, 0, 1) \
)
o2_wts = [1,1,0]+[1]*9+[0]+[1]*5+[0,1,0,1,1,1]+[0,0,1]*2+[1,1]+[0,0]+[1,0,1,1,1,0,0,1,1]

s.add(total_FeatureCount == 1 * If(web_portal, 0, 1) \
+ 1 * If(add_services, 0, 1) \
+ 1 * If(site_stats, 0, 1) \
+ 1 * If(basic, 0, 1) \
+ 1 * If(advanced, 0, 1) \
+ 1 * If(site_search, 0, 1) \
+ 1 * If(images, 0, 1) \
+ 1 * If(text, 0, 1) \
+ 1 * If(html, 0, 1) \
+ 1 * If(dynamic, 0, 1) \
+ 1 * If(ad_server, 0, 1) \
+ 1 * If(reports, 0, 1) \
+ 1 * If(popups, 0, 1) \
+ 1 * If(banners, 0, 1) \
+ 1 * If(ban_img, 0, 1) \
+ 1 * If(ban_flash, 0, 1) \
+ 1 * If(keyword, 0, 1) \
+ 1 * If(web_server, 0, 1) \
+ 1 * If(logging, 0, 1) \
+ 1 * If(db, 0, 1) \
+ 1 * If(file, 0, 1) \
+ 1 * If(protocol, 0, 1) \
+ 1 * If(nttp, 0, 1) \
+ 1 * If(ftp, 0, 1) \
+ 1 * If(https, 0, 1) \
+ 1 * If(cont, 0, 1) \
+ 1 * If(static, 0, 1) \
+ 1 * If(active, 0, 1) \
+ 1 * If(asp, 0, 1) \
+ 1 * If(php, 0, 1) \
+ 1 * If(jsp, 0, 1) \
+ 1 * If(cgi, 0, 1) \
+ 1 * If(persistence, 0, 1) \
+ 1 * If(xml, 0, 1) \
+ 1 * If(database, 0, 1) \
+ 1 * If(ri, 0, 1) \
+ 1 * If(data_storage, 0, 1) \
+ 1 * If(data_transfer, 0, 1) \
+ 1 * If(user_auth, 0, 1) \
+ 1 * If(performance, 0, 1) \
+ 1 * If(ms, 0, 1) \
+ 1 * If(sec, 0, 1) \
+ 1 * If(min, 0, 1) \
)
o3_wts = [1]*43

s.add(total_Defects == 5 * If(web_portal, 1, 0) \
+ 6 * If(add_services, 1, 0) \
+ 0 * If(site_stats, 1, 0) \
+ 8 * If(basic, 1, 0) \
+ 5 * If(advanced, 1, 0) \
+ 6 * If(site_search, 1, 0) \
+ 5 * If(images, 1, 0) \
+ 6 * If(text, 1, 0) \
+ 4 * If(html, 1, 0) \
+ 4 * If(dynamic, 1, 0) \
+ 6 * If(ad_server, 1, 0) \
+ 4 * If(reports, 1, 0) \
+ 0 * If(popups, 1, 0) \
+ 2 * If(banners, 1, 0) \
+ 4 * If(ban_img, 1, 0) \
+ 5 * If(ban_flash, 1, 0) \
+ 5 * If(keyword, 1, 0) \
+ 1 * If(web_server, 1, 0) \
+ 0 * If(logging, 1, 0) \
+ 5 * If(db, 1, 0) \
+ 0 * If(file, 1, 0) \
+ 7 * If(protocol, 1, 0) \
+ 6 * If(nttp, 1, 0) \
+ 6 * If(ftp, 1, 0) \
+ 0 * If(https, 1, 0) \
+ 0 * If(cont, 1, 0) \
+ 3 * If(static, 1, 0) \
+ 0 * If(active, 1, 0) \
+ 0 * If(asp, 1, 0) \
+ 3 * If(php, 1, 0) \
+ 6 * If(jsp, 1, 0) \
+ 5 * If(cgi, 1, 0) \
+ 0 * If(persistence, 1, 0) \
+ 0 * If(xml, 1, 0) \
+ 5 * If(database, 1, 0) \
+ 0 * If(ri, 1, 0) \
+ 3 * If(data_storage, 1, 0) \
+ 4 * If(data_transfer, 1, 0) \
+ 4 * If(user_auth, 1, 0) \
+ 0 * If(performance, 1, 0) \
+ 0 * If(ms, 1, 0) \
+ 6 * If(sec, 1, 0) \
+ 6 * If(min, 1, 0) \
)

s.add(web_portal == True)
metrics_variables = [total_Cost, total_Defects, total_FeatureCount, total_UsedBefore]
metrics_objective_direction = [METRICS_MINIMIZE, METRICS_MINIMIZE, METRICS_MINIMIZE, METRICS_MINIMIZE]

highs = [422, 30, 43, 145]
lows = [0.0, 0, 0, 0]
# set_option('auto_config', False)
# set_option('smt.phase_selection',5)
# set_option('smt.random_seed',100)
# s.push()

class WebPortal(FeatureModel):
  def __init__(self, directions=None, is_empty=False, **settings):
    if directions is None:
      directions = [True, True, False, False]
    FeatureModel.__init__(self, FeatureVariable, metrics_variables,
                          s, highs, lows, directions, is_empty, **settings)
    self.name = WebPortal.__name__

  @staticmethod
  def region_constraints(index, total):
    degree = 90/total
    split_rules = []
    if index == 0:
      radian_higher = degree * pi / 180
      gradient_higher = FeatureModel.get_gradient(radian_higher)
      split_rules.append(1000 * (total_Cost - 422) * 145 >= IntVal(gradient_higher) * (total_Defects - 145) * 422)
    elif index == total - 1:
      radian_lower = (degree * index) * pi / 180
      gradient_lower = FeatureModel.get_gradient(radian_lower)
      split_rules.append(1000 * (total_Cost - 422) * 145 < IntVal(gradient_lower) * (total_Defects - 145) * 422)
    else:
      radian_lower = (degree * index) * pi / 180
      gradient_lower = FeatureModel.get_gradient(radian_lower)
      split_rules.append(1000 * (total_Cost - 422) * 145 < IntVal(gradient_lower) * (total_Defects - 145) * 422)
      radian_higher = (degree * (index + 1)) * pi / 180
      gradient_higher = FeatureModel.get_gradient(radian_higher)
      split_rules.append(1000 * (total_Cost - 422) * 145 >= IntVal(gradient_higher) * (total_Defects - 145) * 422)
    return And(split_rules)

  def clone(self, other=None):
    other = WebPortal(is_empty=True)
    return FeatureModel.clone(self, other)

  def convert_to_points(self, lst):
    objective_index_map = {}
    for i, obj in enumerate(self.objective_vector):
      objective_index_map[str(obj)] = i
    pts = []
    for one in lst:
      objs =[0]*len(self.objectives)
      decs =[0]*len(self.decisions)
      for tup, val in one:
        tup_str = str(tup)
        val = eval(val)
        if tup_str in FeatureIndexMap:
          decs[FeatureIndexMap[tup_str]] = val
        elif tup_str in objective_index_map:
          objs[objective_index_map[tup_str]] = val
      pt = Point(decs)
      pt.objectives = objs
      pts.append(pt)
    return pts

def _test():
  def format_dec(dec):
    d_form = []
    for d in dec:
      if d: d_form.append(1)
      else: d_form.append(0)
    return d_form
  portal = WebPortal()
  constraints = portal.split_features(4)
  portal.solver.add(constraints[0])
  portal.base_solver.add(constraints[0])
  pop = portal.populate(5)
  for one in pop:
    print(format_dec(one), portal.evaluate(one))

if __name__ == "__main__":
  _test()