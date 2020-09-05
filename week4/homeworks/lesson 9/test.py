from product import Product

def test_for_products_comprision():

    parameters = [
        ("ciastka", "słodycze", 5, "ciastka", "słodycze", 5, True),
        ("ciastka", "słodycze", 5, "chleb", "jedzenie", 5, False),
        ("ciastka", "słodycze", 5, "ciastka", "jedzenie", 5, False),
        ("ciastka", "słodycze", 5, "ciastka", "słodycze", 4, False),
    ]

    for params in parameters:
        name, category, price, other_name, other_category, other_price, expected_result = params
        result = Product(name, category, price) == Product(other_name, other_category, other_price)
        if result == expected_result:
            print("Ok")
        else:
            print(f"Data error, result is negative")


def run_test():
    test_for_products_comprision()

print(run_test())



