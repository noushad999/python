
def calc_sum(a, b):
    sum = a + b
    print("Sum of two numbers is:", sum)

calc_sum(10, 20)

def print_hello():
    print("Hello World")

print_hello()

def average(a, b, c):
    avg = (a + b + c) / 3
    print(avg)

average(1, 2, 3)

def clac_sum(a, b):
    sum = a + b
    print(sum)

calc_sum(10, 20)

def cal_prod(a, b=1):
    print(a * b)
    return a * b

cal_prod(1)

cities = ["dhaka", "mumbai", "delhi", "kolkata"]

def print_length(list):
    print(len(list))

print_length(cities)

cities = ["dhaka", "mumbai", "delhi", "kolkata"]

def print_elements(list):
    for i in list:
        print(i, end=" ")

print_elements(cities)

n = 5

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        print(fact)

factorial(n)

def converter(usd):
    bdt = 121.75 * usd
    print(bdt)

converter(100)

def check_num(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

print(check_num(5))
print(check_num(6))