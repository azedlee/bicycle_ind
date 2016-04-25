class Bicycle(object):
    """
    Bicycles contain model name, weight and the cost
    """
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost
    
    def __repr__(self):
        return "{0} weights {1} kilograms and costs ${3} per bicycle".format(self.model_name, self.weight, self.cost)

class Customers(object):
    """
    Customer contains customer name, amount of money per customer and if the person can purchase a new bicycle
    """
    def __init__(self, customer_name, customer_money):
        self.customer_name = customer_name
        self.customer_money = customer_money
        
        self.bike = False
    
    def __repr__(self):
        return "{0} has ${1}".format(self.customer_name, self.customer_money)

class BikeShop(object):
    """
    Bike shop contains shop name, stock per model, 20% profit margin per cost and profit per bicycle sold
    """
    def __init__(self, shop_name, cost_margin, bike):
        self.shop_name = shop_name
        self.cost_margin = cost_margin
        
        self.model_stock = {}
        self.profit = 0
        
        for bikes in bike:
            
            bike.price = bike.cost * (1 + self.cost_margin/100)
            self.model_stock[bike.model] = bike.price
    
    def sell(self, bike, customer):
        
        customer.bike = bike
        customer.money -= bike.price
        self.profit += bike.markup
        del self.model_stock[bike.model]