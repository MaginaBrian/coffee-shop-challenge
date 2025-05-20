from order import Order

class Customer:
    def __init__(self, name):
        self._name = None  
        self.name = name  
        self._orders = [] 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Name must be a string and must have at most 15 characters")

    @property 
    def orders(self):
        return self._orders   

    @property
    def coffees(self):
        unique_coffees = {order.coffee for order in self._orders} 
        return list(unique_coffees)
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee.orders.append(new_order)
        return new_order
    
    @classmethod
    def most_aficionado(cls,coffee):
        if not coffee.orders:
            return None
        
        spending = {}
        for order in coffee.orders:
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price

        return max(spending, key=spending.get)    from order import Order

class Customer:
    def __init__(self, name):
        self._name = None  
        self.name = name  
        self._orders = [] 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Name must be a string and must have at most 15 characters")

    @property 
    def orders(self):
        return self._orders   

    @property
    def coffees(self):
        unique_coffees = {order.coffee for order in self._orders} 
        return list(unique_coffees)
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee.orders.append(new_order)
        return new_order
    
    @classmethod
    def most_aficionado(cls,coffee):
        if not coffee.orders:
            return None
        
        spending = {}
        for order in coffee.orders:
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price

        return max(spending, key=spending.get)    