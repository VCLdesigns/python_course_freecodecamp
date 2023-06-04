"""
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# Improved code
for student in students:
    print(student)

# Improved Code
for i in range(len(students)):
    print(i + 1, students[i])
"""

""" 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=", ")
"""
students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russel Terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None}
]

for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=", ")
