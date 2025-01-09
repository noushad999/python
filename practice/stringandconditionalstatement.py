# String is a data type that stores a sequence of characters

# Defining strings
str1 = "this is a string"  # Most common way to define a string
str2 = 'this is also string'
str3 = '''this is also a string'''  # Triple quotes for multi-line strings
str4 = """this is also a string"""

str1 = "this is a string \n.we are creating this"
print(str1)

# Operations on strings

# Concatenation: Adding two or multiple strings
str1 = "noushad"
str2 = "ramim"
finalstr = str1 + str2
print(finalstr)

# Length of a string
finalstr = str1 + " " + str2
print(len(finalstr))  # 13 because space is also counted

# String indexing - Access a particular character from a string
str = "noushad ramim"
print(str[7])

# Slicing - Access part of a string
str = "md noushad jahan ramim"
print(str[3:8])  # noush
print(str[:8])   # md noush
print(str[3:])   # noushad jahan ramim
print(str[:])    # md noushad jahan ramim
print(str[::2])  # m osa aa ai
print(str[5:len(str)])  # ushad jahan ramim

# Negative indexing - Access characters from the end of the string
str = "apple"  # Starts from -1 to -5
print(str[-2])  # l
print(str[-5:-1])  # appl
print(str[-5:])  # apple

# String functions
str = "i am a coder"
print(str.endswith("er"))  # True
print(str.startswith("am"))  # False
str = str.capitalize()  # Capitalize the first character
print(str)  # I am a coder
print(str.replace("coder", "developer"))  # Replace "coder" with "developer"
print(str.find("a"))  # Find the index of the first occurrence of "a"
print(str.find("a", 9))  # Find "a" starting from index 9
print(str.find("x"))  # Return -1 because "x" is not in the string
print(str.count("a"))  # Count the occurrences of "a"

# Practice 1: Input user's first name and print its length
name = input("Enter your name: ")
print("Your name length is", len(name))

# Practice 2: Find the occurrence of "$" in a string
str = "my $ name $ is $ noushad $"
print("$ counts:", str.count("$"))
