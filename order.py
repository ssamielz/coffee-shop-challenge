# order.py
from customer import Customer
from coffee import Coffee

class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        self._price = None  # must be defined before the price setter is called
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('customer must be an instance of Customer')
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError('coffee must be an instance of Coffee')
        self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if self._price is not None:
            raise AttributeError("Price is immutable and cannot be changed.")
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = price

    @classmethod
    def all_customers(cls):
        return list({order.customer for order in cls.orders})

    @classmethod
    def all_coffees(cls):
        return list({order.coffee for order in cls.orders})

mocha=Coffee("Mocha")
john = Customer("John")
order=Order(john,mocha,4.0)
print(order)
print(john.orders)
print(mocha.name)