# Python Dictionary Notes

## **Definition and Characteristics**
- **Dictionaries** store data in **key-value pairs**.
- They are collections that are:
  - **Unordered** (in Python < 3.7; ordered as of Python 3.7+).
  - **Changeable** (mutable; can be modified after creation).
  - Do **not allow duplicate keys** (latest value overrides earlier ones for duplicate keys).
- **Syntax:** Dictionaries are written using **curly braces** `{}`.

---

## **Examples and Usage**

### **Basic Structure**
```python
info = {
    "key": "value",
    "subject": ["math", "science", "english"],
    "topics": ("dictionaries", "list"),
    "name": "noushad",
    "learning": "python",
    "age": 24,
    "marks": 90,
    12.33: 2.3
}
```

### **Accessing Dictionary Items**
- Use the **key** to access values:
  ```python
  print(info["name"])  # Output: noushad
  print(info["topics"])  # Output: ('dictionaries', 'list')
  ```

### **Updating Values**
- Modify an existing key's value:
  ```python
  info["name"] = "noushad ramim"
  print(info["name"])  # Output: noushad ramim
  ```

### **Creating an Empty Dictionary**
- Add key-value pairs to an initially empty dictionary:
  ```python
  null_dict = {}
  null_dict["name"] = "noushad"
  print(null_dict)  # Output: {'name': 'noushad'}
  ```

---

## **Nested Dictionaries**
- A dictionary can contain another dictionary:
  ```python
  student = {
      "name": "kazi jetu",
      "subject": {
          "math": 90,
          "science": 80,
          "math": 96  # Latest value is retained
      }
  }
  ```
- Access nested values:
  ```python
  print(student["subject"]["math"])  # Output: 96
  ```

---

## **Dictionary Methods**

### **Keys and Values**
- Retrieve all keys:
  ```python
  print(student.keys())  # Output: dict_keys(['name', 'subject'])
  print(list(student.keys()))  # Convert keys to a list
  ```
- Retrieve all values:
  ```python
  print(student.values())  # Output: dict_values(['kazi jetu', {'math': 96, 'science': 80}])
  print(list(student.values()))  # Convert values to a list
  ```

### **Key-Value Pairs**
- Retrieve all key-value pairs:
  ```python
  print(student.items())  # Output: dict_items([('name', 'kazi jetu'), ('subject', {...})])
  print(list(student.items()))  # Convert pairs to a list
  ```
- Access a specific pair:
  ```python
  pairs = list(student.items())
  print(pairs[0])  # Output: ('name', 'kazi jetu')
  ```

### **Accessing Keys Safely**
- Direct key access (throws error if the key doesn’t exist):
  ```python
  print(student["name"])
  ```
- Safe key access using `get()` (returns `None` if key doesn’t exist):
  ```python
  print(student.get("name"))  # Output: kazi jetu
  ```

### **Updating a Dictionary**
- Add or update key-value pairs:
  ```python
  student.update({"city": "dhaka"})
  new_dict = {"name": "noushad"}
  student.update(new_dict)
  print(student)  # Output: {'name': 'noushad', 'subject': {'math': 96, 'science': 80}, 'city': 'dhaka'}
  ```

---
- **Length of a Dictionary:** Use `len()` to get the number of keys.
- **Duplicates:** If duplicate keys are present, the last value is retained.
- **Mutable Nature:** Dictionaries allow adding, updating, and deleting items dynamically.
```
