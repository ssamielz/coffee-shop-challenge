
from coffee import Coffee

class Customer:
    customers = []
    def __init__(self, name):
        self.name = name
        Customer.customers.append(self)
        
    @property
    def name(self):
        return self._name
    
    #enforeces string type and 1 - 15 character length
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        else:
            if len(name) > 0 and len(name) <= 15:
                self._name = name
            else:
                print('Name must be between one to 15 characters')
                
    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.customer == self]
    
    def coffees(self):        
        coffees =  [order.coffee.name for order in self.orders()]
        coffees = set(coffees)
        return list(coffees)
    
    def create_order(self, coffee, price):
        from order import Order
        Order(self, coffee, price)