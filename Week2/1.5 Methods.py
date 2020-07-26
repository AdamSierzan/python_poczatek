# With the costructor we defiend data, status of the object
# Methods are functions defiend in classes

# It has at least one argument
# self

# This arguemnt provides us acces to the current instance of the object
# That is called in function

# Constructor is also a method, but of the special type

class Student:

    def __init__(self, name):
        self.name = name


    def print_something(self):
        print("It's me, method of Student")

def run_example():
    student = Student(name="Adam")
    student.print_something()


print(run_example())