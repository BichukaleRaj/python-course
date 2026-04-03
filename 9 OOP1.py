"""
Class & Object in Python
"""

#Class is the blueprint for creating objects

# #creating class
# class Student:
#     name ="Dhurandhar is not the Propaganda"

# #creating object
# s1=Student()
# print(s1.name)


"""
_ _init_ _ Function
"""
#It is a constructor
#All the classes have a function called __init__(),which is always executed when the object is being initiated.

# #Creating class
# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
    
# # Creating object
# s1=Student("Karan Arjun")
# print(s1.name)


# class Student:
#     name="Karan"
#     def __init__(self):
#         print("adding new student in detebase..")

# s1=Student()

# #default constructors
# def __init__(self):
#     pass


# #Parameterized constructors
# class Student:
#     def __init__(self,fullname,marks):
#         self.name=fullname # self.name is the variable that will create newly inside the object
#                            #fullname and marks are the parameters
#         self.marks=marks
#         print("adding new student in Database..")

# s1=Student("Karan",50)
# print(s1.name,s1.marks)

# s2=Student("Arjun",60)
# print(s2.name,s2.marks)

"""
Class & Instance Attributes
""" 

# class Student:
#     college_name = "ABC college"
#     name="Anonymous" #class attr

#     def __init__(self,name,marks):
#         self.name=name #obj.attr
#         self.marks=marks
#         print("adding new student in database")


# s1 = Student("karan",97)
# print(s1.name)

#when we have same name of class attribute and same name of object attribute the object attribute is always prioritized

"""
Methods
"""
# #Creating Class
# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#     def hello(self):
#         print("hello",self.name)

# #Creating Object
# s1=Student("Karan")
# s1.hello()

#Q. Create a student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

# This is my solution:
# class Student:
#     def __init__(self,marks1,marks2,marks3):
#         self.Physics=marks1
#         self.Chemistry=marks2
#         self.Maths=marks3
    
#     def avg(self):
        
#         self.avg=(self.Physics+self.Chemistry+self.Maths)/3
#         print(self.avg)

# s1=Student(95,95,95)
# s1.avg()

#This is Solution from lecture:
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#         print("Hi",self.name,"your avg score is: ",sum/3)

# s1=Student("Raj",[90,92,93])
# s1.get_avg()

"""
Static Methods
"""
#Methods that don't use self parameters
class Student:
    @staticmethod
    def college():
        print("ABC College")

"""
4 pillars of OOP
"""
#1.Abstraction
#Hiding the implementation details of a class and only showing the essentials features to the user

# class Car:
#     def start(self):
#         print("Car started")

#     def drive(self):
#         print("Car is driving")

# c1 = Car()
# c1.start()
# c1.drive()

#2.Encapsulation
#Wrapping data and functions into a single unit

# class Student:
#     def __init__(self):
#         self.__marks = 0   # private variable

#     def set_marks(self, m):
#         self.__marks = m

#     def get_marks(self):
#         return self.__marks

# s1 = Student()
# s1.set_marks(85)
# print(s1.get_marks())

#Practice
#Create account class with 2 attributes - balance and account no.Create methods for debit,credit and printing the balance
# This is my solution
# class Account:
#     AccountNo = 914603
#     balance = 500000

#     def debit(self):
#         self.amount = int(input("Enter the amount to be debited: "))
#         self.balance = self.balance - self.amount
#         print(f"Money is debited. Your current balance is {self.balance}.")

#     def credit(self):
#         self.amount = int(input("Enter the amount to credit: "))
#         self.balance = self.balance + self.amount
#         print(f"Money is credited. Your current balance is {self.balance}.")


# bank = Account()
# bank.debit()
# bank.credit()


#this is the solution from lecture
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = ", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance = ", self.get_balance())

#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)


