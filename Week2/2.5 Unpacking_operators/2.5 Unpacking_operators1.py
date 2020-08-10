# Użycie unpacking operators powzwala nam na przekazanie
# dowolnej liczby argumentów pozycyjnych. *args pozwala nam na użycie 
# takiej ilości argumentow pozycyjnych jakiej chcemy.
# Te argumenty maja klase "tuple".


def calculate_sum_via_list(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


# def calculate_sum_via_args(*args):
#     # print(type(args))
#     result = 0
#     for number in args:
#         result += number
#     return result


def run_example():
    numbers = [1, 2, 3, 4, 5, 6]
    result = calculate_sum_via_list(numbers)
    print(result)

    # result = calculate_sum_via_args(1, 2, 3, 4, 5, 6)
    # print(result)

    # result = calculate_sum_via_args(5, 6)
    # print(result)


if __name__ == '__main__':
    run_example()