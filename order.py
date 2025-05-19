from customer import Customer
from coffee import Coffee

class Order:
    orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        print(Order.orders)
        Order.orders.append(self)
        # print(Order.orders)
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('customer must be an instance of Customer')
        else:
            self._customer = customer
            
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError('coffee must be an instance of Coffee')
        else:
            self._coffee = coffee
            
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError('Price mus be a float')
        else:
            if 1.0 <= price <= 10.0:
                self._price = price
                
    @classmethod
    def customer(cls):
        return cls.customer
    
    @classmethod
    def coffee(cls):
        return cls.coffee
    
    
alice = Customer("Alice")      
bob = Customer("Bob")           
charlie = Customer("Charlie") 

latte = Coffee("Latte")          # valid
espresso = Coffee("Espresso")    # valid
mocha = Coffee("Mocha")  

order1 = Order(alice, latte, 3.5)     # valid
order2 = Order(alice, espresso, 4.0)  # valid
order3 = Order(bob, latte, 5.0)       # valid
order4 = Order(charlie, mocha, 2.5)   # valid
order5 = Order(alice, latte, 6.0)     # valid
order6 = Order(bob, mocha, 7.0)       # valid
order7 = Order(charlie, espresso, 2.0)

# print(alice.orders())