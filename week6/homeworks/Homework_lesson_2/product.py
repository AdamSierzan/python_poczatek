from enum import Enum
# import random
from dataclasses import dataclass

class ProductCategory(Enum):
    FOOD = "Jedzonko"
    TOOLS = "Narzędzia"
    OTHER = "Inne"

@dataclass

class Product:

 
    name: str
    category : ProductCategory
    unit_price: float
    identifier: int

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category.value} | Cena: {self.unit_price} PLN/szt"

@dataclass
class Best_Before(Product):
 
    
    years_to_use: int
    production_date: int


    def does_expire(self, current_year):
        if self.production_date - current_year < self.years_to_use:
            print(f"Your product is not expired")
        else:
            print(f"Your product is expired")


    

