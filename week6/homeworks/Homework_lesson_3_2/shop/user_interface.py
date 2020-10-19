from errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from order import Order
from store import Store


def handle_customer():
    say_hello()
    order = init_order()
    while want_more_products():
        add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
    print_order_summary(order)


def say_hello():
    print("Witaj w naszym sklepie!")


def init_order():
    
    first_name = input("Podaj swoje imię")
    last_name = input("Podaj swoje nazwisko")
    return Order(first_name, last_name)
    # : Pobierz imię i nazwisko i zwróć to czego oczekuje wołający w handle customer


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(f"{input_error} Proszę upenij się, że wpisaujesz numer")
        return
        # : Obsłuż błędne dane podane przez użytkownika

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except:
        raise NotValidInput(f"Podany numer musi być liczbą")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"Podaj odpowiedni index produktu, mieszczący się w przedziale 0 - {max_index}")
    
    return product_index
    # : Zamień napis na liczbę i upewnij się, że jest poprawna (czyli, że na pewno taki indeks będzie na liście)
    # : W przypadku błędu rzuć odpowiedni wyjątek, który oczekiwany jest w metodzie "wyżej"


def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except:
        raise NotValidInput(f"Liczba sztuk musi być liczbą")

    if quantity < 1:
        raise NotValidInput(f"Liczba sztuk musi wynosić conajmniej jeden")
    
    return quantity
        # : Zamień napis na liczbę i upewnij się, że jest większa od 0, w razie czego rzuć odpowiedni wyjątek


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")
