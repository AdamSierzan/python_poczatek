import random
from order_element import OrderElement
from product import Product
from order import Order

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 10

MIN_QUANTITY = 1
MAX_QUANTITY = 10

def generate_order_elements(number_of_products=None):
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ELEMENTS)
    order_elements = []
    for product_number in range(number_of_products):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        identifier = random.randint(1,10)
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        product = Product(product_name, category_name, unit_price, identifier)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity, ))

    return order_elements

