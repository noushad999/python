# string is a data type that store a sequence of character

# str1="this is a string" #most common way to define a string
# str2='this is also string'
# str3='''this is also a string''' #triple quote is used to define a multiple line string
# str4="""this is also a string"""

# str1="this is a string \n.we are creating this"
# print(str1)

# operations on string
# concatenation:adding two or multiple strings

# str1="noushad"
# str2="ramim"
# finalstr=str1+str2
# print(finalstr)

# length of string
# str1="noushad"
# str2="ramim"
# finalstr=str1+ " " +str2
# print(len(finalstr))#13 because space is also counted

# string indexing - to access a particular character from a string

# str="noushad ramim"
# # ch=str[11]
# print(str[7])

# slicing-to access part of a string
# str [starting index:ending index] -ending index is not included

# str="md noushad jahan ramim"

# print(str[3:8]) #noush
# print(str[ :8]) #md noush
# print(str[3:]) #noushad jahan ramim
# print(str[ : ]) #md noushad jahan ramim
# print(str[ : :2]) #m osa aa ai
# print(str[5:len(str)]) #ushad jahan ramim

# negative indexing-to access character from the end of the string

# str="apple" #strar from -1 to -5
# # print(str[-2]) #l
# print(str[-1:-5]) #empty - because -1 is grater then 1
# print(str[-5:-1]) #appl
# print(str[-2:-4]) #empty -because -2 is grater then -4
# print(str[-5: ]) #apple

# string funtions
# str="i am a coder"
# print(str.endswith("er")) #true -str.endswith() is used to check if a string ends with a particular character
# print(str.startswith("am")) #false str.startswith() is used to check if a string starts with a particular character
# str=str.capitalize() #-we do this to store the change in a string
# print(str) #I am a coder -str.capitalize() is used to capatalize the first character of a string
# print(str.replace("coder","developer")) #-str.replace() is used to replace a particular character with another character
# print(str.find("a")) #str.find() is used to find the index of a particular character in a string it peaks the first occurance of the character
# print(str.find("a",9)) #it return 1 because it starts searching from index 9
# print(str.find("x")) #it return -1 because x is not present in the string

# print(str.count("a")) #2 str.count() is used to count the number of occurance of a particular character in a string

# prac1
# write a program to input users first name and print its length

# name=input("enter your name")
# print("your name  length is",len(name))

# prac2
# write a program  to find the occurence of $ in a string

# str="my $ name $ is $ noushad $"
# print("$ counts : ",str.count("$"))
