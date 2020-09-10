# from apple import Apple
# from potato import Potato

# import random
from order import Order
from data_generator import generate_order_elements
# from discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount
# from product import Product, Best_Before
# from ExpressDelivery import ExpressDelivery



def run_homework():
  
    some_order_elements = generate_order_elements()
    my_order = Order("Bob", "Kowalski", order_elements=some_order_elements)
    print(my_order)



if __name__ == '__main__':
    run_homework()
