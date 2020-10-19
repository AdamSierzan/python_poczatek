import data_generator
from errors import LogicError, PlacesLimitError
# from school import School
from student import Student

# W tym przypadku będziemy łapać błędy z zewnątrz za pomocą try/except
def run_example():
     student = Student(first_name="Bob", last_name="Bobowski")
     try:
         print(student.grades_avg)
     except LogicError as error:
         print(f"Błąd: {error}")

    # students = data_generator.generate_students(number_of_students=250)
    # school = School(name="Mała szkoła", students=[])
    # try:
    #     school.students = students
    # except PlacesLimitError as error:
    #     print(f"Limit miejsc wynosi: {error.places_limit}")


if __name__ == '__main__':
    run_example()
