
# Możemy przenieść odpowiedzialność za przetworzenie tych danych z zewnątrz 
# do wnętrza funcji Handle_even_number


class NumberParsingError(Exception):
    pass


def handle_even_number(number_str):
    # jeśli przyjmiemy, że funcja odbiera stringa i dalej jest odpowiedzialna 
    # za przetworzenie go wewnątrz siebie
    try:
        number = int(number_str)
    except ValueError:
        raise NumberParsingError("Przekazany argument nie jest poprawną liczbą")
    # funcja przetwarza na liczbę, jeśli to sie nie udaje to
    # wyrzuca wyjątek


    # jeśli się uda to leci dalej
    if number % 2 != 0:
        raise NumberParsingError("To nie jest liczba parzysta!")

    print(f"Dzięki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number_str = input("Podaj liczbę parzystą: ")

    try:
        handle_even_number(number_str)
    except NumberParsingError as error:
        print(f"Coś poszło nie tak: {error}")


if __name__ == '__main__':
    run_example()
