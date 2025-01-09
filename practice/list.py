#list - stores set of value,kinda like array



# marks=[92.1,99.2,77.4,22]
# print(marks)
# print(type(marks))
# # print(marks(0)) #using this syntex we can simply get access to the value of the list
# print(len(marks))
# #we can store different type of data in the list
#strings are immutable but list are mutable

# student=["noushad",88,12,"dhaka"]
# print(student[0])

# student[0]="hasan"
# print(student)

#list slicing

# marks=[99,12,42,44.5,99.1]
# # print(marks[1:4])
# # print(marks[1:])
# # print(marks[:5])
# # print(marks[ : ])

# #negitive slicing
# print(marks[-4:-1])
# print(marks[-3:])
# print(marks[:-2])

#list method

list=[2,1,4,2,1]

list.append(99) #add one element at the end
print(list)

# list.sort() #sort the list in ascending order
# print(list)


# list.sort(reverse=True) #sort the list in ascending order
# print(list)

# list2=["noushad","jahan","ramim"] #for string it will sort in alphabetical order
# list2.sort(reverse=True)
# print(list2)

# list.reverse()
# print(list)

list.insert(2,11) #insert method takes two argument first one is the index and second one is the value
print(list)

list.remove(2) #remove first occuerence of the value
print(list)

list.pop(2)
print(list)
