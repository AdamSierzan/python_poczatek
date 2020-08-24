
import random
from order import Order
from data_generator import generate_order_elements
from discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount
# from product import Product, Best_Before
# from ExpressDelivery import ExpressDelivery


def run_homework():
  

    elements_for_order = generate_order_elements()
    ten_percentage_discount = PercentageDiscount(discount_percentage=10)
    houndret_pln_discount = AbsoluteDiscount(value_of_discount=100)

    brand_new_order = Order(      
      client_first_name = "Adam",
      client_last_name = "Sierzan",
      order_elements= elements_for_order,
    )

    order_with_percentage_discount = Order(
      client_first_name = "John",
      client_last_name = "Wick",
      order_elements = elements_for_order,
      discount_policy = ten_percentage_discount,
    )


    order_with_value_discount = Order(
      client_first_name = "Jack",
      client_last_name = "Ripper",
      order_elements = elements_for_order,
      discount_policy = houndret_pln_discount,
    )
    
    
    print(order_with_percentage_discount)
    print(order_with_value_discount)
    print(brand_new_order)






    
  


if __name__ == '__main__':
    run_homework()
