class ElementLimitError(Exception):

    def __init__(self, order_limit, message=None, *args):
        self.order_limit = order_limit
        if message == None:
            message = f"Osiągnięto limit pozycji w zamówieniu, który wynosi {order_limit}"
        super().__init__(message, *args)
    


