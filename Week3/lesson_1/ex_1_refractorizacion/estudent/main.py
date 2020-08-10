
from data_generator import generate_students
from school import School


def run_example():
    students = generate_students()
    school = School(name="Hogwart", students=students)
    print(school)


if __name__ == '__main__':
    run_example()
