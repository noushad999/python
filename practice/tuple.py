# Tuples: Immutable sequence of values

# Tuple examples
tup = (87, 32, 22, 77, 22)
print(tup)
print(tup[1])

# Empty tuple
tup = ()
print(tup)
print(type(tup))

# Single element tuple
tup = (1,)
print(tup)

# Without a comma, it's considered an integer
tup = (1)
print(tup)

# String with and without a comma
tup = ("noushad",)
print(tup)

tup = ("noushad")
print(tup)

# Tuple slicing
tup = (1, 2, 3, 4)
print(tup[1:3])
print(tup[1:])
print(tup[:3])
print(tup[:])

# Tuple methods
tup = (2, 1, 3, 1)
print(tup.index(1))  # Return the index of the first occurrence of 1
print(tup.count(2))  # Count the occurrences of 2

# WAP to ask the user to enter the names of their three favorite movies and store them in a list
movies = []
movies.append(input("Enter your favorite movie 1: "))
movies.append(input("Enter your favorite movie 2: "))
movies.append(input("Enter your favorite movie 3: "))
print(movies)

# WAP to check if a list contains a palindrome of elements
palindrome = [1, 2, 3, 4, 3, 2, 1]
palindrome2 = palindrome.copy()
palindrome2.reverse()
if palindrome == palindrome2:
    print("Palindrome")
else:
    print("Not palindrome")

# WAP to count the number of students with the grade "A" in the following tuple
student = ("c", "d", "a", "a", "b", "b", "a")
print(student.count("a"))

# Store the above values in a list and sort them from 'a' to 'd'
student_list = ["c", "d", "a", "a", "b", "b", "a"]
student_list.sort()
print(student_list)
