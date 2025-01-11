i = 1
while i <= 10:
    print(i)
    i += 1

i = 5
while i >= 1:
    print(i)
    i -= 1

i = 1
while i <= 100:
    print(i)
    i += 1

i = 100
while i >= 1:
    print(i)
    i -= 1

n = int(input("Enter a number:"))
i = 1
while i <= 10:
    print(n * i)
    i += 1

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

x = 9
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
while i < len(num):
    if num[i] == x:
        print("Found")
    i += 1

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in num:
    print(val)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for num in tup:
    print(num)

str = "noushad"
for char in str:
    print(char)

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in num:
    print(el)

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49
idx = 0
for el in num:
    if(el == x):
        print("found at index", idx)
        break
    idx += 1
    print(el)

seq = range(10)
for i in seq:
    print(i)

for i in range(2, 10):
    print(i)

for i in range(2, 10, 2):
    print(i)

for i in range(2, 101, 2):
    print(i)

for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)

n = int(input("Enter a number:"))
for i in range(1, 11):
    print(n * i)

for i in range(10):
    pass
print("Some useful work")

n = 5
sum = 0
for i in range(1, n + 1):
    sum += i
print("Total sum is", sum)

n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is", fact)
