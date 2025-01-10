# Python Sets and Practice Problems

## **Set Overview**
- **Definition**: A set is a collection of unordered, unique, and immutable elements.
- **Characteristics**:
  - Avoids duplicate elements.
  - Elements are **immutable**, but the set itself is **mutable** (can be modified after creation).
  - Written using **curly braces** `{}` or the `set()` function.

---

## **Examples and Set Operations**

### **Creating a Set**
```python
collection = {1, 23, 4, 5, 6, 6, 0, "noushad"}
print(collection)  # Duplicate elements are removed
print(type(collection))
print(len(collection))  # Total number of unique elements
```

### **Empty Set**
```python
collection = set()
print(type(collection))  # Output: <class 'set'>
```

### **Adding and Removing Elements**
```python
collection.add(1)
collection.add(2)
collection.add("apna college")
collection.add((2, 5, 1))  # Adding a tuple (immutable)

collection.remove(2)  # Remove an element
print(collection)

collection.clear()  # Clear all elements
print(collection)
```

### **Set Methods**
```python
collection = {"hello", "world", "noushad", "ramim", "hello"}
print(collection.pop())  # Removes a random element
```

### **Set Operations**
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))        # Union of two sets
print(set1.intersection(set2)) # Intersection of two sets
```

---

## **Practice Problems**

### **1. Storing Word Meanings**
```python
dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts or figures"]
}
print(dictionary)
```

### **2. Finding Required Classrooms**
- Given subjects: `"python", "math", "science", "english", "history", "geography", "bangla", "religion", "physical education," "python", "math"`

```python
subjects = {
    "python", "math", "science", "english", "history", 
    "geography", "bangla", "religion", "physical education"
}
print(len(subjects))  # Output: Total unique subjects
```

### **3. Store Marks of 3 Subjects**
```python
marks = {}
marks.update({"phy": input("Enter Physics marks: ")})
marks.update({"chem": input("Enter Chemistry marks: ")})
marks.update({"math": input("Enter Math marks: ")})
print(marks)
```

### **4. Store `9` and `9.0` Separately**
```python
value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)
