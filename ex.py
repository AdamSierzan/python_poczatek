import random
expenditures = {}
expenditures_names = ["woda", "gaz", "prad"]

for expenditure in expenditures_names:
    expenditures[expenditure] = random.randint(1,100)
print(expenditures)