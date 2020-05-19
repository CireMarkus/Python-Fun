# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:06:36 2020

@author: MrKim
"""

class test():
    def __init__(self):
        self.a = [1,2,3]
        self.b = [4,5,6]
        self.c = [7,8,9]
        
    def __contains__(self,item):
      if item in self.a:
          return item in self.a 
      elif item in self.b: 
          return item in self.b
      elif item in self.c: 
          return item in self.c
      else:
          return False
       


b = test()

if 3 in b:
    print('yes')
else:
    print('no')