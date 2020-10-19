
# Rozbuduj własną klasę wyjątku dodając do niej pole domyślną wiadomość i pole “allowed_limit”
import data_generator
from order import Order
from product import Product
from errors import ElementsInOrderLimitError


def run_homework():
    order_elements_on_limit = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)
    product = data_generator.generate_product()
    quantity = data_generator.generate_quantity()
    
    try:
        order_on_limit.add_product_to_order(product, quantity)
    except ElementsInOrderLimitError as error:
        print(f"Błąd: {error}")

        print(f"Błąd limit pozcji wynosi: {error.allowed_limit}")
    
    

    # order_elements_over_limit = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS + 1)
    # order_over_limit = Order("Bob", "Kowalski", order_elements=order_elements_over_limit)


if __name__ == '__main__':
    run_homework()
