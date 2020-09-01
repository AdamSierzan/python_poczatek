import random

class Product:

 
    def __init__(self, name, category_name, unit_price, identifier):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
        self.identifier = identifier


    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category_name == other.category_name and
                self.unit_price == other.unit_price)

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt"


class Best_Before(Product):
    def __init__(self, name, category_name, unit_price, years_to_use, production_date):
        super().__init__(name, category_name, unit_price)
        self.years_to_use = years_to_use
        self.production_date = production_date

    def does_expire(self, current_year):
        if self.production_date - current_year < self.years_to_use:
            print(f"Your product is not expired")
        else:
            print(f"Your product is expired")

