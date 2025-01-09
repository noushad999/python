# Python Lists

## Lists in Python

A list is a collection of values, similar to an array, and can store multiple items in a single variable.

```python
marks = [92.1, 99.2, 77.4, 22]
print(marks)  # Output: [92.1, 99.2, 77.4, 22]
print(type(marks))  # Output: <class 'list'>
```

## Accessing List Elements

Lists are indexed, and elements can be accessed using the index.

```python
student = ["noushad", 88, 12, "dhaka"]
print(student[0])  # Output: "noushad"
```

## Modifying List Elements

Lists are mutable, meaning you can change their elements.

```python
student[0] = "hasan"
print(student)  # Output: ['hasan', 88, 12, 'dhaka']
```

## List Slicing

You can extract parts of a list using slicing.

```python
marks = [99, 12, 42, 44.5, 99.1]
print(marks[1:4])  # Output: [12, 42, 44.5]
print(marks[1:])  # Output: [12, 42, 44.5, 99.1]
print(marks[:5])  # Output: [99, 12, 42, 44.5, 99.1]
print(marks[-4:-1])  # Output: [12, 42, 44.5]
print(marks[-3:])  # Output: [42, 44.5, 99.1]
print(marks[:-2])  # Output: [99, 12, 42]
```

## List Methods

### `append()`

Adds an element to the end of the list.

```python
list = [2, 1, 4, 2, 1]
list.append(99)
print(list)  # Output: [2, 1, 4, 2, 1, 99]
```

### `sort()`

Sorts the list in ascending order.

```python
list.sort()
print(list)  # Output: [1, 1, 2, 2, 4, 99]
```

### `sort(reverse=True)`

Sorts the list in descending order.

```python
list.sort(reverse=True)
print(list)  # Output: [99, 4, 2, 2, 1, 1]
```

### `insert()`

Inserts an element at a specific index.

```python
list.insert(2, 11)
print(list)  # Output: [2, 1, 11, 4, 2, 1, 99]
```

### `remove()`

Removes the first occurrence of a value.

```python
list.remove(2)
print(list)  # Output: [1, 11, 4, 2, 1, 99]
```

### `pop()`

Removes an element at a specific index.

```python
list.pop(2)
print(list)  # Output: [1, 11, 2, 1, 99]
```

## Lists vs Strings

Strings are immutable (cannot be changed), while lists are mutable (can be changed).

