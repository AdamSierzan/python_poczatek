
# tutaj tworzymy własny typ wyjątku
# łapiemy type error w funkcji i wyrzucamy 
# własny wyjątek
class NumberParsingError(Exception):
    pass


def handle_even_number(number):
    # łapiemy wyjątek w funkcji i rzucamy własny wyjątek
    # w ten sposób możemy zagregować różnie niskopoziomowe wyjątki
    # zastąpić je bardziej ogólnym interfejsem i dzięki temu funcja nie
    # musi się zastanawiać nad tym czy to błąð typu czy wartości
    # przekazujemy informacje, że coś poszło nie tak   i
    # wyrzucony będzie nasz komunikat

    try:
        if number % 2 != 0:
            raise NumberParsingError("To nie jest liczba parzysta!")
    except TypeError:
        raise NumberParsingError("Przekazany argument nie jest poprawną liczbą")

    print(f"Dzięki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number = input("Podaj liczbę parzystą: ")
    if number.isnumeric():
        number = int(number)

    try:
        handle_even_number(number)
    except NumberParsingError as error:
        print(f"Coś poszło nie tak: {error}")



if __name__ == '__main__':
    run_example()
