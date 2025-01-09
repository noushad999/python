# List - stores a set of values, similar to an array

# Example list
marks = [92.1, 99.2, 77.4, 22]
print(marks)
print(type(marks))
print(len(marks))  # Get the length of the list

# Lists can store different types of data
student = ["noushad", 88, 12, "dhaka"]
print(student[0])

student[0] = "hasan"  # Lists are mutable
print(student)

# List slicing
marks = [99, 12, 42, 44.5, 99.1]
print(marks[1:4])  # Slicing from index 1 to 3
print(marks[1:])   # Slicing from index 1 to the end
print(marks[:5])   # Slicing from the start to index 4
print(marks[:])    # Entire list

# Negative slicing
print(marks[-4:-1])  # Slicing with negative indices
print(marks[-3:])    # From the third last to the end
print(marks[:-2])    # From the start to the second last

# List methods
list = [2, 1, 4, 2, 1]

list.append(99)  # Add one element at the end
print(list)

list.insert(2, 11)  # Insert at index 2
print(list)

list.remove(2)  # Remove the first occurrence of 2
print(list)

list.pop(2)  # Remove the element at index 2
print(list)

list.sort()  # Sort the list in ascending order
print(list)

list.sort(reverse=True)  # Sort the list in descending order
print(list)

list2 = ["noushad", "jahan", "ramim"]  # Sorting strings alphabetically
list2.sort(reverse=True)
print(list2)

list.reverse()  # Reverse the list
print(list)
