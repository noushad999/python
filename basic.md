*Prepared by: Md Noushad Jahan Ramim*  
**Contact:** [md.noushad@example.com]
```markdown
# 🐍 Python Basics: Variables, Data Types, and Operations

---

## 📌 Using Variables
Variables are used to store data in Python.

### Example:
```python
name = "noushad"
age = "24"
price = 100

print("My name is:", name)
print("My age is:", age)

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'str'>
print(type(price)) # Output: <class 'int'>
```

---

## 🔍 Data Types in Python
Python supports several data types.

### Example:
```python
age = 23
old = False
a = None

print(type(age))  # Output: <class 'int'>
print(type(old))  # Output: <class 'bool'>
print(type(a))    # Output: <class 'NoneType'>
```

---

## ➕ Mathematical Operations
You can perform arithmetic operations like addition, subtraction, multiplication, and division.

### Example:
```python
a = 10
b = 12

sum = a + b
print("Sum is:", sum)

dif = a - b
print("Difference:", dif)

mul = a * b
print("Multiplication:", mul)

div = a / b
print("Division:", div)
```

---

## 💡 Comments
- **Single-line comment:** Use `#`  
- **Multi-line comment:** Use triple quotes `'''` or `"""`

Example:
```python
# This is a single-line comment
'''
This is a 
multi-line comment
'''
```

---

## 🧮 Operators in Python
### 1️⃣ Arithmetic Operators
```python
a = 2
b = 5

sum = a + b
print("Sum is:", sum)

dif = a - b
print("Difference:", dif)

mul = a * b
print("Multiplication:", mul)

div = a / b
print("Division:", div)

remainder = a % b
print("Remainder:", remainder)

power = a ** b
print("Power:", power)
```

### 2️⃣ Relational/Comparison Operators
```python
a = 2
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

### 3️⃣ Assignment Operators
```python
num = 10
num += 10
print("num is", num)  # 20

num -= 10
print("num is", num)  # 10

num *= 10
print("num is", num)  # 100

num /= 10
print("num is", num)  # 10.0

num %= 10
print("num is", num)  # 0.0
```

### 4️⃣ Logical Operators
```python
x = 10
y = 2

print(not False)        # True
print(not (x > y))      # False
print((x > y) and (y < x))  # True
print(x > y or y > x)   # True
```

---

## 🔄 Type Conversion (Type Casting)
Convert between data types in Python.

### Example:
```python
a = int("2")
b = 5.33

print(a + b)  # Output: 7.33
```

---

## 📥 Input from User
The `input()` function is used to take user input.  
By default, the input is a string.

### Example:
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Welcome", name)
print("Age:", age)
print("Marks:", marks)
```

---

## 📝 Practice Problems

### Problem 1: Input Two Numbers and Print Their Sum
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("First number is:", num1)
print("Second number is:", num2)

sum = num1 + num2
print("Sum is:", sum)
```

---

### Problem 2: Calculate Area of a Square
```python
side = int(input("Enter one side of the square: "))
area = side * side
print("Area is:", area)
```

---

### Problem 3: Calculate Average of Two Floating Point Numbers
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

avg = (a + b) / 2
print("Average is:", avg)
```

---

### Problem 4: Compare Two Numbers
```python
d = int(input("Enter first number: "))
e = int(input("Enter second number: "))

print(d >= e)  # Output: True or False
```

---

## 🎉 Conclusion
This document covers Python's basics, including variables, data types, and common operations. By practicing these examples, you’ll strengthen your foundation in Python programming.
```

You can save this as `Python_Basics.md` for easy reference or sharing.
