#!/usr/bin/env python3
def average(students, class_name):
    for student in students:
        total = 0
        for score in student.values():
            total += score
        avg = total / len(student)
        print(f"Average score for {class_name}: {avg:.2f}")


class_3B = [{
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
    }]

class_3C = [{
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
    }]

average(class_3B, "class_3B")
average(class_3C, "class_3C")
