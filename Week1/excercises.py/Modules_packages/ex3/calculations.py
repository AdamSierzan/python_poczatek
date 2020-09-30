import math


def final_value(initial_capital, rate_of_intrest, years):
    final_value = initial_capital * (1 + rate_of_intrest)
    final_value = math.pow(final_value, years)
    return final_value
