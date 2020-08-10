import random

class Product:
    
    def __init__(self, name, category_name, price):
        self.name = name 
        self.category_name = category_name
        self.price = price


class Order:
    
    def __init__ (self, name, last_name, list_of_products = None):
        self.name = name
        self.last_name = last_name
        if list_of_products is None:
            list_of_products = []
        self.list_of_products = list_of_products
        
        total_price = 0
        
        for product in list_of_products:
            total_price += product.price
        self.total_price = total_price


class Apple:
    
    def __init__(self, name, size, price_for_kg):
        self.name = name
        self.size = size
        self.price_for_kg = price_for_kg

class Potato:
    
    def __init__(self, name, size, price_for_kg):
        self.name = name
        self.size = size
        self.price_for_kg = price_for_kg

def run_homework():

    ligol = Apple(name="ligol", size="S", price_for_kg=5)
    ambrosia = Apple(name="ambrosia", size="M", price_for_kg=3)
    candy = Product("candy", "sweets", 20)
    bread = Product("bread", "pastries", 25)


    empty_order = Order("John", "Lewy", [candy, bread])
    order = Order("Jack", "Reaper", [bread, candy, candy])
    third_order = random_order()
    print_order(third_order)

  

    

def random_order():

    number_of_product = random.randint(1,20)
    products = []
    for product_number in range(number_of_product):
        name = f"Product{product_number}"
        category_name = f"Other"
        price = random.randint(1,20)
        product = Product(name, category_name, price)
        products.append(product)
    
    order = Order("Adam", "Sierza", products )
    return order


def print_product(product):
    print(f"Product name{product.name} | Category{product.category_name} | Price{product.price}")

def print_order(order):
    print(f"Order of {order.name} {order.last_name}")
    print(f"For {order.total_price}")
    print(f"Client ordered:")
    for product in order.list_of_products:
        print_product(product)
    print()

run_homework()
