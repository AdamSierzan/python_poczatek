
class Student:

    # constructor can gain some arguments
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    

    # We can pass objects as arguments to function

def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


    # We can also modify object state(side effect)

def promote_student(student):
    student.promoted = True


def run_example():
    student = Student(first_name="Jack", last_name="Beck")
    print_student(student)

    other_student = Student("Pablo", "Diego")
    print_student(other_student)


    promote_student(student)
    print_student(student)
run_example()