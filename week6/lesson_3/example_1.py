# 
def run_example():

    # w bloku try umieszczamy wyjątek, który potencjalnie 
    # nasz program może wyrzucić
    try:
        print("Przed rzuceniem wyjątku")
        raise TypeError("Coś poszło nie tak...")
        print("To się nie wydarzy")
    # w sekcji except specyfikujemy jaki typ wyjątku nas interesuje
    #  w tym przypadku wyjątku typu TypeError, w przyadku złapania 
    # tego wyjątku, jego kod się wykona
    except TypeError:
        print("Ale złapaliśmy wyjątek")

    print("I program będzie przetwarzany dalej :)")

    # Fakt złapania wyjątku, powoduje że program nie przerywa
    # działania


if __name__ == '__main__':
    run_example()
