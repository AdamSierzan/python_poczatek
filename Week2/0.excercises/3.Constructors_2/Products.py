class Product:
    
    def __init__(self, name, category_name, price):
        self.name = name 
        self.category_name = category_name
        self.price = price

def print_product(product):
    print(f"Product name{product.name} | Category{product.category_name} | Price{product.price}")
