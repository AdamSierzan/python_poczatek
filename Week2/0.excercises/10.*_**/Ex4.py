# Zadanie nr 4
# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.

# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.


def names_and_age_dict(**kwargs):

    for name, age in kwargs.items():
        print(f"Name = {name}, Age= {age}")

def run_example():
    first_dict = {
        "Adam":27,
        "Julia":28,
        "Kasia":34
    }
    # names_and_age_dict(**first_dict)


    second_dict = {
        "Paweł":34,
        "Jacek":27,
        "Malwina":29
    }

    dicts_together = {**first_dict, **second_dict}
    print(dicts_together)

run_example()