from dataclasses import dataclass

@dataclass
class Apple:

    species_name: str
    size: str
    price: int

    def calculate_price(self, quantity):
        return quantity * self.price

   