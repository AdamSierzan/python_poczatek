
import random
from order import Order
from data_generator import generate_order_elements



def run_homework():
    first_name = "Mikołaj"
    last_name = "Lewandowski"
    
    order_elements = generate_order_elements(120)
    normal_order = Order(first_name, last_name, order_elements)

    # for element in normal_order.order_elements:
    #     print(element)
    print(normal_order.total_price)
    print(normal_order)



if __name__ == '__main__':
    run_homework()
