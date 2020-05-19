# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:27:12 2020

@author: MrKim
"""

class Complex_Number():
    def __init__(self,real,imaginary):
        self.real = real 
        self.imaginary = imaginary

#Function that overloads the addition operator
# to add complex numbers
    def __add__(self,other):
        
        self.real = self.real + other.real
        self.imaginary = self.imaginary + other.imaginary
        return self.display(self.real,self.imaginary)
#Function that overloads the subraction 
# operator to subtract complex numbers 
    def __sub__(self,other):
        self.real = self.real-other.real
        self.imaginary = self.imaginary - other.imaginary
        
        return self.display(self.real,self.imaginary)
#Function that overloads the multiplication operator 
# to multiply the two complex numbers. 
    def __mul__(self,other):
        a = self.real * other.real
        b = (self.real*other.imaginary) + (self.imaginary * other.real)
        c = (self.imaginary * other.imaginary)*-1
        
        self.real = a+c
        self.imaginary = b
        return self.display(self.real,self.imaginary)
#Function that overloads the division operator 
# to divide the complex numbers. 
    def __truediv__(self,other):
# overloads the string output of the function to print 
# the formatted complex number. 
        numerator = Complex_Number(self.real,self.imaginary) * Complex_Number(other.real,(other.imaginary)*-1)
        denomenator = Complex_Number(other.real,other.imaginary) * Complex_Number(other.real,(other.imaginary)*-1)
        
        return "{}/{}".format(numerator,denomenator)
    def __str__(self):
        return "{:+}{:+}i".format(self.real,self.imaginary)
      
    def display(self,real,imaginary):
        if(real == 0 and imaginary == 0):
            return 0
        elif(real == 0):
            if(imaginary < 0):
                if(imaginary == -1):
                    return "-i"
                else:
                    return "{:+}i".format(imaginary)
            else:
                if(imaginary == 1):
                    return "i"
                else:
                    return "{}i".format(imaginary)
        elif(real < 0):
            return "{:+}{:+}i".format(real,imaginary)
        elif(imaginary == 0):
            return "{}".format(real)
        elif(imaginary == -1):
            if(real > 0):
                return "{}-i".format(real,imaginary)
            else:
                return "{:+}-i".foramt(real,imaginary)

            
        else:
            if(imaginary == 1):
                return "{}+i".format(real)
            elif(imaginary == -1):
                return "{}-i".format(real)            
            return "{}{:+}i".format(real,imaginary)
        
        


class Calculator():
    
    
    def menu():
        menu_inputs = ["A","B","C","D","E"]
        user_input = ""  
        
        print("Please enter a letter corresponsing to a menu option.")
        while True: 
            try:
                print("A. Add complex numbers\n"
                      "B.Subtract complex numbers\n"
                      "C. Multiply complex numbers\n"
                      "D. Divide Complex numbers\n"
                      "E. Exit Calculator\n")
                user_input = str.upper(input("What would you like to do?\n\nEnter Option:")) 
                
                if(str.upper(user_input) not in menu_inputs):
                    raise TypeError
                else: 
                    if(user_input == 'A'):
                        real_a = 0
                        imaginary_a = 0
                        real_b = 0
                        imaginary_b = 0
                        
                        while True: 
                            try:
                                real_a = int(input("Please enter the real part of the first number:"))
                                imaginary_a = int(input("Please enter the imaginary part, excluding the i, of the first number: "))
                                break
                            except ValueError:
                                print("Please enter an integer for your number(s)")
                                continue
                        
                        while True:
                            try: 
                                real_b = int(input("Please enter the real part of the second number:"))
                                imaginary_b = int(input("Please enter the imaginary part, excluding the i, of the second number: "))
                                break
                            except ValueError:
                                print("Please neter an integer for your number(s)")
                                continue    
                        print(Complex_Number(int(real_a),int(imaginary_a)) + Complex_Number(int(real_b),int(imaginary_b)))
                        print("\n\n\n\n\n\n\n\n\n")
                        
                    elif(user_input =='B'):
                        real_a = 0 
                        imaginary_a = 0
                        real_b = 0 
                        imaginary_b = 0 
                        
                        while True: 
                            try: 
                                real_a = int(input("Please enter the real part of your first number: "))
                                imaginary_a = int(input("Please enter the imaginary part, excluding the i, of your first number: "))
                                break
                            except ValueError:
                                print("Please enter an integer for your number(s)")
                                continue
                                print("Enter an integer for your number(s)")
                                continue
                                continue
                        while True:
                            try:
                                real_b = int(input("Please enter the real part of your second number: "))
                                imaginary_b = int(input("Please enter the imaginary part, excluding the i, of your second number : "))
                                break
                            except ValueError:
                                print("Please enter an integer for your number(s)")
                                continue
                                print("Enter an integer for your number(s)")
                                continue
                        print(Complex_Number(int(real_a),int(imaginary_a)) - Complex_Number(int(real_b),int(imaginary_b)))
                        print("\n\n\n\n\n\n\n\n\n")
                        
                    elif(user_input == 'C'):
                        real_a = 0
                        imaginary_a = 0
                        real_b = 0 
                        imaginary_b = 0
                        
                        while True: 
                            try:
                                real_a = int(input("Enter the real part of your first number: "))
                                imaginary_a = int(input("Enter the imaginary part, excluding the i, of your first number: "))
                                break
                            except ValueError: 
                                print("Please enter an integer in as your number(s)")
                                continue
                            
                        while True: 
                            try:  
                                real_b = int(input("Enter the real part of your second number: "))
                                imaginary_b = int(input("Enter the imaginary part, excluding the i, of your second number: "))
                                break
                            except ValueError: 
                                print("Please enter an integer in as your number(s)")
                                continue
                        print(Complex_Number(real_a,imaginary_a) * Complex_Number(real_b,imaginary_b))
                        print("\n\n\n\n\n\n\n\n\n")
                        
                    elif(user_input == 'D'):
                        real_a = 0 
                        imaginary_a = 0 
                        real_b = 0 
                        imaginary_b = 0 
                        
                        while True: 
                            try: 
                                real_a = int(input("Enter the real part of your first number: "))
                                imaginary_a = int(input("Enter the imaginary part, excluding the i, of your first number: "))
                                break
                            except ValueError: 
                                print("Please enter an integer in as your number(s)")
                                continue
                        
                        while True: 
                            try: 
                                real_b = int(input("Enter the real part of your second number: "))
                                imaginary_b = int(input("Enter the imaginary part, exculding the i, of your second number: "))
                                break
                            except ValueError: 
                                print("Please enter an integer in as your number(s)")
                                continue 
                        print(Complex_Number(real_a,imaginary_a) / Complex_Number(real_b,imaginary_b))
                        print("\n\n\n\n\n\n\n\n\n")
                    elif(user_input == 'E'):
                        print("Thank you for using")
                        break
            except TypeError:
                print("Pleasee chose an option from the menu")
                continue
            
                


# print(Complex_Number(4,-5) * Complex_Number(12,11))
# print(Complex_Number(-3,-1) - Complex_Number(6,-7))
# print(Complex_Number(1,4) - Complex_Number(-16,9))
# print(Complex_Number(0,8) * Complex_Number(10,2))
# print(Complex_Number(-3,-9) * Complex_Number(1,10))
# print(Complex_Number(2,7) * Complex_Number(8,3))
# print(Complex_Number(7,-1) / Complex_Number(2,10))
# print(Complex_Number(1,5) / Complex_Number(0,-3))
# print(Complex_Number(6,7) / Complex_Number(0,0))




Calculator.menu()
