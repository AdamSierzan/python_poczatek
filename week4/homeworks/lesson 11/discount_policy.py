
class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price


class PercentageDiscount(DiscountPolicy):

    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_price):
        return total_price * (100 - self.discount_percentage) / 100
    

class AbsoluteDiscount(DiscountPolicy):
    
    def __init__(self, value_of_discount):
        self.value_of_discount = value_of_discount

    def apply_discount(self, total_price):
        if total_price < self.value_of_discount:
            return 0
        return total_price - self.value_of_discount



# def loyal_customer_policy(total_price):
#     return 0.95 * total_price


# def christmas_policy(total_price):
#     if total_price > 100:
#         return total_price - 20
#     return total_price
