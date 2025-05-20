class Coffee:
    def __init__(self, name):
        if not (isinstance(name, str) and len(name) >= 3):
            raise Exception("Coffee name must have at least 3 characters")
        self._name = name
        self._orders = []  

    @property
    def name(self):
        return self._name

    @property
    def orders(self):
        return self._orders
    
    @property
    def customers(self):
        unique_customers = {order.customer for order in self._orders}
        return list(unique_customers)
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

