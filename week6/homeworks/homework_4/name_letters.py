class NumberParsingError(Exception):
    pass


def three_letters():
    name = input("Napisz trzy piersze litery swojego imienia: ")
    name_len = len(name)
    if name_len < 3 or name_len> 3:
        raise ValueError("Wprowadz 3 litery, nie więcej nie mniej")

    print("Dziękuję, dobranoc")
def run_example():
    try:
        three_letters()
    except ValueError as error:
        print(error)
    else:
        print("Coś wymyślasz")
    finally:
        print("Elo")

run_example()