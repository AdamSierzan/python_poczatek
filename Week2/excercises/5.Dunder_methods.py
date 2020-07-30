import random

class Product:
    
    def __init__(self, name, category_name, price):
        self.name = name 
        self.category_name = category_name
        self.price = price

    def __str__(self):
        return (f"Product name{self.name} | Category{self.category_name} | Price{self.price}")



class Order:
    
    def __init__ (self, name, last_name, order_elements = None):
        self.name = name
        self.last_name = last_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price


    def calculate_total_price(self):

        total_price = 0
        
        for element in self.order_elements:
            total_price += element.calculate_price()
        return total_price
    
    def __str__(self):
        order_details = (f"Order of {self.name} {self.last_name}")
        value_details = (f"For {self.total_price}")
        ordered_products = (f"Client ordered: ")
        for element in self.order_elements:
            ordered_products += f"\t{element}"
        result = "\n".join([order_details, value_details, ordered_products])
        return result


def random_order():
    number_of_product = random.randint(1,20)
    order_elements = []
    for product_number in range(number_of_product):
        name = f"Product{product_number}"
        category_name = f"Other"
        price = random.randint(1,20)
        product = Product(name, category_name, price)
        quantity = random.randint(1,10)
        order_elements.append(Order_element(product, quantity))
        
    order = Order("Adam", "Sierzan", order_elements=order_elements )
    return order

    
class Apple:
    
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price_for_kg = price_for_kg

    def calculate_price(self, quantity):
        return quantity*self.price_for_kg

    def __repr__(self):
        return f"Apple type: {self.name}, avg size: {self.size}, price for kg {self.price_for_kg}"

class Potato:
    
    def __init__(self, name, size, price_for_kg):
        self.name = name
        self.size = size
        self.price_for_kg = price_for_kg
    
    def calculate_price(self, quantity):
        return quantity*self.price_for_kg

    def __repr__(self):
        return f"Potato type: {self.name}, avg size: {self.size}, price for kg {self.price_for_kg}"


class Order_element:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.price_for_kg * self.quantity
    
    def __str__(self):
        return f"{self.product} x {self.quantity}"

def run_homework():

    first_order = random_order()
    print(first_order)
    first_order.__str__()


run_homework()
