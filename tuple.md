
#### **Tuples**
- Tuples are immutable sequences of values.
- Once created, the elements of a tuple cannot be modified.

```python
tup = (87, 32, 22, 77, 22)
print(tup)       # Output: (87, 32, 22, 77, 22)
print(tup[1])    # Output: 32
```

- **Empty Tuple**: An empty tuple is defined as:

```python
tup = ()
print(tup)       # Output: ()
print(type(tup)) # Output: <class 'tuple'>
```

- **Single Element Tuple**: A comma is required to define a single-element tuple.

```python
tup = (1,)
print(tup)       # Output: (1,)
```

If the comma is omitted, it will not be a tuple:

```python
tup = (1)
print(tup)       # Output: 1 (integer)
```

- **Tuple Slicing**: Slicing works similarly to lists.

```python
tup = (1, 2, 3, 4)
print(tup[1:3])  # Output: (2, 3)
print(tup[:3])   # Output: (1, 2, 3)
print(tup[:])    # Output: (1, 2, 3, 4)
```

- **Tuple Methods**:
  - `index(value)`: Returns the index of the first occurrence of the value.
  - `count(value)`: Returns the count of the specified value in the tuple.

```python
tup = (2, 1, 3, 1)
print(tup.index(1))  # Output: 1
print(tup.count(2))  # Output: 1
```

---

#### **Working with Lists**
1. **Store Favorite Movies**:
   - **Using `append()`**:

```python
movies = []
movies.append(input("Enter your favorite movie 1: "))
movies.append(input("Enter your favorite movie 2: "))
movies.append(input("Enter your favorite movie 3: "))
print(movies)
```

   - **Direct Input**:

```python
movies = [
    input("Enter your favorite movie 1: "),
    input("Enter your favorite movie 2: "),
    input("Enter your favorite movie 3: ")
]
print(movies)
```

2. **Check for Palindrome in a List**:
   - A palindrome is a sequence that reads the same forward and backward.

```python
palindrome = [1, 2, 3, 4, 3, 2, 1]
palindrome_copy = palindrome.copy()
palindrome_copy.reverse()

if palindrome == palindrome_copy:
    print("Palindrome")
else:
    print("Not a palindrome")
```

3. **Count "A" Grades in a Tuple**:
   - Use the `count()` method to count occurrences of a value.

```python
grades = ("c", "d", "A", "a", "b", "b", "a")
print(grades.count("a"))  # Output: 3
```

4. **Sort a List**:
   - Convert a tuple to a list, then sort it alphabetically.

```python
grades = ["c", "d", "a", "a", "b", "b", "a"]
grades.sort()
print(grades)  # Output: ['a', 'a', 'a', 'b', 'b', 'c', 'd']
```

---

### Converted to GitHub Markdown

```markdown
# Python Tuples, Lists, and Operations

## Tuples in Python

- **Definition**: Tuples are immutable sequences of values.
- **Example**:

```python
tup = (87, 32, 22, 77, 22)
print(tup)       # Output: (87, 32, 22, 77, 22)
print(tup[1])    # Output: 32
```

### Empty Tuple

```python
tup = ()
print(tup)       # Output: ()
print(type(tup)) # Output: <class 'tuple'>
```

### Single Element Tuple

- A comma is required for single-element tuples.

```python
tup = (1,)
print(tup)       # Output: (1,)
```

Without a comma:

```python
tup = (1)
print(tup)       # Output: 1 (integer)
```

### Tuple Slicing

```python
tup = (1, 2, 3, 4)
print(tup[1:3])  # Output: (2, 3)
print(tup[:3])   # Output: (1, 2, 3)
print(tup[:])    # Output: (1, 2, 3, 4)
```

### Tuple Methods

- `index(value)`: Returns the index of the first occurrence of the value.
- `count(value)`: Returns the count of the specified value in the tuple.

```python
tup = (2, 1, 3, 1)
print(tup.index(1))  # Output: 1
print(tup.count(2))  # Output: 1
```

---

## Working with Lists

### Store Favorite Movies

1. **Using `append()`**:

```python
movies = []
movies.append(input("Enter your favorite movie 1: "))
movies.append(input("Enter your favorite movie 2: "))
movies.append(input("Enter your favorite movie 3: "))
print(movies)
```

2. **Direct Input**:

```python
movies = [
    input("Enter your favorite movie 1: "),
    input("Enter your favorite movie 2: "),
    input("Enter your favorite movie 3: ")
]
print(movies)
```

---

### Check for Palindrome in a List

```python
palindrome = [1, 2, 3, 4, 3, 2, 1]
palindrome_copy = palindrome.copy()
palindrome_copy.reverse()

if palindrome == palindrome_copy:
    print("Palindrome")
else:
    print("Not a palindrome")
```

---

### Count "A" Grades in a Tuple

```python
grades = ("c", "d", "A", "a", "b", "b", "a")
print(grades.count("a"))  # Output: 3
```

---

### Sort a List

```python
grades = ["c", "d", "a", "a", "b", "b", "a"]
grades.sort()
print(grades)  # Output: ['a', 'a', 'a', 'b', 'b', 'c', 'd']
```
```
