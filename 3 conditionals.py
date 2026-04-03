# if-else

a=50
if(a==50):
    print("Its Half century")
else:
    print("You need more runs!!")

#if-elif-else

age=35
gender="female"
if(age==60):
    print("You will get free ticket to hell")
elif(age<=40 and gender=="female"):
    print("Hey beautiful Lady!! I love you")
else:
    print("Kya ukhad liya jawaan mard banke")

#Practice questions

# 1.WAP to check if number entered by user is odd or even

num=int(input("Enter the number: "))

if(num % 2 ==0 ):
    print("Its an even number.")
else:
    print("Its an odd number.")

#2.WAP to find the greatest of 3 numbers entered by the user
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
n3=int(input("Enter 3rd number: "))

if(n1 > n2 and n1>n3):
    print(f"{n1} is the greatest.")
elif(n2 > n3):
    print(f"{n2} is the greatest.")
else:
    print(f"{n3} is the greatest.")