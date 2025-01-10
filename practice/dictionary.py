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

print(info)

print(info["name"])
print(info["topics"])
print(info["subject"])

info["name"] = "noushad ramim"
print(info["name"])

null_dict = {}
null_dict["name"] = "noushad"
print(null_dict)

student = {
    "name": "kazi jetu",
    "subject": {
        "math": 90,
        "science": 80,
        "math": 96
    }
}

print(student["subject"]["math"])

print(student.keys())
print(list(student.keys()))

print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])

print(student["name"])
print(student.get("name"))

student.update({"city": "dhaka"})

new_dict = {"name": "noushad"}
student.update(new_dict)
print(student)
