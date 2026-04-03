"""
del keyword
"""
#used to delete object properties or object itself
# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Shraddha")
# print(s1.name)
# del s1.name
# print(s1.name)

"""
Private attributes
"""
#these are meant to be used only within the class and are not accessible from outside the class
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass=acc_pass #by adding double under-score before acc_pass we made this attribute private
        
#     def reset_pass(self):
#         print(self.__acc_pass) # we can access it inside the class but not outside the class

# acc1=Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass()) #no error
# print(acc1.__acc_pass) #error "'Account' object has no attribute '__acc_pass'"will occur

"""
Inheritance
"""
#-----------------Single level-----------------
# class Car:
#     color="Black"
#     @staticmethod
#     def start():
#         print("car Started....")


#     @staticmethod
#     def stop():
#         print("car Stopped....")

# class BMW(Car):
#     def __init__(self,name):
#         self.name=name

# car1 = BMW("M5 CS")
# car2 = BMW("X7")
# print(car1.start())
# print(car1.color)

#-----------------Multi-level-----------------
# class Car:
#     color = "Black"

#     @staticmethod
#     def start():
#         print("Car Started....")


# class BMW(Car):
#     def __init__(self, name):
#         self.name = name


# class BMWElectric(BMW):   # Multi-level inheritance
#     def battery(self):
#         print("Electric battery present")


# car1 = BMWElectric("i7")

# car1.start()
# print(car1.color)
# car1.battery()

#-----------------Multiple inheritance-----------------
# class Car:
#     def start(self):
#         print("Car Started....")


# class Engine:
#     def engine_type(self):
#         print("Petrol Engine")


# class BMW(Car, Engine):   # Multiple inheritance
#     def __init__(self, name):
#         self.name = name


# car1 = BMW("M5 CS")

# car1.start()
# car1.engine_type()

"""
Super Method
"""
# The child class wants to use or call the parent class constructor or methods
# The child class has its own constructor, but still needs parent initialization
# To avoid rewriting code (code reuse)

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped.")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()


# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

""""
Class method
"""
#So basically the scene is to change the class variable using object that is why the classmethod is used 
# class Person:
#     name="Anonymous" #Class variable 

#     def changeName(self,name):
#         self.name=name

# p1=Person()
# p1.changeName("Jinu Pengu") #New name created in an object 
# print(p1.name) 
# print(Person.name)

"""
This code can be written as:
"""
#Method1
# class Person:
#     name="Anonymous" #Class variable 

#     def changeName(self,name):
#         Person.name=name

# p1=Person()
# p1.changeName("Jinu Pengu") #New name created in an object 
# print(p1.name) 
# print(Person.name)
#If you run this code,you will see that class variable is changed,this is indirect method of changing the class variable

#Method2
# class Person:
#     name="Anonymous" #Class variable 

#     def changeName(self,name):
#         self.__class__.name="Jinu"

# p1=Person()
# p1.changeName("Jinu Pengu") #New name created in an object 
# print(p1.name) #prints Jinu

#Method3
# class Person:
#     name="Anonymous" #Class variable 

#     # def changeName(self,name):
#     #     self.name=name

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=Person()
# p1.changeName("Jinu Pengu") #New name created in an object 
# print(p1.name) 
# print(Person.name)

"""
Property decorator
"""

# class Student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#         self.percentage = str((self.phy+self.chem+self.maths)/3)+"%"

# s1=Student(95,30,95)
# print(s1.percentage)

# #If we change the mark in any subject
# s1.phy=86
# print(s1.phy)
# print(s1.percentage) #The overall percentage should be changed

#Method 1
# class Student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
         
#     def CalPercent(self):
#         self.percentage = str((self.phy+self.chem+self.maths)/3)+"%"
        

# s1=Student(95,30,95)
# print(s1.percentage)

# #If we change the mark in any subject
# s1.phy=86
# print(s1.phy)
# s1.CalPercent()
# print(s1.percentage)

#Method 2 using property decorator
# class Student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
        
#     @property
#     def percentage(self):
#        return str((self.phy+self.chem+self.maths)/3)+"%"

# s1=Student(95,30,95)
# print(s1.percentage)

# #If we change the mark in any subject
# s1.phy=100
# print(s1.percentage)

# @getter,@setter other 2 decorators 
"""
Polymorphism : Operator Overloading
"""
#For example
# print(68+1) #69
# print("Raj" + "Bichukale") #Concatenate
# print([1,2,3] + [4,5,6]) #merge 2 lists

# polymorphism gives many forms of single thing
#Means a single operator or single thing can be used for many uses

# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2): #Dunder Function
#         newReal=self.real + num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal , newImg)
    
#     def __mul__(self,num2): #Dunder Function
#         Newreal=((self.real*num2.real)-(self.img*num2.img))
#         Newimg=((self.real*num2.img)+(self.img*num2.real))
#         return Complex(Newreal,Newimg)
    
# num1=Complex(6,9)
# num1.showNumber()

# num2=Complex(9,7)
# num2.showNumber()

# print("---Addition---")
# num3=num1 + num2
# num3.showNumber()

# print("---Multiplication---")
# num3=num1 * num2
# num3.showNumber()

# Operators & Dunder functions

# a + b  -> addition
# a.__add__(b)  Dunder

# a - b  -> subtraction
# a.__sub__(b)   Dunder

# a * b  -> multiplication
# a.__mul__(b)  Dunder

# a / b  -> division
# a.__truediv__(b)  Dunder

# a % b  -> modulus
# a.__mod__(b)   Dunder

#Practice Problems

#Q.1 Qs. Define a Circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self,radius):
#         self.r=radius

#     def area(self):
#         self.area=3.14*(self.r)**2
#         print(self.area)
    
#     def perimeter(self):
#         self.perimeter=2*3.14*self.r
#         print(self.perimeter)
    
# c1=Circle(20)
# c1.area()
# c1.perimeter()

#Q.2Define a Employee class with attributes role,dept and salary.This class should also have showDetails() method.
#Create an Engineer class that inherits properties from Employee & has additional attributes:name & age.

# class Employee:
#     def __init__(self, roles, department, salary):
#         self.role = roles
#         self.dept = department
#         self.salary = salary

#     def showDetails(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.dept}")
#         print(f"Salary: {self.salary}")


# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", 5000000)

#     def showDetails(self):   # override method
#         super().showDetails()   # call parent method
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# eng1 = Engineer("Raj", 20)
# eng1.showDetails()

#Q.3 Qs. Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price

#     def details(self):
#         print(f"{self.item} : {self.price}Rs.")

#     def __gt__(self,order2):
#         return self.price > order2.price

# order1=Order("RTX 5080 Ti",140000)
# order1.details()
# order2=Order("Intel ultra 7 265K",30000)
# order2.details()

# print(order1<order2)