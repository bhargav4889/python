from ex1.ex01 import Product as PR


# Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class

class Category:
    def __init__(self, display_name, parent=None):
        self.display_name = display_name
        self.parent = parent
        self.products = []

    def display_info(self):
        while self.parent is None:
            return self.display_name
        else:
            return f'{self.parent.display_info()} > {self.display_name}'

    def __str__(self):
        return f'{self.products}'

    def order_by_category(self, list1):
        length = len(list1)
        for i in range(0, length - 1):
            for j in range(length - i - 1):
                if list1[j].category > list1[j + 1].category:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
        for k in list1:
            print("Category name: ", k.category, '\n''Product Name: ', k.name)

    def group_by_category(self, list2):
        for i in list2:
            for j in i.products:
                print("Product Name: ", j.name, '\n''Product Code: ', j.code, '\n''Category: ', j.category,
                      '\n'"Price: ",
                      j.price, '\n')
            print('\n')


Vehicle = Category(display_name="Vehicle")
Car = Category(display_name="Car", parent=Vehicle)
Bike = Category(display_name="Bike", parent=Vehicle)
Petrol = Category(parent=Bike, display_name="Petrol")
Diesel = Category(parent=Car, display_name='Diesel')
NewObj = Category(parent=Diesel, display_name="newobj2")
NewObj2 = Category(parent=NewObj, display_name='New')

print(Vehicle.display_info())
print(Bike.display_info())
print(Car.display_info())
print(Petrol.display_info())
print(Diesel.display_info())
print(NewObj.display_info())
print(NewObj2.display_info())

# Vehicle is Parent Class It Has Two Child Class --> 1)Bike 2)Car
# Bike Class Has One Child Class --> Petrol
# Car Class has One Child Class --> Diesel

Mustang = PR(name="Mustang", category=Vehicle.display_name, price=190, code=10)
RollsRoyce = PR(name='Rolls-Royce', category=Vehicle.display_name, price=200, code=11)
BMW = PR(name='BMW', category=Vehicle.display_name, price=240, code=12)

Vehicle.products.insert(0, Mustang)
Vehicle.products.insert(1, RollsRoyce)
Vehicle.products.insert(2, BMW)

Swift = PR(name="Swift-Turbo", category=Car.display_name, price=1999, code=21)
HondaCity = PR(name='Honda-City-Elite', category=Car.display_name, price=344, code=22)
Toyota = PR(name='Toyota-Corolla', category=Car.display_name, price=657, code=23)

Car.products.append(Swift)
Car.products.append(HondaCity)
Car.products.append(Toyota)

RoadBikes = PR(name="AeroStorm", category=Bike.display_name, price=15999, code=31)
ElectricBikes = PR(name="TurboBoost", category=Bike.display_name, price=16999, code=32)
CityBikes = PR(name="CitySprint", category=Bike.display_name, price=20000, code=33)

Bike.products.append(RoadBikes)
Bike.products.append(ElectricBikes)
Bike.products.append(CityBikes)

Power_Generation = PR(name="AdaniGreenEnergy", category=Petrol.display_name, price=900, code=41)
Small_Engines = PR(name='PetrolEngines', category=Petrol.display_name, price=20000, code=42)
Small_machinery = PR(name='PilarPressMachine', category=Petrol.display_name, price=25000, code=43)

Petrol.products.append(Power_Generation)
Petrol.products.append(Small_Engines)
Petrol.products.append(Small_machinery)

Trains = PR(name='Train-Engines', category=Diesel.display_name, price=50000, code=51)
Generator = PR(name='Generator-Machine', category=Diesel.display_name, price=258000, code=52)
Rocket = PR(name="Spaceship", category=Diesel.display_name, price=450000, code=53)

Diesel.products.append(Trains)
Diesel.products.append(Generator)
Diesel.products.append(Rocket)


list_of_products = [Mustang, BMW, RollsRoyce, Swift, Toyota, HondaCity, RoadBikes, ElectricBikes, CityBikes,
                    Power_Generation, Small_Engines, Small_machinery, Trains, Generator, Rocket]
list_of_categories = [Car, Diesel, Petrol, Vehicle, Bike]

#
new = Category(display_name='')
new.order_by_category(list_of_products)
new.group_by_category(list_of_categories)

# ----------------------------------------------------------------------------#
# def order_by_category(list1):
#     length = len(list1)
#     for i in range(0, length - 1):
#         for j in range(length - i - 1):
#             if list1[j].category > list1[j + 1].category:
#                 list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     return list1


# order_by_category(list1=list_of_products)
# for i in list_of_products:
#     print("Product Name: ", i.name, '\n''Product Code: ', i.code, '\n''Category: ', i.category, '\n'"Price: ",
#           i.price, '\n')
#
#
# def group_by_category(list2):
#     for i in list2:
#         for j in i.products:
#             print("Product Name: ", j.name, '\n''Product Code: ', j.code, '\n''Category: ', j.category, '\n'"Price: ",
#                   j.price, '\n')
#         print('\n')

#
# group_by_category(list_of_categories)
