

class Coffee:
    coffees = []
    def __init__(self, name):
        self.name = name
        if self not in Coffee.coffees: Coffee.coffees.append(self)
        
    @property
    def name(self):
        return self._name
    
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
        return [order for order in Order.orders if order.coffee == self]
    
    def customers(self):
        return [order.customer for order in self.orders()]
    
    def num_orders(self):
        total_orders = 0
        for order in self.orders(): total_orders += 1           
        return total_orders
    
    def average_price(self):
        total_price = 0
        for order in self.orders(): total_price += order.price
        return total_price/self.num_orders()