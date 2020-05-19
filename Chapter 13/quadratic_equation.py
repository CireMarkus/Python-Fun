# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:07:51 2020

@author: MrKim
"""
class negative_discriminant(Exception):
    def __init__(self,a):
        self.a=a
    def __str__(self):
        return(self.a)

class quadradic_equation: 
    def  __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.positive_root = 0.0
        self.negative_root = 0.0
        
        self.root_calculation()
    
    def root_calculation(self):
        try:
            under_the_root = self.b**2-4*self.a*self.c
            if (under_the_root < 0.0):
                raise negative_discriminant("Unreal number")
        except negative_discriminant as e:
            print (e.a)
        else:
            self.positive_root = (-self.b)+(under_the_root)**(1/2)
            try:
                self.positive_root=self.positive_root/(2*self.a)
            except ZeroDivisionError:
                self.positive_root = "[Undefined]"
            self.negative_root = (-self.b)-(under_the_root)**(1/2)
            try:  
                self.negative_root=self.negative_root/(2*self.a)
            except ZeroDivisionError:
                self.negative_root = "[Undefined]"
            self.Display(self.positive_root, self.negative_root)
                
    
    def Display(self,a,b):
        print("The positive root is {0}. The negative roots {1}".format(a,b))
        

a = quadradic_equation(2,11,10)



            