class Dad():
    def say_hello(self):
        print("I'm a dad!")


class Son(Dad):
    def say_hello(self):
        print("I'm a Son!")


class Son2(Dad):
    def say_hello(self):
        print("I'm a Son2!")


class Grandson(Dad):
#  def say_hello(self):
#         print("I'm a son of my granddad son!")
    pass

def run_example():
    grandkid = Grandson()
    print(grandkid.say_hello())


if __name__ == '__main__':
    run_example()