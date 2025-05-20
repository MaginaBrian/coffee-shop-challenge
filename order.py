from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise Exception("Order must be initialized with a Customer instance")
        self._customer = customer

        if not isinstance(coffee, Coffee):
            raise Exception("Order must be initialized with a Coffee instance")
        self._coffee = coffee

        if not (isinstance(price, float) and 1.0 <= price <= 10.0):
            raise Exception("Price must be a float between 1.0 and 10.0")
        self._price = price

        self._customer._orders.append(self)

        self._coffee._orders.append(self)


    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price