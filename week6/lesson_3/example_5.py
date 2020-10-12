
def handle_even_number(number):
    
    #funkcja sprawdza czy liczba jest parzysta
    # jak nie jest to rzuca nam value error
    if number % 2 != 0:
        raise ValueError("To nie jest liczba parzysta!")
    # jak jest parzysta to wykonuje ten kod
    print(f"Dzięki! Wprowadzona liczba podzielona przez 2 to: {number / 2}")


def run_example():
    number = input("Podaj liczbę parzystą: ")
    if number.isnumeric():
        number = int(number)


    # wywołujemy obsłużenie liczby parzystej
    # ważne jest tutaj, że na sekcje try możemy
    # wstawić więcej niż jeden typ wyjątku
    try:
        handle_even_number(number)
    except TypeError as error:
        print(f"Coś nie tak z typem: {error}")
    except ValueError as error:
        print(f"Zła wartość: {error}")

# Możemy także użyć Exception aby złapać obydwa typy błędów,
# w ten sposób nie przekazemy oddzielnych wiadomości dla każdefo
#  z błędów

# ważne jest również, że wyjątek nie jest rzucany w sekcji try
# przedostaje się do funcji i jest wywoływany stamtąd



if __name__ == '__main__':
    run_example()
