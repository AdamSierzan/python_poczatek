# Create a class of Product, Order, Apples, Potatoes
#Create a few object of apple class and potatoe class and 
# print their type with type function
# <Create a 5 orders dictionary, in which keys will be names of products, 
# and values will be Instances of product class


class Apple:
    pass

class Potato:
    pass
class Product:
    pass
class Order:
    pass



if __name__ == "__main__":

    ligol = Apple()
    ambrosia = Apple()
    opal = Apple()

    yukon = Potato()
    bintje = Potato()
    ratte = Potato()

    print(type(ligol))
    print(type(ambrosia))
    print(type(opal))
    print(type(yukon))
    print(type(bintje))        
    print(type(ratte))


    orders = [Order(), Order(), Order(), Order(), Order()]
    print(orders)

    products_dictonary = {
        "Orange": Product(),
        "Banana": Product(),
        "Cherry": Product()
    }

    print(products_dictonary)