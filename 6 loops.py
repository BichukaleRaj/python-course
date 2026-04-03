# WHILE LOOP

# count=1
# while count <= 5:
#     print("Hello India")
#     count +=1

# i=5
# while i<6:
#     print(i)
#     i -= 1   #Infinite loop

# Some questions for practice

#Q.1 Print number from 1 to 100
# num = 1
# while num <= 100:
#     print(num)
#     num += 1

#Q.2 print numbers from 100 to 1
# num=100
# while num >=1:
#     print(num)
#     num -= 1

#Q.3 Print the multiplication table of number n

# n=int(input("Enter the number: "))
# i=1
# while i<=10:
#     print(i*n)
#     i += 1

#Q.4 Print the elements of the following list using loop
# list=[1,4,9,16,25,36,49,64,81,100]
# n=len(list)
# i=0
# while i<n:
#     print(list[i])
#     i += 1

#Q.5 Search for a number x in this tuple using loop


# while i<n:
#     if(tuple[i] == x):
#         print("Found at",i)
#     else:
#         print("finding...")
#     i += 1

#             OR

# tuple=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter the number from tuple: "))
# n=len(tuple)
# i=0
# while i<n:
#     if(tuple[i] == x):
#         print("Found at",i)
#         break
#     else:
#         print("finding...")
#     i += 1
"""
-------------------------------------------------------------------------------------------------
"""

#break and continue

# i=1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break   #breaks at 3
#     i += 1  


# i=1
# while i <= 5:
  
#     if(i==3):
#         i+=1
#         continue #acts as skip
#     print(i)  
#     i += 1 

# i=1
# while i <=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i += 1

"""
-------------------------------------------------------------------------------------------------
"""

#FOR LOOP

# #1.for Loops
# list = [1,2,3]
# for el in list:
#     print(el)

# #2 for Loops with else
# for el in list:
#     print(el)
# else:
#     print("END")

#Q. Print the elements of the following list using a loop
# list1 = [1,4,9,16,25,36,49,64,81,100]
# for i in list1:
#     print(i)

# nums =(1,4,9,16,25,36,49,64,81,100)
# x=49
# idx=0
# for i in nums:
#     if(i == x):
#         print(f"{x} at",idx)
#     idx += 1

"""
FOR loop using Range
"""
#case 1 - range(stop)

# for i in range(5):
#     print(i)

# if range(n) then it prints the number from 0 to n-1
#output : 0 1 2 3 4

#case 2 - range(start,stop)

# for i in range(1,5):
#     print(i)

#if range(p,q) then it prints the numbers from p to q-1
#output: 1 2 3 4

#case 3 - range(start,stop,step)

# for i in range(1,10,2):
#     print(i)

#if range(p,q,r) then it prints p to q-1 and it will jump by r ((p+r)th term)
#for eg. 1 2 3 4 5 6 7 8 9
# r = 2
# jump = p+r = 1+2 = 3
#output : 1 3 5 7 9


#Practice questions using for & range()

 #Q.1 print numbers from 1 to 100

# for i in range(1,101):
#     print(i)

# print("Q.2")

 #Q. print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

#Q. Print the multiplication table of a number n
# n=int(input("Enter the number: "))
# for i in range(1,11):
#     print(n*i)

"""
-------------------------------------------------------------------------------------------------
"""

#PASS statement
#When the situation comes in the code when user doesn't want to work inside the for loop but still user have to use that , that time PASS is used 
# for i in range(1,5):
#     if(i==3):
#         pass
#     else:
#         print(i)

# When i == 3 → pass → nothing happens
# So 3 is ignored (no action taken)
# Rest numbers are printed

#Q.1 WAP to find the sum of first n numbers

# n = 5
# sum=0
# i=1
# #using while
# print("using while")
# while i <= n:
#     sum=sum+i
#     print(sum)
#     i +=1
#using for
# n = 5
# sum=0
# print("using for")
# for i in range(1,n+1):
#     sum=sum+i
#     print(sum)

#Q.2 WAP to find factorial of first n numbers

# print("Using while")
# n = 5
# fact = 1
# i = 1

# while i <= n:
#     fact = fact * i
#     i += 1

# print(fact)
    
# print("Using For")
# n=5
# fact = 1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
