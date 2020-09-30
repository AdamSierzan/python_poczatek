# Implement the function that will calculate lenght of the 3 side of a triangle
# based on the values you have
# Formula is:
# C = root(a ^ 2 + b ^ 2 )
# Use math library
# a) sqrt(x) root of x
# b) pow(x,y) gets x to the root y


import math


def hypotenuse_calc(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


c = hypotenuse_calc(5, 3)

print(f"Hypotenuse lenght is {c}")
