#use variable

name="noushad"
age="24"
price=100

print("my name is: ",name)
print("my age is:",age)

print(type(name))
print(type(age))
print(type(price))

#data type

age=23
old=False
a=None

print(type(age))
print(type(old))
print(type(a))

#print sum

a=10
b=12

sum=a+b
print("sum is:",sum)

dif=a-b
print("dif:",dif)

mul=a*b
print("mul:",mul)

div=a/b
print("div",div)

#comment
#single line comment
'''Multiline 
comment'''

#operator
#arithmetic operator
a=2
b=5

sum=a+b
print("sum is:",sum)

dif=a-b
print("dif:",dif)

mul=a*b
print("mul:",mul)

div=a/b
print("div",div)

div=a%b
print("div",div) #reminder

div=a**b
print("div",div) #power

#relational/comparison operator

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#assignment operator
num=10
num+=10
print("num is",num) #20

num-=10
print("num is",num) #10

num*=10
print("num is",num) #100

num/=10
print("num is",num) #10

num%=10
print("num is",num)#0

num**=10
print("num is",num)#0

#logical operator
x=10
y=2

print(not False)
print(not(x>y))
print((x>y) and (y<x))
print(x>y or y<x)

#type conversion/type casting
a=int("2")
b=5.33

print(a+b)

#Input-it is used to take input from user.and by default it is string

name=input("Enter your name:")
age=int(input("enter your age"))
marks=float(input("enter your marks"))

print("welcome",name)
print("age",age)
print("marks",marks)

#prac:write a program to input 2 numbers and print their sum

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("First number is",num1)
print("second number is",num2)

sum=num1+num2
print("sum is:",sum)

#prac:write a program to input side of a square and print it area

a=int(input("enter one side of square: "))
area=a*a
print("area is ",area)

#prac:write a program to input 2 floating point number and print their avg

a=float(input("enter first number"))
b=float(input("enter second number"))

avg=(a+b)/2
print("avg is",avg)

#prac:write a program to input 2 number d and e,print trie if a is grater then b,if not print falsr

d=int(input("enter 1st no:"))
e=int(input("Enter 2nd no : "))

print(d>=e)
