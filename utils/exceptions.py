from __future__ import print_function, division
import traceback
__author__ = 'panzer'



class RuntimeException(Exception):
  def __init__(self, message):
    super(RuntimeException, self).__init__(message)
    self.name = RuntimeException.__name__

  @staticmethod
  def print_trace():
    traceback.print_exc()