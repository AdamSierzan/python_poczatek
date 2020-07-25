from Products import Product, print_product

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

def print_order(order):
    print(f"Order of {order.name} {order.last_name}")
    print(f"For {order.total_price}")
    print(f"Client ordered:")
    for product in order.list_of_products:
        print_product(product)
    print()

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