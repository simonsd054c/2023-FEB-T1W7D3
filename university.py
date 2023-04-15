from pprint import pprint

'''
{
    "sydney": [
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer or tutor"
            }
        },
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer or tutor"
            }
        }
    ],
    "melbourne": [
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer or tutor"
            }
        },
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer or tutor"
            }
        }
    ],
    "brisbane": [
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer or tutor"
            }
        },
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer or tutor"
            }
        }
    ]
}
'''

university = {
    "sydney": [
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer"
            }
        },
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer"
            }
        }
    ],
    "melbourne": [
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer"
            }
        },
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer"
            }
        }
    ],
    "brisbane": [
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer"
            }
        },
        {
            "class_name": "className",
            "teacher": {
                "name": "teacherName",
                "role": "lecturer"
            }
        }
    ]
}

campus = 0

while (not (campus > 0 and campus < 4)):
    campus = int(input(
        """Which campus do you want to add the class to?
        (Press 1 for Sydney, 2 for Melbourne and 3 for Brisbane): """
    ))

class_name = input("Enter class name: ")

teacher_name = input("Enter teacher's name: ")

teacher_role = 0

while (not (teacher_role > 0 and teacher_role < 3)):
    teacher_role = int(
        input("Enter teacher's role. (Enter 1 for lecturer and 2 for tutor): "))

campus_names = ("sydney", "melbourne", "brisbane")
teacher_role_names = ("lecturer", "tutor")

campus_location = campus_names[campus - 1]
# print(teacher_role_names[teacher_role - 1])

university[campus_location].append({
    "class_name": class_name,
    "teacher": {
        "name": teacher_name,
        "role": teacher_role_names[teacher_role - 1]
    }
})

pprint(university)