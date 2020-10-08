# from apple import Apple
# from potato import Potato

# import random
from order import Order
from data_generator import generate_order_elements, generate_product, generate_quantity
# from discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount
# from product import Product, Best_Before
# from ExpressDelivery import ExpressDelivery



def run_homework():
  
    order_elements_on_limit = generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)
    print(order_on_limit)

    product = generate_product()
    quantity = generate_quantity()
    order_on_limit.add_product_to_order(product, quantity)

if __name__ == '__main__':
    run_homework()
