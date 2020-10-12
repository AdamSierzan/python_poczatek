
# W przykładzie tym mamy sytuację, w której błędy z funcji handle_even_number
# łapiemy w funcji run_example i robimy z nimi nic
# nazywane jest to wyciszaniem wyjątków 
# tego typu jest antywzorcem 
 

class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest poprawną liczbą")

    if number % 2 != 0:
        raise NumberParsingError("To nie jest liczba parzysta!")

    print(f"Dzięki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number_str = input("Podaj liczbę parzystą: ")

    try:
        handle_even_number(number_str)
    except NumberParsingError:
        pass


if __name__ == '__main__':
    run_example()
