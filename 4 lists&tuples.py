marks=[100,96,95,94,90,92,91]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
Student=["Raj",100,"Raigad"]
print(Student)
Student[2]="BMW"
print(Student) #Lists are mutable

#         100   96   95   94   90   92   91
# index:   0     1   2    3     4   5    6
#         -7    -6  -5   -4    -3   -2   -1 

#Slicing 
print(marks[1:4]) #prints elements from index 1 upto index 3
print(marks[:4]) #prints elements from start upto index 3
print(marks[1:]) #prints elemnts from list at index 1 upto end of the list
print(marks[-3:-1]) #prints 90,92
print(marks[::2])#prints alternate elements from list
print(marks[::-1])#prints reverse list

#List Methods
marks.append(60)
print(marks)
marks.sort()
print(marks)
marks.reverse()
marks.insert(4,93)
print(marks)
marks.remove(95)
marks.pop(3)
print(marks)


# ------------------------------------------------------------------------------------------------------------------


 #Tuples in Python

 # A built-in datatype that lets us create immutable sequences of values.Tuples are immutable

tup = (87,64,33,95,76)
# tup[0] = 43  NOT allowed 
tup1 = (1,)
#if you want to create single value tuple then give comma after that tuple 
print(tup[1:3])
#slicing is as the same as list 

#Methods in the Tuple...
print(tup.index(64))
print(tup.count(64))

#Questions to practice
#WAP to check if a list contains a palindrome of elements.(hint:use copy() method)


num=[1,2,3,2,1]
num1=num.copy()
num1.reverse()
print(num1)

#WAP to count the number of students with the "A" grade in the following tuple

grades=("C","D","A","A","B","B","A")
print("Number of students with the grade 'A' is:",grades.count("A"))

