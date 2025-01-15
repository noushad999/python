# File Handling in Python

## File Types
1. **Text Files**: `.txt`, `.doc`, `.docx`, `.pdf`, `.csv`
2. **Binary Files**: `.jpg`, `.png`, `.mp3`, `.mp4`, `.avi`, `.exe`, `.zip`, `.rar`

---

## Opening a File
**Syntax**:  
```python
f = open("file_name", "mode")
```
- `f`: File object  
- `file_name`: Name of the file  
- `mode`: Mode in which the file is opened  

---

## File Modes
- `r`: Read mode  
- `w`: Write mode (overwrites file)  
- `a`: Append mode (adds data to the end)  
- `x`: Exclusive mode (creates a file; raises error if file exists)  
- `t`: Text mode (default)  
- `b`: Binary mode  
- `+`: Update mode (read/write)

---

## File Reading
1. **Read Entire File**:  
   ```python
   f = open("demo.txt", "r")
   data = f.read()
   print(data)
   ```
2. **Read Line by Line**:  
   ```python
   f = open("demo.txt", "r")
   line1 = f.readline()
   line2 = f.readline()
   ```

---

## File Writing
1. **Overwrite File**:  
   ```python
   f = open("demo.txt", "w")
   f.write("hello duniya")
   f.close()
   ```
2. **Append to File**:  
   ```python
   f = open("demo.txt", "a")
   f.write("\nlalalalalal")
   f.close()
   ```

---

## Reading and Writing Modes
- `r+`: Read and write (does not truncate data).  
- `w+`: Write and read (truncates data).  
- `a+`: Append and read (does not truncate data).

---

## Using `with` Syntax
Automatically closes the file after operation:  
```python
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
```

---

## Deleting Files
Use the `os` module:  
```python
import os
os.remove("sample.txt")
```

---

## Practice Tasks

### 1. Create and Write to a File
```python
f = open("practice.txt", "w")
f.write("hi everyone\nwe are learning file i/o\nusing python\ni like programming in python")
f.close()
```

### 2. Replace Text in a File
Replace all occurrences of "java" with "python":  
```python
with open("practice.txt", "r") as f:
    data = f.read()
data = data.replace("java", "python")
with open("practice.txt", "w") as f:
    f.write(data)
```

### 3. Search for a Word
Check if "learning" is in the file:  
```python
with open("practice.txt", "r") as f:
    data = f.read()
    if "learning" in data:
        print("Yes")
    else:
        print("No")
