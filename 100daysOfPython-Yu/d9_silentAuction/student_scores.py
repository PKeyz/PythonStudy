student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the Code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your Code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] in range(91,100):
        grade_value = "Outstanding"
        student_grades[key] = grade_value
    elif student_scores[key] in range(81,90):
        grade_value = "Exceeds Expectations"
        student_grades[key] = grade_value
    elif student_scores[key] in range(71,80):
        grade_value = "Acceptable"
        student_grades[key] = grade_value
    else:
        grade_value = "Fail"
        student_grades[key] = grade_value

# 🚨 Don't change the Code below 👇
print(student_grades)

"""
Experimenting with lists dicts , lists in dicts, dicts in lists

travel_log = {
    "France": {
        "cities_visited": ["Paris","Lyon"],
        "cities_liked" : ["the more sun the better!"]
    },
    "Germany":{
        "cities_visited": ["Berlin","Frankfurt","Chemnitz"]
    },
}

print(travel_log)

"""