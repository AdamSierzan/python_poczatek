# To make better use of class, we should add some characteristics to it
#  To do it we use constructor

class Student:

    # constructor will be called while we create object
    def __init__(self):
        print("We create a new object!")

if __name__ == "__main__":
    student = Student()

# Constructor's work is to define and initialize state of object

class Student_2:

    def __init__(self):
        self.first_name = "Adam"
        self.last_name = "Sierzan"
        self.age = 27

def run_example():
    student = Student_2()

    print(student.first_name)  
    print(student.last_name)  

    # We can also modify object
    student.last_name = "Sierzko"
    print(student.last_name)  



if __name__ == "__main__":
    run_example()