from shop.orders import create_new_order
def run_shop():
    print("Hi, welcome to my shop, tell me what you need")

    product_name = input("what do you want to buy")
    quantity = int(input("How much do you need"))

    result = create_new_order(product_name, quantity)
    if result is not None:
        total_price = result["total_price"]
        print(orders)

if __name__ == "__main__":
    run_shop()