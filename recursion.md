# Recursion

## What is Recursion?

A function that calls itself is called a **recursive function**. Recursion is used when a problem can be divided into smaller subproblems. Looping is done implicitly in recursion, and recursion can also be done implicitly in looping.

### Example of Recursion with a Base Case

```python
def show(n):
    if n == 0:  # Base case
        return
    print(n)
    show(n - 1)

show(5)
```

If we comment out the base case, the function will run infinitely and give an error:

```python
def show(n):
    print(n)
    show(n - 1)

show(5)
```

## When to Use Recursion?

Recursion is used when the problem can be divided into smaller subproblems. It is not always the best approach, and it is typically used in specific use cases.

### Factorial Example

A recursive function to calculate the factorial of a number:

```python
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))  # Output: 120
```

### Sum of Natural Numbers

A recursive function to calculate the sum of the first `n` natural numbers:

```python
def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(5))  # Output: 15
```

### Print All Elements in a List

A recursive function to print all elements in a list:

```python
def print_list(lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    print_list(lst, idx + 1)

fruits = ["apple", "banana", "mango", "orange"]
print_list(fruits, 0)
