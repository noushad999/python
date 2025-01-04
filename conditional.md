
---

# 🌟 Conditional Statements in Python


---

## 📜 Syntax  

<details>
<summary>🔍 Click to expand syntax details!</summary>

```python
if condition:  # Executes if the condition is True
    statement1
elif condition:  # Executes if the previous conditions are False, and this one is True
    statement2
else:  # Executes if all conditions are False
    statementN
```

</details>  

---

## 🔥 Examples  

### ✅ Simple `if` and `else`  
<details>
<summary>🔗 Click to view example</summary>

```python
age = 14
if age >= 18:
    print("can vote")
    print("can drive")
else:
    print("can't vote")
```

Output:  
> can't vote  

</details>  

---

### 🟢 Using `elif`  
<details>
<summary>🔗 Click to view example</summary>

```python
light = "green"

if light == "red":
    print("Stop")
elif light == "green":
    print("Go")
elif light == "yellow":
    print("Go fast")
else:
    print("Invalid light")

print("End of code")
```

Output:  
> Go  
> End of code  

</details>  

---

## 🧮 Grading Students Based on Marks  

### 🎓 Conditions  
- **`marks >= 90`** → Grade = `A`  
- **`90 > marks >= 80`** → Grade = `B`  
- **`80 > marks >= 60`** → Grade = `C`  
- **`marks < 60`** → Grade = `D`  

<details>
<summary>🔗 Click to view example</summary>

```python
marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks < 90 and marks >= 80:
    grade = "B"
elif marks < 80 and marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade is:", grade)
```

Example Input:  
> 85  

Output:  
> Grade is: B  

</details>  

---

## 🔄 Nested Conditions  
<details>
<summary>🔗 Click to view example</summary>

```python
age = 64
if age >= 18:
    if age >= 90:
        print("Can't drive")
    else:
        print("Can drive")
else:
    print("Can't drive")
```

Example Output:  
> Can drive  

</details>  

---

## 🛠️ Practice Problems  

### 🧮 Problem 1: Odd or Even  
<details>
<summary>🔗 Click to view solution</summary>

```python
num = int(input("Enter a valid number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Example Input:  
> 5  

Output:  
> Odd  

</details>  

---

### 🏆 Problem 2: Find the Greatest of Three Numbers  
<details>
<summary>🔗 Click to view solution</summary>

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")
```

Example Input:  
> a = 7, b = 12, c = 5  

Output:  
> b is greater  

</details>  

---

### 🧮 Problem 3: Check if a Number is a Multiple of 7  
<details>
<summary>🔗 Click to view solution</summary>

```python
x = int(input("Enter a number: "))
if x % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")
```

Example Input:  
> 14  

Output:  
> Multiple of 7  

</details>  

---

**Prepared by:** *Md Noushad Jahan Ramim*  
**Contact:** contactwithnoushad@gmail.com

---
