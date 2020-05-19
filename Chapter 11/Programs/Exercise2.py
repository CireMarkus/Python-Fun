# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:18 2020

@author: MrKim
"""


class operation():
   def __init__(self,argument):
       self.number = argument
       
   def squareRoot(self):
       return self.number**(1/2)
   
   def cubeRoot(self):
       return self.number**(1/3)
    
    

Num1 = operation(9)
Num2 = operation(27)

List1 = [Num1.squareRoot(),Num1.cubeRoot(),Num2.squareRoot(),Num2.cubeRoot()]

for i in List1:
    print(i)

        