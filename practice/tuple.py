#it create immutable sequence of values

# tup=(87,32,22,77,22)
# print(tup)
# print(tup[1])

#not allowed to change values
# tup[0]=0

# tup=()
# print(tup)
# print(type(tup))

# tup=(1,)
# print(tup)

#but if we dont use the comma then it will be considerd as a integer
# tup=(1)
# print(tup)

# tup=("noushad",)
# print(tup)

#but if we dont we dont use the comma then it will be considerd as a string
# tup=("noushad")
# print(tup)

# tup=(1,2,3,4)
# print(tup)
# print(type(tup))

#tuple slicing
# tup=(1,2,3,4)
# print(tup[1:3])
# print(tup[1:])
# print(tup[:3])
# print(tup[:])

# tup=(2,1,3,1)
# print(tup.index(1))#return the index of the given value
# print(tup.count(2))

#wap to ask the user to enter the name of their three favourite movies and store then in list

# movies=[]
# movie1=input("enter your favourite movie 1: ")
# movie2=input("enter your favourite movie 2: ")
# movie3=input("enter your favourite movie 3: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

#direct way
# movies.append(input("enter your favourite movie 1: "))
# movies.append(input("enter your favourite movie 2: "))
# movies.append(input("enter your favourite movie 3: "))
# print(movies)


#wap to check if a list contains a palindrome of elements (hint use copy() method)

# palindrome=[1,2,3,4,3,2,1]
# palindrome2=palindrome.copy()
# palindrome2.reverse()
# if palindrome==palindrome2:
#     print("palindrome")
# else:
#     print("not palindrome")

#write to count the number of students with the grade "A" in the following tuple
#("c","d","A","a","b","b","a")

# student=("c","d","a","a","b","b","a")

# print(student.count("a"))

#store the above values in a list and sort them from a to d
# student=["c","d","a","a","b","b","a"]
# student.sort()
# print(student)