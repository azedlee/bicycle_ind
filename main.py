import random
from bicycle_ind import Bicycle, BikeShop, Customers

#Create Bikes

Professional = Bicycle("Professional", 17, 800)
Expert = Bicycle("Expert", 17, 500)
Mountain = Bicycle("Mountain", 17, 385)
City = Bicycle("City", 16, 300)
Amateur = Bicycle("Amateur", 16, 250)
Childrens = Bicycle("Childrens", 12, 150)

bike_model = [Professional, Expert, Mountain, City, Amateur, Childrens]

#Create a Shop w/ Shop Name, Margin, Bikes Stock 

peters_shop = BikeShop("Peter Griffin's Bike Shop", 20, bike_model)

#Create Customers

Meg = Customers("Meg", 1000)
Chris = Customers("Chris", 500)
Stewie = Customers("Stewie", 200)

peters_customers = [Meg, Chris, Stewie]

#Sell a Bike to a Customer
for person in peters_customers:
    person.affordable = []
    for bike in bike_model:
        if person.customer_money >= bike.cost:
            print(bike.model_name)
            person.affordable.append(bike.model_name)
for person in peters_customers:
    bought = random.choice(person.affordable)
    print(person.customer_name, "bought", bought)