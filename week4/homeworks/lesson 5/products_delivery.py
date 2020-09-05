import random


def products_delivery():
    available_products = ["ciasto", 
    "chleb", 
    "woda", 
    "piwo", 
    "cukier", 
    "ser", 
    "pasztet", 
    "bułki", 
    "cebula", 
    "jabłka"]



    return [available_products[random.randint(0,9)] for _ in range(5)]

print(products_delivery())