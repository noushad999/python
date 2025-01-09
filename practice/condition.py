#conditional statements
#if,elif,else
#syntax
# if(condion): ->if the condition is true then the statement will be executed
#     statement1
# elif(condition):
#     statement2
# else:
#     statementN

#example
#if
# age=14
# if(age>=18):
# # if(True):
#     print("can vote")
#     print("can drive")
# else:
#     print("cant vote")


#elif
# light="green"

# if(light=="red"):
#      print("stop")

# elif(light=="green"):
#      print("gogogo")

# elif(light=="yellow"):
#      print("go fast")

# else: -->if all the condition are false then the statement will be executed
#      print("invalid light")

# print("end of code")
# #difference between if and elif is that if the condition is true then the statement will be executed and the rest of the code will be skipped but in case of elif if the condition is true then the statement will be executed and the rest of the code will be executed
#indentation means the proper spacing between the code

'''grade student based on marks
marks>=90 ,grade ="A"
90>marks>=80,grade="B"
80>marks>60,grade="c"
70>marks,grade="D"'''

# marks=int(input("enter your marks :" ))
# if(marks>=90):
#     grade="A"
# elif(marks<90 and marks>=80):
#     grade="B"
# elif(marks<80 and marks>60):
#     grade="c"
# else:
#     grade="D"
# print("Grade is: ",grade)

# nesting condition
# age=64
# if(age>=18):
#     if(age>=90):
#         print("cant drive")
#     else:
#         print("can drive")

#     print("can drive")
# else:
#     print("cant drive")

#wap to check if a number entered by the user is odd or even
# num=int(input("Enter valid number: "))
# if(num%2==0):
#     print("even")
# else:
#     print("odd")

#write a program to find the greayest of 3 numbers given by the user
# a=int(input("enter first  number : "))
# b=int(input("enter second  number : "))
# c=int(input("enter third  numbers  "))

# if(a>b and a>c):
#     print("a is greater")
# elif(b>a and b>c):
#     print("b is greater")
# else:
#     print("c is greater")


#write a program to check if a number is multiple of 7 or not


# x=int(input("enter a number :"))
# if(x%7==0):
#     print("multiple by 7" )
# else:
#     print("not multiple by 7")