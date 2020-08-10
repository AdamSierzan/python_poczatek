# Zadanie nr 3
# Wygeneruj dwie listy zawierające losowe liczby całkowite i połącz je w jedną wykorzystując operator *.
import random

def randon_number_list_generator():
    list_of_nums = []
    for i in range(4):
        numbers = random.randint(1,10)
        list_of_nums.append(numbers)
    return list_of_nums

def run_example():
    random_numbers_1 = randon_number_list_generator()
    random_numbers_2 = randon_number_list_generator()
    numbers_together = [*random_numbers_1, *random_numbers_2]
    print(numbers_together)
run_example()

# print(randon_number_list_generator())