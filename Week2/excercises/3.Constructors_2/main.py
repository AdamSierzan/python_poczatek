



from Apple import Apple
from Orders import Order, print_order
from Potato import Potato
from Products import Product, print_product


def run_homework():

    ligol = Apple(name="ligol", size="S", price_for_kg=5)
    ambrosia = Apple(name="ambrosia", size="M", price_for_kg=3)
    candy = Product(" candy", " sweets", 20)
    bread = Product(" 
    bread", " pastries", 25)


    empty_order = Order("John", "Lewy", [candy, bread])
    order = Order("Jack", "Reaper", [bread, candy, candy])
    
    print_order(order)


run_homework()
