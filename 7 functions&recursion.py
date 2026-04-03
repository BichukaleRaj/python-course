"""
SYNTAX :
"""
# def fun_name(param1,param2):
#     some work
#     return val

# func_name(arg1,arg2..) function call

# def sum(a,b):
#     return a+b

# print(sum(5,8))

#Default parameter

# def add(a=2,b=6):
#     print(a+b)
#     return a+b

# add()

# Q.1 WAF to print length of the list

# lst = [5,8,9,7,3]

# def length(lst):
#     print("Length of list is:", len(lst))

# length(lst)

#Q.2 WAF to print the elements of a list in a single line.(list is the parameter)

# lst = [5,8,9,7,3]

# def print_lst(lst):
#     for i in lst:
#         print(i,end=" ")

# print_lst(lst)

#Q.3 WAF to find the factorial of n.(n is the paramater)

# n=int(input("Enter the number of which you want factorial: "))

# n=int(input("Enter number:"))

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#       fact *= i
#     print(fact)

# factorial(5)

#Q.4 WAF to convert USD to INR

# USD=int(input("Enter the value in US dollars: "))

# def INR_converter(USD):
#     INR= 93.97 * USD
#     print(f"{USD} USD = {INR} INR")

# INR_converter(USD)

"""
Recursion
"""

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(6)

#Q.1 Write arecursive function to calvulate sum of first n natural numbers

# def calc_sum(n):
#     if(n==0):
#         return 0
    
#     return calc_sum(n-1) + n

# sum = calc_sum(3)
# print(sum)

#Q.2 Write a recursive function to print all elements in a list.
#Hint :  use list & index as parameters.


# def print_lst(lst,idx):
#     if(idx==len(lst)):
#         return
#     print(lst[idx])
#     print_lst(lst,idx+1)

# num=[1,2,3,4,5,6,8]
# print_lst(num,0)

