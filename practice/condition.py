# if-else example
age=14
if age >= 18:
    print("can vote")
    print("can drive")
else:
    print("cant vote")

# elif example
light = "green"
if light == "red":
    print("stop")
elif light == "green":
    print("gogogo")
elif light == "yellow":
    print("go fast")
else:
    print("invalid light")

print("end of code")

# Grade student based on marks
marks = int(input("enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks < 90 and marks >= 80:
    grade = "B"
elif marks < 80 and marks > 60:
    grade = "C"
else:
    grade = "D"
print("Grade is:", grade)

# Nesting condition
age = 64
if age >= 18:
    if age >= 90:
        print("cant drive")
    else:
        print("can drive")
else:
    print("cant drive")

# Check if a number is odd or even
num = int(input("Enter a valid number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Find the greatest of 3 numbers
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

# Check if a number is a multiple of 7
x = int(input("enter a number: "))
if x % 7 == 0:
    print("multiple by 7")
else:
    print("not multiple by 7")
