info={
    "name":"Raj",
    "subjects":["python","C","Java"],
    "topics":("dict","list"),
    "age":20,
    "is_adult":True
}
"""
print(info["subjects"])
print(info["topics"])
print(info["name"])
info["name"]="jinu" #overwrites value of particular key
info["surname"]="Gundu" #adding new key-value pair
print(info)
"""

#nested Dict
student={
    "name":"Raj",
    "Score":{
        "Physics":95.36,
        "Chemisry":30.25,
        "Mathematics":95.40
    },
    "Total":90.34,
    "College":"MESWCOE",
    "CGPA":8.066
}
print(student)

info={
    "name":"Raj",
    "subjects":["python","C","Java"],
    "topics":("dict","list"),
    "age":20,
    "is_adult":True
}

"""
#Dict Methods
print(info.keys())
print(info.values())
print(info.items())
print(info.get("age"))

print(list(student.keys()))
print(len(info)) #No. of keys in dict

new_dict = {"City" : "Pune"}
student.update(new_dict)
print(student)
"""

# Sets in python

nums = {1,2,3,4}
set2={1,2,2,2}

null_set=set() #empty set syntax

# We can only store boolean,int,float,string and tuple..We can't store list and dict
"""
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3.5)
collection.add("Jinu")
collection.add((6,5,9))
print(collection)
collection.remove(2)
print(collection)
collection.pop()
print(collection)
collection.clear()
print(collection)
"""


#Methods in sets
#Sets are mutable but we can't change the value of elements
"""
collection1={1,2,2,6,8.5,"Khalu",True}
collection2={1,2,4,6,9.5,"Gundu",False}

print(collection1.union(collection2))
print(collection1.intersection(collection2))
"""

# Practice Questions
#Q.1
random={
    "table":["a piece of furniture","list of facts"],
    "Cat":"a small animal"
}
print(random)

#Q.2 You are given a list of subjects for students>assume 1 classroom is required for 1 subject.How many classrooms are needed by all students.
subjects={"python","java","C++","javascript","C++","java","python"}
print("Total classrooms needed by the all students will be:",len(subjects))

# Q.3 WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value.
student_info={}

x=float(input("Enter physics: "))
student_info.update({"Physics":x})

y=float(input("Enter chemistry: "))
student_info.update({"Chemistry":y})

z=float(input("Enter maths: "))
student_info.update({"Mathematics":z})

print(student_info)

#Q.4 Figure out a way to store 9 & 9.0 as seperate values in a set.

# case 1:
values1={9,"9.0"}
print(values1)

#case 2:
values2={"9",9.0}
print(values2)

#Using built-in data type
values3={("Float",9.0),("Int",9)}
print(values3)