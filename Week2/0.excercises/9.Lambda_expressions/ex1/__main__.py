
from Order_elements import OrderElement
from Order import Order
from Products import Product
# from Tax_calc import TaxCalculator, TaxRates

# def get_order_price(order):
#     return order.total_price

def run_homework():
    orders = []
    for _ in range(5):
        orders.append(Order.generate_order(2))
 
    # orders.sort(key=get_order_price)
    orders.sort(key=lambda order: order.total_price)

    for order in orders:
        print(order)


if __name__ == '__main__':
        run_homework()