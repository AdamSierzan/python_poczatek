# Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby całkowite z przedziału od 1 do 10.
# Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).
# Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio pierwszej, drugiej i trzeciej wylosowanej liczby całkowitej.

import random
import math

float_nums = []
for _ in range(6):
    float_nums.append(random.uniform(-20,20))
print(float_nums)


int_nums = []
for _ in range(3):
    int_nums.append(random.randint(1,10))
print(int_nums)


for _ in float_nums:
    if _ == float_nums[0]:
        print(round(_))
    if _ == float_nums[1]:
        print(math.ceil(_))
    if _ == float_nums[2]:
        print(math.floor(_))
    if _ == float_nums[3]:
        print(_**int_nums[0])
    if _ == float_nums[4]:
        print(pow(_,int_nums[1]))
    if _ == float_nums[5]:
        print(math.pow(_,int_nums[2]))
    else:
        continue