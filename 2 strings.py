str1="This is a string"
str2='Modern Education'
str3="""This is a string"""
str4 ='Society"s wadia college of engg'
str5="India is my country.\n All indians are my brothers and sisters."
str6="India is my country.\t All indians are my brothers and sisters."
str7="India is my country. All indians are my brothers and sisters."
str8="Bichukale"

#Concatenation
str=str2+" "+str4
print(str)

#length of string
print(len(str7))

#indexing
print(str7[4]) #prints character at index 4
#In indexing we can only access the characters,can't manipulate them.

#slicing
print(str7[:2]) #prints upto 1 character before index 2
print(str7[3:]) #prints character starting from index 3 to end of the string
print(str7[3:11]) #prints characters from index 3 to 10(1 character before nth index)
print(str7[:-1]) #prints from starting to 1 character before last(here last character is '.' so it will print upto sisters)
print(str7[-1:]) #prints only last character
print(str8[-1:-7]) # start=-1 (e), end=-7 (c), step=+1 by default; since slicing moves left→right and start is to the right of end, result is empty string ''
print(str7[::2])#prints alternate characters
print(str7[::-1])#prints reverse string

# I n  d  i  a     i  s     m  y         c   o   u   n   t   r   y   .
# 0 1  2  3  4  5  6  7  8  9  10   11   12  13  14  15  16  17  18  19
# 
#     A   l   l      i   n   d   i   a   n   s     a   r   e      m   y      b   r   o   t   h   e   r   s 
# 20  21  22 23  24  25  26  27  28 29  30 31 32  33   34  35 36  37 38  39  40  41  42  43  44 45  46  47
# 
#      a   n   d      s   i   s   t   e   r   s  .
# 48   49  50  51  52 53 54  55  56  57  58  59  60

#  B     i     c     h     u     k    a    l     e
# -9    -8    -7    -6    -5    -4   -3   -2    -1 

#string functions

str9="I am a Student of Computer Engineering and I like coding"

print(str9.endswith("ing")) #returns true if string ends with substr
print(str9.capitalize()) #capitalize the initial letter of character
print(str9.replace("coding","gaming")) #here old is coding and new is gaming now gamer will replace coder
print(str9.find("coding"))#returns index of 1st occurence
print(str9.count("Student"))#counts the occurence of substr in string

food = "Pizza"
food.replace("z","s")
print(food) #Strings are immutable we can't change them.