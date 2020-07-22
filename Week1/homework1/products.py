products = { 
    "apple": 
    {
        "quantity": 100,
        "price": 3.5
    },
    "bread": 
    {
        "quantity": 20,
        "price": 2.5
    }
}


def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"]-= ordered_quantity