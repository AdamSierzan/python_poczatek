# Modify the exercise from last lesson to change functions into methods.
# Write a methods to calculate apple price, to each Apple oject, and proce of potatoes, for 
# pottato object, based on the information from argument about number of kilograms
# Write OrderElement class, in which you will represent position in order. It will contain information about the 
# product, number of ordered elements. In OrderElement implement method to write information about number of elements and product, and 
# the one that calculates price of the elements 
# In Order class change list of productslist of positions in ordere( modify functions i.e random order).
# Write a method to sum order of all elements (use method from OrderElement) and use it in constructor to initialize value of an order
import random

class Product:
    
    def __init__(self, name, category_name, price):
        self.name = name 
        self.category_name = category_name
        self.price = price

    def print_self(self):
        print(f"Product name{self.name} | Category{self.category_name} | Price{self.price}")



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
            total_price += elements.calculate_price()
        return total_price
    
    def print_self(self):
        print(f"Order of {self.name} {self.last_name}")
        print(f"For {self.total_price}")
        print(f"Client ordered:")
        for element in self.order_elements:
            print("\t", end="")
            element.print_self()
        print("=" * 20)
        print()


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

class Potato:
    
    def __init__(self, name, size, price_for_kg):
        self.name = name
        self.size = size
        self.price_for_kg = price_for_kg
    
    def calculate_price(self, quantity):
        return quantity*self.price_for_kg

class Order_element:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.price_for_kg *self.quantity
    
    def print_self(self):
        self.product.print_self()
        print(f"\t\t x {self.quantity}")

def run_homework():

    first_order = random_order()
    print(first_order)
    first_order.print_self()


run_homework()
