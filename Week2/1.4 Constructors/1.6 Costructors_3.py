# Create a constructors with the class of:
# Product(name, name of the catoegory, price)
# Order (name, last name, list of products, total price (sum of prices from list of products))
# Apple (name, size, price for kg)
# Potato (name, size, proce for kg)
# Create few objects of each class
# 
# Write a function that prints product and order
# Create a function fo generate random list of products
# Divide a projects into smaller modules, run it from main file


import random




# Objects can contain other objects

class School:
    def __init__(self, name, students):
        self.name = name 
        self.students = students

# Costructor could also has it's own logic
# def __init__(self, name, students):
        # self.name = name 
        # if len(students) > 10:
        #     students = students[:10]
        # self.students = students


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    
def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


def promote_student(student):
    student.promoted = True


# functions can return objects
def create_school_with_students(school_name):
    number_of_students = random.randint(1,20)
    students = []
    for student_number in range(number_of_students): 
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school



def run_example():
    school = create_school_with_students("Matrix")
    print(school)
    for student in school.students:
        print_student(student)

run_example()
