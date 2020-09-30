import calculations
import math


def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)


initial_capital = ask_for_int_value("Type your initial capital")
rate_of_intrest = ask_for_int_value("Type your rate_of_intrest")
years = ask_for_int_value("How many years you want to keep investing")

final_value = calculations.final_value(initial_capital, rate_of_intrest, years)

print(f" After {years} your investment will be worth {final_value:.f}")
