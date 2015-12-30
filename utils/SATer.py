from __future__ import print_function, division
import sys, os
sys.path.append(os.path.abspath("."))

__author__ = 'panzer'

class Term:
  def __init__(self, term_id, name=None, negate=False):
    self.id = term_id
    self.name = name
    self.negate = negate

  def clone(self):
    return Term(self.id, self.name, self.negate)

  def get_value(self, value):
    if self.negate:
      return not value
    return value

  def get_negation(self):
    cloned = self.clone()
    cloned.negate = not cloned.negate
    return cloned


class Operator:
  def __init__(self, name, *args):
    self.name = name
    self.operands = args

  def evaluate(self, values):
    """
    To be overridden by
    sub classes
    :return:
    """
    assert False
    pass

  # def is_set(self):
  #   return all([operand.value is not None for operand in self.operands])

class AND(Operator):
  def __init__(self, *args):
    Operator.__init__(self, AND.__name__, *args)

  def evaluate(self, values):
    status = True
    for operand in self.operands:
      status = status and operand.get_value(values[operand.id])
      if not status:
        return False
    return True

class OR(Operator):
  def __init__(self, *args):
    Operator.__init__(self, OR.__name__, *args)

  def evaluate(self, values):
    status = False
    for operand in self.operands:
      status = status or operand.get_value(values[operand.id])
      if status:
        return True
    return False

class XOR(Operator):
  def __init__(self, *args):
    Operator.__init__(self, XOR.__name__, *args)

  def evaluate(self, values):
    status = self.operands[0].get_value(values[self.operands[0].id])
    for operand in self.operands[1:]:
      if status and operand.get_value(values[operand.id]):
        return False
      status = status or operand.get_value(values[operand.id])
    return status

