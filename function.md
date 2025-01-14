# Functions in Python

## What is a Function?
A function is a block of code that performs a specific task. Functions only run when they are called. They help reduce code duplication and complexity.

### Key Points:
- Functions can accept data as parameters.
- Functions can return results.
- Functions reduce the need for duplicate code.

### Syntax of a Function:
```python
def function_name(parameters):
    # Block of statements
```

---

## Examples of Functions

### 1. Function with Parameters:
```python
def calc_sum(a, b):  # a, b are parameters
    sum = a + b
    print("Sum of two numbers is:", sum)

# Function call with arguments
calc_sum(10, 20)
```

### 2. Function Without Parameters:
```python
def print_hello():
    print("Hello World")

print_hello()
```

### 3. Average of Three Numbers:
```python
def average(a, b, c):
    avg = (a + b + c) / 3
    print(avg)

average(1, 2, 3)
```

---

## Types of Functions

### 1. Built-in Functions:
- Examples: `print()`, `input()`, `len()`, `sum()`, `max()`, `min()`

### 2. User-Defined Functions:
Functions created by users to perform specific tasks.

---

## Function with Return Statement:
```python
def calc_sum(a, b):
    sum = a + b
    return sum

result = calc_sum(10, 20)
print(result)
```

---

## Default Parameters:
```python
def cal_prod(a, b=1):
    print(a * b)  # Multiplication of two numbers
    return a * b

cal_prod(5)
```

---

## Practice Problems:

### 1. Function to Print the Length of a List:
```python
cities = ["dhaka", "mumbai", "delhi", "kolkata"]

def print_length(lst):
    print(len(lst))

print_length(cities)
```

### 2. Function to Print Elements of a List in a Single Line:
```python
cities = ["dhaka", "mumbai", "delhi", "kolkata"]

def print_elements(lst):
    for i in lst:
        print(i, end=" ")

print_elements(cities)
```

### 3. Function to Find the Factorial of a Number:
```python
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

factorial(5)
```

### 4. Function to Convert USD to BDT:
```python
def converter(usd):
    bdt = 121.75 * usd
    print(bdt)

converter(100)
```

### 5. Function to Check if a Number is Odd or Even:
```python
def check_num(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

print(check_num(5))
print(check_num(6))
