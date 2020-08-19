
import random
from order import Order
from data_generator import generate_order_elements
from product import Product, Best_Before
from ExpressDelivery import ExpressDelivery


def run_homework():
  

    elements_for_order = generate_order_elements()

    brand_new_order = ExpressDelivery(      
      date_of_delivery = "24.05.2030",
      client_first_name = "Adam",
      client_last_name = "Sierzan",
      order_elements= elements_for_order,
    )
    print(brand_new_order)


    
  


if __name__ == '__main__':
    run_homework()
