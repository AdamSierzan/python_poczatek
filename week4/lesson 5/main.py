
import random
from order import Order
from data_generator import generate_order_elements
from discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount
# from product import Product, Best_Before
# from ExpressDelivery import ExpressDelivery
from products_delivery import products_delivery

def run_homework():
  
  needed_products =  [
    "ciasto", 
    "chleb", 
    "woda", 
    "piwo", 
    "cukier", 
    "ser", 
    "pasztet", 
    "bułki", 
    "cebula", 
    "jabłka"]  

  recieved_products = []

  while not set(needed_products) == set(recieved_products):
    new_products = products_delivery()
    recieved_products += new_products
    print(f"Otrzymano {new_products}")
    missing_products = set(needed_products).difference(recieved_products)
    print(f"Brakuje {missing_products}")

  print(f"Łącznie otrzymano {set(recieved_products)set(range(0,11))})


if __name__ == '__main__':
    run_homework()
