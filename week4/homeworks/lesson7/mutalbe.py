import random

def random_nums_to_set(numbers):

    number = (random.randint(0,10))
    numbers.add(number)
    return numbers 



def random_nums_to_frozenset(numbers):

    number = (random.randint(0,10))
    return  numbers.union({number})




def run_example():
    # numbers = set()
    numbers = frozenset()

    # while len(numbers) < 11:
    #     numbers.add(random.randint(0,10))
    # print(numbers)

    while len(numbers) < 11:
        numbers = random_nums_to_frozenset(numbers)
    print(numbers)


def run_example_remember_result():
    numbers = set()
    result = []
    
    while len(numbers) < 11:
        result.append(numbers)
        numbers = random_nums_to_frozenset(numbers)
    
    print(result)


run_example()
run_example_remember_result()


