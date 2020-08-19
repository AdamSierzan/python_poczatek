from order import Order
from discount_policy import DiscountPolicy

class ExpressDelivery(Order):
    
    EXPRESS_DELIVERY_FEE = 10

    def __init__(self, date_of_delivery, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.date_of_delivery = date_of_delivery
    
    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price) + ExpressDelivery.EXPRESS_DELIVERY_FEE
    
   
    def __str__(self):
        mark_lines = "-"*20
        order_details = f"Delivery for {self.client_first_name} {self.client_last_name}"
        value_details = f"For {self.total_price}"
        delivery_date = f"Will arrive on {self.date_of_delivery}"
        product_details = f"Ordered elements {self.order_elements}"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_lines, order_details, value_details, delivery_date, product_details])
        return result
