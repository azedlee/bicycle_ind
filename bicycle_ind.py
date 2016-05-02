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
    
    def can_afford(self, cost):
        return self.customer_money >= cost


class BikeShop(object):
    """
    Bike shop contains shop name, stock per model, 20% profit margin per cost and profit per bicycle sold
    """
    def __init__(self, shop_name, cost_margin, bikes):
        self.shop_name = shop_name
        self.cost_margin = cost_margin
        
        self.model_stock = {}
        self.profit = 0
        self.inventory = {}
        
        for bike in bikes:
            
            bike.price = bike.cost * (1 + self.cost_margin/100)
            self.model_stock[bike.model_name] = bike
            self.inventory[bike.model_name] = 5
    
    
    def sell(self, bike, customer):
        
        if customer.can_afford(bike.price):
            if self.inventory[bike.model] > 0:
                customer.bike = bike
                customer.money -= bike.price
                self.profit += bike.price
                self.inventory[bike.model] -= 1
            else:
                print("{} is out of Stock".format(bike.model))
        else:
            print("{} does not have enough money.".format(customer.name))