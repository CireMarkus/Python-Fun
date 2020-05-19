# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:03:45 2020

@author: MrKim
"""

class Base1:
    def method1(self,message):
        print("This is the base class message: "+message)
    def method2(self):
        self.action1()
        
        

class Derived(Base1):
    def method1(self,message):
        print("derived1 method1: " + message)

class Derived2(Base1):
    def action1(self):
        print("This is the action1 method in derived2")
    


base1 = Base1()
derived1 = Derived()
derived2 = Derived2()

base1.method1('Hello')
derived1.method1('Hello2')
derived2.method1('Hello3')
#base1.method2()
derived2.method2()
#derived1.method2()
derived2.action1()