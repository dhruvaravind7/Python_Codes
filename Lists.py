from unicodedata import name


def Lists():
    students = ["Hermoine", "Harry", "Ron"]

    for i in range(len(students)):
        print(students[i])

def Dicts():
    students = [{"name": "Hermoine", "house": "Gryffindor", "patronus": "otter"},
                {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
                {"name": "Ron", "house": "Gryffindor", "patronus": "weasel"},
                {"name": "Draco", "house": "Slytherin", "patronus": None}]

    for i in students:
        print(i["name"], i["house"], i["patronus"], sep=", ")


Dicts()