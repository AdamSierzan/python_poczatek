# Możliwość wywołania takiej funkcji przkazując jej różną ilość argumentóœ
# przydaje się w OOP, szczególnie przy dziedziczeniu.
# Stosując unpacking operators należy pamiętać o kolejności
# przekazywanych argumentów. Najpierw przekazujemy argumenty, potem argumenty 
# pozycyjne, a nastepnie nazwane.
# unpacking operators mozemy zastosowac nie tylko definiujac  przyjmowane przez funkcje parametry, ale 
# rowniez do innych celow. Operator * możemy uzyć do rozpakowania elementow z jednej listy.



def calculate_sum_via_args(*args):
    result = 0
    for number in args:
        result += number
    return result


def add_two_numbers(first, second):
    ''' Funkcja przyjmujaca dwa normalne 
        argumenty'''
    return first + second
    


def run_example():
    numbers = [1, 2, 3, 4, 5, 6]


    # Gdybyśmy użyli argumentu bez * python nie 
    # mógłby wykonać polecenia

    # result = calculate_sum_via_args(numbers)
    # print(result)

    # Aby uzyc listy, jako argumentów, musimy ją 
    # rozpakowac. Do tego używamy * jak poniżej
    result = calculate_sum_via_args(*numbers)
    print(result)


    # To samo możemy zrobić, aby rozpakowac funkcje 
    # ktora ma dwa zwykłe argumenty 

    two_numbers = [10, 30]
    result = add_two_numbers(*two_numbers)
    print(result)


    # Unpacking operators uzywamy rozniez do polaczenia
    # dwoch list

    combined_numbers = [*numbers, *two_numbers]
    print(combined_numbers)



if __name__ == '__main__':
    run_example()