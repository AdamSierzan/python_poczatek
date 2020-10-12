
def run_example():

    try:
        print("Przed rzuceniem wyjątku")
        # instancja klasy type error
        raise TypeError("Coś poszło nie tak...") 
        print("To się nie wydarzy")
    # Tutaj do części except dodaliśmy as error
    # as error pozwala nam chwycic obiekt
    # w ten sposób możemy dobrać się do tego błedu
    # który został stworzony
    except TypeError as error:
        print(f"Wyjątek zawiera informacje: {error}")

    print("I program będzie przetwarzany dalej :)")


if __name__ == '__main__':
    run_example()
