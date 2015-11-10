'''
Created on Jan 17, 2014

@author: ezulkosk
'''
from z3 import *

FeatureIndexMap = {}
FeatureVariable = []
FeatureIndexMap['web_portal'] = 0
web_portal = Bool('web_portal')
FeatureVariable.append(web_portal) 
FeatureIndexMap['web_portal'] = 1
web_portal = Bool('web_portal')
FeatureVariable.append(web_portal) 
FeatureIndexMap['add_services'] = 2
add_services = Bool('add_services')
FeatureVariable.append(add_services) 
FeatureIndexMap['site_stats'] = 3
site_stats = Bool('site_stats')
FeatureVariable.append(site_stats) 
FeatureIndexMap['basic'] = 4
basic = Bool('basic')
FeatureVariable.append(basic) 
FeatureIndexMap['advanced'] = 5
advanced = Bool('advanced')
FeatureVariable.append(advanced) 
FeatureIndexMap['site_search'] = 6
site_search = Bool('site_search')
FeatureVariable.append(site_search) 
FeatureIndexMap['images'] = 7
images = Bool('images')
FeatureVariable.append(images) 
FeatureIndexMap['text'] = 8
text = Bool('text')
FeatureVariable.append(text) 
FeatureIndexMap['html'] = 9
html = Bool('html')
FeatureVariable.append(html) 
FeatureIndexMap['dynamic'] = 10
dynamic = Bool('dynamic')
FeatureVariable.append(dynamic) 
FeatureIndexMap['ad_server'] = 11
ad_server = Bool('ad_server')
FeatureVariable.append(ad_server) 
FeatureIndexMap['reports'] = 12
reports = Bool('reports')
FeatureVariable.append(reports) 
FeatureIndexMap['popups'] = 13
popups = Bool('popups')
FeatureVariable.append(popups) 
FeatureIndexMap['banners'] = 14
banners = Bool('banners')
FeatureVariable.append(banners) 
FeatureIndexMap['ban_img'] = 15
ban_img = Bool('ban_img')
FeatureVariable.append(ban_img) 
FeatureIndexMap['ban_flash'] = 16
ban_flash = Bool('ban_flash')
FeatureVariable.append(ban_flash) 
FeatureIndexMap['keyword'] = 17
keyword = Bool('keyword')
FeatureVariable.append(keyword) 
FeatureIndexMap['web_server'] = 18
web_server = Bool('web_server')
FeatureVariable.append(web_server) 
FeatureIndexMap['logging'] = 19
logging = Bool('logging')
FeatureVariable.append(logging) 
FeatureIndexMap['db'] = 20
db = Bool('db')
FeatureVariable.append(db) 
FeatureIndexMap['file'] = 21
file = Bool('file')
FeatureVariable.append(file) 
FeatureIndexMap['protocol'] = 22
protocol = Bool('protocol')
FeatureVariable.append(protocol) 
FeatureIndexMap['nttp'] = 23
nttp = Bool('nttp')
FeatureVariable.append(nttp) 
FeatureIndexMap['ftp'] = 24
ftp = Bool('ftp')
FeatureVariable.append(ftp) 
FeatureIndexMap['https'] = 25
https = Bool('https')
FeatureVariable.append(https) 
FeatureIndexMap['cont'] = 26
cont = Bool('cont')
FeatureVariable.append(cont) 
FeatureIndexMap['static'] = 27
static = Bool('static')
FeatureVariable.append(static) 
FeatureIndexMap['active'] = 28
active = Bool('active')
FeatureVariable.append(active) 
FeatureIndexMap['asp'] = 29
asp = Bool('asp')
FeatureVariable.append(asp) 
FeatureIndexMap['php'] = 30
php = Bool('php')
FeatureVariable.append(php) 
FeatureIndexMap['jsp'] = 31
jsp = Bool('jsp')
FeatureVariable.append(jsp) 
FeatureIndexMap['cgi'] = 32
cgi = Bool('cgi')
FeatureVariable.append(cgi) 
FeatureIndexMap['persistence'] = 33
persistence = Bool('persistence')
FeatureVariable.append(persistence) 
FeatureIndexMap['xml'] = 34
xml = Bool('xml')
FeatureVariable.append(xml) 
FeatureIndexMap['database'] = 35
database = Bool('database')
FeatureVariable.append(database) 
FeatureIndexMap['ri'] = 36
ri = Bool('ri')
FeatureVariable.append(ri) 
FeatureIndexMap['data_storage'] = 37
data_storage = Bool('data_storage')
FeatureVariable.append(data_storage) 
FeatureIndexMap['data_transfer'] = 38
data_transfer = Bool('data_transfer')
FeatureVariable.append(data_transfer) 
FeatureIndexMap['user_auth'] = 39
user_auth = Bool('user_auth')
FeatureVariable.append(user_auth) 
FeatureIndexMap['performance'] = 40
performance = Bool('performance')
FeatureVariable.append(performance) 
FeatureIndexMap['ms'] = 41
ms = Bool('ms')
FeatureVariable.append(ms) 
FeatureIndexMap['sec'] = 42
sec = Bool('sec')
FeatureVariable.append(sec) 
FeatureIndexMap['min'] = 43
min = Bool('min')
FeatureVariable.append(min) 
#s = Solver()
s = Goal()


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


s.add(web_portal == True)
