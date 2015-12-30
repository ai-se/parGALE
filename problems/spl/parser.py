from __future__ import print_function, division
import sys, os, re
sys.path.append(os.path.abspath("."))
from utils.lib import O
import xml.etree.ElementTree as ET

__author__ = 'panzer'

PATTERN_FEATURES = re.compile('(\t*):([a-z]?)\s*([a-zA-Z0-9_ ]*)\s*\W(\w+)\W.*')
PATTERN_GROUPS = re.compile('\t*:g \W(\w+)\W \W(\d),([\d\*])\W.*')

class Node(O):
  def __init__(self, level, node_id, node_name=None, node_type='o', parent=None):
    O.__init__(self)
    self.level = level
    self.id = node_id
    self.name = node_name
    self.type = node_type
    self._parent = parent
    if parent:
      parent.update_child(self)
    self._children = None
    if self.type == 'g':
      self.grouping = 'OR'

  def update_child(self, child):
    child._parent = self
    if not self._children:
      self._children = []
    self._children.append(child)

  def __repr__(self):
    pre = "|.. "
    node_str = "%sid: %s, type: %s, name: %s\n"%(pre*self.level, self.id, self.type, self.name)
    if self._children:
      for child in self._children:
        node_str += repr(child)
    return node_str


def parse_spl(url):
  tree = ET.parse(url)
  features_text, constraints_text = None, None
  for child in tree.getroot():
    if child.tag == "feature_tree":
      features_text = child.text
    elif child.tag == "constraints":
      constraints_text = child.text

  lines = filter(bool,features_text.split("\n"))
  levels = dict()
  for line in lines:
    match = PATTERN_FEATURES.match(line)
    level = len(match.group(1))
    tag = match.group(2) if match.group(2) else None
    name = match.group(3) if match.group(3) else None
    uid = match.group(4)

    if tag == 'r':
      root = Node(level, uid, node_name=name, node_type=tag)
      levels[level] = root
    elif tag == 'g':
      group = PATTERN_GROUPS.match(line)
      uid = group.group(1)
      upper = group.group(3)
      node = Node(level, uid, node_type=tag, parent=levels[level-1])
      levels[level] = node
      if upper == '*':
        node.grouping = 'OR'
      else:
        node.grouping = 'XOR'
    elif tag == 'm' or tag == 'o':
      node = Node(level, uid, node_name=name, node_type=tag, parent=levels[level-1])
      levels[level] = node
  print(root)






parse_spl("problems/spl/references/web_portal.xml")
