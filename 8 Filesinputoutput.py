"""
Types of files:
"""
# Text Files: .txt, .docx, .log etc
# Binary Files: .mp4, .mov, .png, .jpeg etc

"""
Open,read & close File
"""

# f = open("file_name","mode")

# file_name can be sample.txt,demo.docx
# modes are read mode and write mode
"""
Different modes
"""
# 'r' → open for reading (default)
# 'w' → open for writing, truncating the file first
# 'x' → create a new file and open it for writing
# 'a' → open for writing, appending to the end of the file if it exists
# 'b' → binary mode
# 't' → text mode (default)
# '+' → open a disk file for updating (reading and writing)



#Read Operation
#f=open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","r")
#data = f.read()
#data1 = f.readline()
#print(data)
#print(data1)
#f.close()

#Write Operation
# f=open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","w")
# f.write("This is a new line.")
#f.close()

 #append operation
# f=open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","a")
# f.write("This is an another new line.")
#f.close()

# using '+' 
# f=open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","r+")
# f.write("ABCDE")
# print(f.read())
# f.close()

# f=open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","w+")
# #f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()    #truncate the previous data

# f=open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","a+")
# #f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

"""
with syntax:
"""
# with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","r") as f:
#       data=f.read()
#       print(data)

with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt","w") as f:
      f.write("Getting over it")
      

"""
Deleting the File
"""   
#using the os module

#import os
#os.remove(filename)

# import os
# os.remove(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\demo.txt")

#Practice questions
#Q.1 Create a newfile "practice.txt" using python. Add the following data in it
# with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\practice.txt","w") as f:
#       f.write("Hi everyone.\nWe are learning File IO\nusing java.\nI like programming in java.")

#Q.2 WAF that replace all the occurrences of "java" with "python" in above file.
# with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\practice.txt","r+") as f:
#       data=f.read()
#       new_data=data.replace("java","python")
#       print(new_data)

# with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\practice.txt","w") as f:
#       f.write(new_data)

#Q.3 search if the word "learning" exists in the file or not
# with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\practice.txt","r") as f:
#       data=f.read()
#       if(data.find("learning")):
#             print("found")

# def check_for_word():
#       with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\practice.txt","r") as f:
#        data=f.read()
#        if(data.find("learning")):
#             print("found")
# check_for_word()


#Q.4 WAF to find in which line of the file does the word "learning"occur first.print -1 if word not found
# def check_for_line():
#       data =True
#       word="learning"
#       line_no=1
#       with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\practice.txt","r") as f:
#             while data:
#                   data=f.readline()
#                   if(word in data):
#                     print(line_no) 
#                     return 
#                   line_no += 1   
#       return -1       
# check_for_line()   

#Q.5 From a file containing numbers seperated by comma,print the count of even numbers.
# count =0
# with open(r"C:\do not touch\coding\python\Python DSA basics\8 filesinputoutput\numbers.txt") as f:
#      data=f.read()

#      nums=data.split(",")
#      for val in nums:
#           if(int(val) % 2 == 0):
#                count +=1
# print(count)
          
     
        