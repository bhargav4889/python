# Exercise: E001-V3 :
#
# Create one class named “location” with members “name”, “code”.
# Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
# Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
# This method will return all “movement” objects which belong to the passed “product” as an argument.
# Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary, and it contains “location” as key and actual stock of that product on that location as value.
# Create 4 different location objects.
# Create 5 different product objects.
# Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve.
# Display movements of each product using the “movement_by_product” method.
# Display product details with its stock at various locations using “stock_at_locations”.
# Display product list by location ( group by location).


class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        # print("Location", self.name, '\n''Code: ', self.code)

    def __str__(self):
        return self.name


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    @staticmethod
    def movement_by_product(product):
        for i in list_of_movements:
            if i.product == product:
                print("From-Location: ", i.from_location, "\n""To-Location: ", i.to_location, "\n""Product is: ",
                      i.product,
                      "\n""Quantity is: ", i.quantity)

    def move_by_product(self):
        for i in list_of_movements:
            print("From-Location: ", i.from_location, "\n""To-Location: ", i.to_location, "\n""Product is: ",
                  i.product,
                  "\n""Quantity is: ", i.quantity)
            print('\n')

    def movement(self, productname, movement):
        try:
            if productname.stockofproduct <= 0 or movement.quantity <= 0:
                raise ValueError("Out of Stock")
            print("From:", movement.from_location, '\n''To:', movement.to_location, '\n'"Quantity total: ",
                  productname.stockofproduct)

            ans = productname.stockofproduct - movement.quantity
            print(movement.to_location, 'Added: ', movement.quantity, '\n''After Available is: ', ans)
            print('\n')

        except ValueError as ve:
            print("Error:", str(ve))

    # def product_move(self,Object,Object2):
    #     try:
    #         if Object.stockofproduct<= 0 or Object2.quantity <=0:
    #             raise ValueError('Out Of Stock')
    #
    #         print('From-Location: ', Object.from_location, '\n''To-Location: ', Object.to_location, '\n''Product-Name: ',
    #               Object.product, '\n''Product Quantity: ', Object.quantity)
    #         ans = Object.stockofproduct - Object2.quantity
    #         print('After Product Move Available Quantity: ', ans)
    #         if ans == 0:
    #             print('Product Out of Stock ! Now')
    #
    #     except ValueError as ve:
    #         print('\n''Error: ', {str(ve)}, '\n')


m1 = Movement(from_location='Rajkot', to_location="Upleta", product="Mobile", quantity=100)
m2 = Movement(from_location="Surat", to_location="Rajkot", product="Laptop", quantity=20)
m3 = Movement(from_location='Baroda', to_location="Mumbai", product="Fruits", quantity=200)
m4 = Movement(from_location="Mumbai", to_location="Morbi", product='Tv', quantity=231)

list_of_movements = [m1, m2, m3, m4]


Movement.movement_by_product("Tv")


class Product:

    def __init__(self, location, stockofproduct, productname):
        self.productname = productname
        self.stockofproduct = stockofproduct
        self.location = location
        self.stock_at_locations = {self.location: self.stockofproduct}

    def __str__(self):
        return f"{self.productname}"

    def group_by_location(self, list2):
        for i in list2:
            for j in i.stock_at_locations.items():
                print("Location: ", j)
            print('\n')

    def display(self):
        locations = self.stock_at_locations.keys()
        for i in locations:
            print(i)


Rajkot = Location(name="Rajkot", code=120)
Upleta = Location(name="Upleta", code=123)
Surat = Location(name="Surat", code=99)
Ahmadabad = Location(name='Ahmadabad', code=31)

Mobile = Product(location=Rajkot, stockofproduct=10, productname="iPhone")
Laptop = Product(location=Upleta, stockofproduct=25, productname="Asus-Tuf")
Laptop1 = Product(location=Upleta, stockofproduct=5, productname="Asus-Tuf-2")
Fruits = Product(location=Surat, stockofproduct=3, productname="Apple")
Bikes = Product(location=Ahmadabad, stockofproduct=10, productname="Honda")
Car = Product(location=Surat, stockofproduct=20, productname="i-20")
#
# Mobile.display()
# Car.display()

laptops = Movement(from_location=Rajkot, to_location=Upleta, quantity=5, product=Laptop)
mobiles = Movement(from_location=Surat, to_location=Ahmadabad, quantity=10, product=Mobile)
fruits = Movement(from_location=Surat, to_location=Upleta, quantity=2, product=Fruits)
bikes = Movement(from_location=Ahmadabad, to_location=Rajkot, quantity=1, product=Bikes)
cars = Movement(from_location=Upleta, to_location=Surat, quantity=2, product=Car)

laptops.movement(productname=Laptop, movement=laptops)
mobiles.movement(productname=Mobile,movement=mobiles)
fruits.movement(productname=Fruits,movement=fruits)
bikes.movement(productname=Bikes,movement=bikes)
cars.movement(productname=Car,movement=cars)

# mobiles.product_move()
# fruits.product_move()
# bikes.product_move()
# cars.product_move()

# laptops.move_by_product()

list_of_products = [Laptop, Fruits, Bikes, Car, Mobile]

# new = Product(location='', stockofproduct='', productname='')
# new.group_by_location(list_of_products)
