from collections import namedtuple

Apple = namedtuple("Apple", ["species_name", "size", "price"])

def run_example():
    ligol = Apple("ligol", "medium", "5")
    print(ligol.species_name, ligol.size, ligol.price, ligol)
    print("------")
    print(ligol[0], ligol[1], ligol[2])
    print("------")

    for element in ligol:
        print(element)


run_example()