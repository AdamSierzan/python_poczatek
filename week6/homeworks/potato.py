from dataclasses import dataclass

@dataclass
class Potato:

    species_name: str
    size: str
    price: int

    def calculate_price(self, quantity):
        return quantity * self.price
