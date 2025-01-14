def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)

show(5)

def show(n):
    print(n)
    show(n - 1)

show(5)

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(5))

def print_list(lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    print_list(lst, idx + 1)

fruits = ["apple", "banana", "mango", "orange"]
print_list(fruits, 0)