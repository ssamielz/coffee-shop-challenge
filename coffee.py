

class Coffee:
    coffees = []
    def __init__(self, name):
        self._name = name
        if self not in Coffee.coffees: Coffee.coffees.append(self)
        
    @property
    def name(self):
        return self._name
    
    #enforeces string type and 1 - 15 character length
    @name.setter
    def name(self, name):
        #making the name immutable once initialized
        if self._name is not None:
            raise AttributeError("Coffee name is immutable and cannot be changed.")
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        else:
            if len(name) > 0 and len(name) <= 15:
                self._name = name
            else:
                print('Name must be between one to 15 characters')
                
    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.coffee == self]
    
    def customers(self):
        customers = [order.customer.name for order in self.orders()]
        customers = set(customers)
        return sorted(list(customers))
    
    def num_orders(self):
        total_orders = 0
        for order in self.orders(): total_orders += 1           
        return total_orders
    
    def average_price(self):
        total_price = 0
        for order in self.orders(): total_price += order.price
        return total_price/self.num_orders()
