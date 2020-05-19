# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:12:05 2020

@author: MrKim
"""

class Employee():
    
    def getdata(name,age):
        name = name
        age = age
        
        print("Name: " + name+"\nAge: " + age)
        
    def getdata1(self,name,age):
        self.name=name
        self.age=age

    def putdata(self):
        print("Name: " + self.name+"\nAge: " + self.age)
        
        
        

Employee.getdata("Eric","12")

employee1 = Employee()

employee1.getdata1("Eric","15")
employee1.putdata()