import numpy as np
import random
import pickle
import re
import xml.etree.ElementTree as ET
import sys, os
sys.path.append(os.path.abspath("."))
from utils.lib import O


class Node(O):
    def __init__(self, id, parent = None, node_type = 'o'):
        O.__init__(self)
        self.id = id
        self.parent = parent
        self.node_type = node_type
        self.children = []
        if node_type == 'g':
            self.g_u = 1
            self.g_d = 0

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def __repr__(self):
        return '| id: %s, type:%s'%(
            self.id,
            self.node_type)

class Constraint(O):
    def __init__(self, id, literals, literals_pos):
        O.__init__(self)
        self.id = id
        self.literals = literals
        self.li_pos = literals_pos

    def __repr__(self):
        return self.id+'\n'+str(self.literals)+'\n'+str(self.li_pos)

    def iscorrect(self, ft, filledForm):
        for (li, pos) in zip(self.literals, self.li_pos):
            i = ft.find_fea_index_by_id(li)
            if int(pos) == filledForm[i]: return True
        return False


class FeatureTree(O):
    def __init__(self):
        O.__init__(self)
        self.root = None
        self.features = []
        self.groups = []
        self.leaves = []
        self.con = []
        self.cost = []
        self.featureNum = 0

    def set_root(self,root):
        self.root = root

    def add_constraint(self,con):
        self.con.append(con)

    def find_fea_index_by_id(self, id):
        for i,x in enumerate(self.features):
            if x.id == id:
                return i

    # featch all the features in the tree basing on the children structure
    def set_features_list(self):
        def setting_feature_list(self,node):
            if node.node_type == 'g':
                node.g_u = int(node.g_u) if node.g_u != np.inf else len(node.children)
                node.g_d = int(node.g_d) if node.g_d != np.inf else len(node.children)
                self.features.append(node)
                self.groups.append(node)
            if node.node_type != 'g':
                self.features.append(node)
            if len(node.children) == 0:
                self.leaves.append(node)
            for i in node.children:
                setting_feature_list(self, i)
        setting_feature_list(self, self.root)
        self.featureNum = len(self.features)

    def postorder(self, node, func, extraArgs = []):
        if node.children:
            for c in node.children:
                self.postorder(c,func, extraArgs)
        func(node, *extraArgs)


    # setting the form by the structure of feature tree
    # leaves should be filled in the form in advanced
    # all not filled feature should be -1 in the form
    def fillForm4AlFea(self, form):
        def filling(node):
            index = self.features.index(node)
            if form[index] != -1:
                return
            # handeling the group featues
            if node.node_type == 'g':
                sum = 0
                for c in node.children:
                    i_index = self.features.index(c)
                    sum += form[i_index]
                form[index] = 1 if sum >= node.g_d and sum <= node.g_u else 0
                return

            """
            # the child is a group
            if node.children[0].node_type == 'g':
                form[index] = form[index+1]
                return
            """

            #handeling the other type of node
            m_child = [x for x in node.children if x.node_type in ['m','r','g']]
            o_child = [x for x in node.children if x.node_type == 'o']
            if len(m_child) == 0: #all children are optional
                s = 0
                for o in o_child:
                    i_index = self.features.index(o)
                    s += form[i_index]
                form[index] = 1 if s>0 else 0
                return
            for m in m_child:
                i_index = self.features.index(m)
                if form[i_index] == 0:
                    form[index] = 0
                    return
            form[index] = 1
            return

        self.postorder(self.root, filling)

    def getFeatureNum(self):
        return len(self.features) - len(self.groups)

    def getConsNum(self):
        return len(self.con)

    def _genRandomCost(self,tofile):
        any=random.random
        self.cost = [any() for _ in self.features]
        f = open(tofile, 'w')
        pickle.dump(self.cost, f)
        f.close()

    def loadCost(self, fromfile):
        if not os.path.isfile(fromfile):
            self._genRandomCost(fromfile)
        f = open(fromfile)
        self.cost = pickle.load(f)
        f.close()

    @staticmethod
    def load_ft_url(url):
        # load the feature tree and constraints
        tree = ET.parse(url)
        root = tree.getroot()
        feature_tree, constraints = None, None
        for child in root:
            if child.tag == 'feature_tree':
                feature_tree = child.text
            if child.tag == 'constraints':
                constraints = child.text

        # initialize the feature tree
        ft = FeatureTree()

        # parse the feature tree text
        feas = feature_tree.split("\n")
        feas = filter(bool, feas)
        common_feature_pattern = re.compile('(\t*):([romg]?).*\W(\w+)\W.*')
        group_pattern = re.compile('\t*:g \W(\w+)\W \W(\d),([\d\*])\W.*')
        layer_dict = dict()
        for f in feas:
            m = common_feature_pattern.match(f)
            """
            m.group(1) layer
            m.group(2) type
            m.group(3) id
            """
            layer = len(m.group(1))
            t = m.group(2)
            if t == 'r':
                treeRoot = Node(id = m.group(3), node_type = 'r')
                layer_dict[layer] = treeRoot
                ft.set_root(treeRoot)
            elif t== 'g':
                mg = group_pattern.match(f)
                """
                mg.group(1) id
                mg.group(2) down_count
                mg.group(3) up_count
                """
                gNode = Node(id = mg.group(1), parent = layer_dict[layer-1], node_type = 'g')
                layer_dict[layer] = gNode
                if mg.group(3) == '*':
                    gNode.g_u = np.inf
                else:
                    gNode.g_u = mg.group(3)
                gNode.g_d = mg.group(2)
                layer_dict[layer] = gNode
                gNode.parent.add_child(gNode)
            else:
                treeNode = Node(id = m.group(3), parent = layer_dict[layer-1], node_type = t)
                layer_dict[layer] = treeNode
                treeNode.parent.add_child(treeNode)

        # parse the constraints
        cons = constraints.split('\n')
        cons = filter(bool, cons)
        common_con_pattern = re.compile('(\w+):(~?)(\w+)(.*)\s*')
        common_more_con_pattern = re.compile('\s+(or) (~?)(\w+)(.*)\s*')

        for cc in cons:
            literal = []
            li_pos = []
            m = common_con_pattern.match(cc)
            con_id = m.group(1)
            li_pos.append(not bool(m.group(2)))
            literal.append(m.group(3))
            while m.group(4):
                cc = m.group(4)
                m = common_more_con_pattern.match(cc)
                li_pos.append(not bool(m.group(2)))
                literal.append(m.group(3))
            """
             con_id: constraint identifier
             literal: literals
             li_pos: whether is positive or each literals
            """
            con_stmt = Constraint(id = con_id, literals = literal, literals_pos = li_pos)
            ft.add_constraint(con_stmt)

        ft.set_features_list()

        return ft

def _test():
  ft = FeatureTree.load_ft_url("problems/spl/references/web_portal.xml")
  print(ft)

if __name__ == "__main__":
  _test()