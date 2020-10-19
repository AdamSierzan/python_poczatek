Try i except pozwala nam złapać i obsłużyć wyjątki
Oprócz tych dwóch bloków, istnieją jeszcze dwa słowa kluczowe
Finally oraz else


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
    finally:
        print("Błędu nie złapiemy ale wykonamy to zawsze")



    # Jeśli złapiemy wyjątek i dołożymy sekcję finally
    # ale w sekcji except wyrzucimy wyjątek ponownie 
    # to finally się wykona
    # try:
    #     handle_even_number(number_str)
    # except NumberParsingError as error:
    #     print(error)
    #     raise error
    # finally:
    #     print("Błędu nie złapiemy ale wykonamy to zawsze")

    # Jeśli chcemy by jakiś kod był zrealizowany zawsze
    # to zamiast finally możemy wykonać try except. Powieli to kod
    # 
    # try:
    #     handle_even_number(number_str)
    # except NumberParsingError as error:
    #     print("Błędu nie złapiemy ale wykonamy to zawsze")
    #     print(error)
    # print("Błędu nie złapiemy ale wykonamy to zawsze")



if __name__ == '__main__':
    run_example()
