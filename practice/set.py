collection = {1, 23, 4, 5, 6, 6, 0, "noushad"}
print(collection)
print(type(collection))
print(len(collection))

collection = set()
print(type(collection))

collection.add(1)
collection.add(2)
collection.add("apna college")
collection.add((2, 5, 1))
collection.remove(2)
print(collection)
collection.clear()
print(collection)

collection = {"hello", "world", "noushad", "ramim", "hello"}
print(collection.pop())

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts or figures"]
}
print(dictionary)

subjects = {
    "python", "math", "science", "english", "history",
    "geography", "bangla", "religion", "physical education"
}
print(len(subjects))

marks = {}
marks.update({"phy": input()})
marks.update({"chem": input()})
marks.update({"math": input()})
print(marks)

value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)
