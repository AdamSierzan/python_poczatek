
import random
from order import Order
from data_generator import generate_order_elements



def run_homework():
    first_name = "Mikolaj"
    last_name = "Lewandowski"

    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    print(normal_order)

    new_elements = generate_order_elements(3)
    normal_order.order_elements = new_elements
    print(normal_order)

    too_many_elements = generate_order_elements(1222)
    normal_order.order_elements = too_many_elements
    print(normal_order)


if __name__ == '__main__':
    run_homework()
