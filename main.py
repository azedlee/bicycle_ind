from bicycle_ind import Bicycle, BikeShop, Customers

#Create Bikes

bikes = [
    Bicycle("Professional", 17, 800), Bicycle("Expert", 17, 500),
    Bicycle("Mountain", 17, 385), Bicycle("City", 16, 300),
    Bicycle("Amateur", 16, 250), Bicycle("Childrens", 12, 150)
    ]

#Create a Shop w/ Shop Name, Margin, Bikes Stock 

shop = BikeShop("Peter Griffin's Bike Shop", 20, bikes)

#Create Customers

customers = [
    Customers("Meg", 1000), Customers("Chris", 500), 
    Customers("Stewie", 200)
    ]

#Sell a Bike to a Customer


print(shop)