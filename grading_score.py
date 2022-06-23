student_score = {
    "harry": 81,
    "rohan": 78,
    "rachit": 99,
    "rosan": 74,
    "abhishek": 62
}
# don't change the code above

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: write your code below to add the grades to student_grades.
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "exceeds exceptations"
    elif score > 70:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "fail"

print(student_grades)

#  nesting lists and dictionary
travel_log = {
    "uttar_pradesh": {"citi_visited": ["kanpur", "agra", "allahabad"], "total_visits": "12"},
    "maharastra": ["mumabai ", "pune", "thane"]
}
print(travel_log)
