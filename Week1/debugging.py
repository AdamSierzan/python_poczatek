# Debugging is a process of controlled running the programme to check it step by step
# Let's check some examples

def find_best_grade(grades_by_subject):
    best_grade = 0 
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade = best_grade_from_subject
        return best_grade


grades_data = {
    "History": [5,4,3,2],
    "Math": [4,5,4],
    "Physics": [2,4,5]

}

the_best_grade = find_best_grade(grades_data)
print(f"Best grade is {the_best_grade}")

# Debugging is used to delete bugs, most of the time the
# software is very complicated, and bugs can be hard to discover
# 