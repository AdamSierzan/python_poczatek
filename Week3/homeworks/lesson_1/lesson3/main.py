
import random
from order import Order
from data_generator import generate_order_elements
from product import Product, Best_Before


def run_homework():
    cookies = Best_Before(
      name= "brown_cookie",
      category_name = "cookies",
      unit_price = 12,
      years_to_use = 2,
      production_date = 2019
    )
    is_it_ok = cookies.does_expire(2000)
    print(is_it_ok)


if __name__ == '__main__':
    run_homework()
