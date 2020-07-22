from products import products, update_product_quantity



orders = []

def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]
    
    if available_quantity < quantity:
        print("We don't have enough quantity of this product")
        return None
    
    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }
    
    update_product_quantity
    orders.append(new_order)
    return new_order