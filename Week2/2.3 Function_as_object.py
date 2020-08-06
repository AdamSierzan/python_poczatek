# W pythonie wszystko możemy uznać za obiekt
# Także funkcję, jest to niezwykle przydatne gdyż możemy ją
# póżniej przypisać do zmiennej


def say_hello_name(name):
    print(f"hello {name}!")


def run_example():
    hello_name = say_hello_name
    hello_name("Adam")

run_example()

# Taka funkcja może też zwracać jakiś wynik


def calculate_something(some_value, other_value):
    return some_value + other_value


def run_example2():


    calculation = calculate_something
    result = calculation(10, 30)
    print(result)


run_example2()


import random


def say_hello():
    print("Hello World!")


def say_good_bye():
    print("Good bye!")


def randomize_func(first_func, second_func):
    number = random.randint(1, 2)
    if number == 1:
        return first_func
    return second_func


def run_example3():
    hello_or_good_bye = randomize_func(say_hello, say_good_bye)
    hello_or_good_bye()

run_example3()



# Popularnym wykorzystaniem funckji jako argumentu jest reaizcj tzw. domkniecia
# Czyli niejako wstrzykniecia roznych wariantow logiki biznesowej do wnetrza jakiegos
# innego algorytmu
# Przykładem może być sortowanie elementów, gdzie specjalny argument pozwoli name
# przekazac funkcje, ktora bedzie nasza wlasna implementacja logiki porownywania

