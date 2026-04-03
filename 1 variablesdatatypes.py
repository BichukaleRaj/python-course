print("Raj") 
print("Raj","Sanjay","Bichukale")
print(3+2)



# A.Rules for Identifiers
# 1)Identifiers can be combination of uppercase and lowercase letters,digits or an underscore(_).SO myVariable,variable_1,var_for_print all are valid puthon identifiers 
# 2)An identifier can not start with digit.So while variable1 is valid,1variable is not valid.
# 3)We can't use special symbols like !,#,@,%,$ etc in our identifier.
# 4)Identifier can be of any length


# B.Data types
#1.String
name="Raj"
#2.Integer
age=20
#3.Float
salary=6000.66
#4.Boolean
ishaunted = True
#5.None
a=None
print(type(name))
print(type(age))
print(type(salary))



#C. Keywords
# and,else,in,return,as,except,is,True,assert,finally,lambda,
# try,break,False,nonlocal,with,class,for,None,while,continue,
# from,not,yield,def,global,or,del,if,pass,elif,import,raise




#D.Operators in Python
#1.Arithematic (+,-,*,/,%,**)
a=500
b=600
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#2.Relational / Comparison (==,!=,<,>,>=,<=)
print(5==5)
print(6<=5)
#3.Assignment (=,+=,-=,*=,/=,%=,**=)
age=56
age += 5
print(age)
age -= 1
print(age)
age *= 5
print(age)
age /= age
print(age)
#means age = age + 5
#4.Logical (not,and,or)
5==5 and 6>5


#E.Type Conversion
a,b = 1,4.25
sum = a+b
print(sum)

#x,y=1,"2"
#print(x+y) #It will give an error

#F. Type Casting
a,b=1,"2"
c=int(b)
print(a+c)

#G. Input
name=input("Enter your name: ")
age=int(input("Enter your age: "))
price=float(input("Enter price of your PC: "))
print("My name is ",name," My age is ",age," The price of my PC is ",price,".")