# Class is a type of matrix. It defines the objects, and its functions.
# Class if a form for instances, otherwords objects.

class Student:
    pass

class Grade:
    pass

class School:
    pass


if __name__ == "__main__":
    student_mikołaj = Student()

    grade_a = Grade()
    grade_f = Grade()

    my_school = School()

    print(student_mikołaj)
    print(grade_a,grade_f)
    print(my_school)

    print("type(student_mikołaj):", type(student_mikołaj))
# We can see that we have created new type by defining class

# We can perform same actions on classes as on int, lists, dicts, etc.


    all_students = [Student(), Student(), Student()]
    print(all_students)

# We always use uppercase letters to name classes!!!









