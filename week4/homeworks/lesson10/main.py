from apple import Apple
from potato import Potato
# import random
# from order import Order
# # from data_generator import generate_order_elements
# from discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount
# from product import Product, Best_Before
# from ExpressDelivery import ExpressDelivery



def run_homework():
  
    green_apple = Apple(species_name="Green", size="M", price = 4.4)

    print(green_apple)

    old_potato = Potato(species_name = "Old", size="L", price=5)

    print(old_potato)




if __name__ == '__main__':
    run_homework()
