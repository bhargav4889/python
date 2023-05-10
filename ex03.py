# Create one class named “location” with members “name”, “code”.

class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def locationinfo(self):
        print('Location Name: ', self.name, '\n''Location Code: ', self.code)


# lc = Location(name=input('Enter Location Name: '), code=int(input('Enter Location Code: ')))
# lc.locationinfo()


# ----------------------------------------------------#
# Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.

class Movement:
    from_location = 'Rajkot'
    to_location = 'Surat'
    product = 'Laptop', 'Mobile', 'Fruits'
    quantity = 200

    def __init__(self, from_location=None, to_location=None, productname=None, quantity=None, code=None):
        self.from_location = from_location
        self.to_location = to_location
        self.productname = productname
        self.quantity = quantity
        self.code = code
        self.products = []

    def movement_info(self):
        print('From-Location: ', self.from_location, '\n''To-Location: ', self.to_location, '\n''Product is: ',
              self.product, '\n''Quantity is: ', self.quantity)

    def movement_by_product(self):
        self.products.append(self.product)
        print(self.products)

    @staticmethod
    def movements_by_product(product):
        print('Product Is: ', product, '\n''Quantity is: ', Movement.quantity, '\n''From_Location: ',
              Movement.from_location, '\n''To_Location: ', Movement.to_location)

    def movements_infomation(self):
        print('\n', "From-Location: ", self.from_location, '\n', "To_location: ", self.to_location, '\n',
              "Product_Name: ",
              self.productname, '\n', "Quantity is: ", self.quantity, '\n', 'Code is: ', self.code)

    def product_move(self):
        try:
            if self.quantity <= 0:
                raise ValueError('Out Of Stock')

            print('From-Location: ', self.from_location, '\n''To-Location: ', self.to_location, '\n''Product-Name: ',
                  self.productname, '\n''Code: ', self.code, '\n''Product Quantity: ', self.quantity)
            self.quantity -= 1
            print('After Product Move Available Quantity: ', self.quantity)
            if self.quantity == 0:
                print('Product Out of Stock ! Now')

            print('\n')

        except ValueError as ve:
            print('Error: ', {str(ve)})


# mv = Movement(from_location='Rajkot', to_location='Upleta', productname='Apple', quantity=100, code=12)
# mv.movement_info()
# ----------------------------------------------------#
# Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
# This method will return all “movement” objects which belong to the passed “product” as an argument.

# mv = Movement()
# mv.movements_by_product(product=input('Enter Product Name: '))


# ----------------------------------------------------#
# Add new members inside the product “stock_at_locations”.
# This new member is a type of Dictionary, and it contains “location” as key and
# actual stock of that product on that location as value.

class Product:
    def __init__(self, location1, stockofproduct, productname):
        self.productname = productname
        self.location = location1
        self.stockofproduct = stockofproduct
        self.stock_at_locations = {}

    def addlocation(self):
        self.stock_at_locations[self.location] = self.stockofproduct
        print(self.stock_at_locations)


#
# pr = Product(location1='Rajkot', stockofproduct=200)
# pr.addlocation()

# ----------------------------------------------------#
# Create 4 different location objects.

gujarat = Location(name='Rajkot', code=360001)
bihar = Location(name='Bihar', code=800001)
delhi = Location(name='New Delhi', code=110001)
rajasthan = Location(name='Jaipur', code=302001)

gujarat.locationinfo()
bihar.locationinfo()
delhi.locationinfo()
rajasthan.locationinfo()

# ----------------------------------------------------#

# Create 5 different product objects.

laptops = Product(location1=gujarat.name, stockofproduct=10, productname='laptop')
foods = Product(location1=bihar.name, stockofproduct=2, productname='foods')
watches = Product(location1=gujarat.name, stockofproduct=1, productname='watches')
t_shirt = Product(location1=delhi.name, stockofproduct=9, productname='t-shirt')
cars = Product(location1=rajasthan.name, stockofproduct=21, productname='cars')

laptops.addlocation()
foods.addlocation()
watches.addlocation()
t_shirt.addlocation()
cars.addlocation()

# ----------------------------------------------------#

# Move those 5 products from one location to another location using movement.
# Manage exceptions if product stock goes in -ve.

laptop = Movement(from_location=rajasthan.name, to_location=gujarat.name, productname=laptops.productname,
                  quantity=laptops.stockofproduct, code=rajasthan.code)
tshirt = Movement(from_location=bihar.name, to_location=rajasthan.name, productname=t_shirt.productname,
                  quantity=t_shirt.stockofproduct, code=bihar.code)
watch = Movement(from_location=bihar.name, to_location=gujarat.name, productname=watches.productname,
                 quantity=watches.stockofproduct, code=bihar.code)
food = Movement(from_location=delhi.name, to_location=gujarat.name, productname=foods.productname,
                quantity=foods.stockofproduct, code=delhi.code)
car = Movement(from_location=delhi.name, to_location=bihar.name, productname=cars.productname,
               quantity=cars.stockofproduct, code=delhi.code)

laptop.product_move()
tshirt.product_move()
watch.product_move()
food.product_move()
car.product_move()

# ----------------------------------------------------#

# Display movements of each product using the “movement_by_product” method.
# m1 = Movement()
# m1.movement_by_product()

# ----------------------------------------------------#

# Display product details with its stock at various locations using “stock_at_locations”.
#
# foods = Product(location1=gujarat.name, stockofproduct=foods.stockofproduct,productname=foods.productname)
# foods.addlocation()
# watch = Product(location1=bihar.name, stockofproduct=watches.stockofproduct,productname=watches.productname)
# watch.addlocation()

# ----------------------------------------------------#
# Display product list by location ( group by location).
# list_of_products = [
#     {'productname': 'Laptops', 'location': 'Rajkot'},
#     {'productname': 'Cameras', 'location': 'Surat'},
#     {'productname': 'Mobiles', 'location': 'Ahmedabad'}
# ]
#
# # empty dict
# location_by_product = {}
#
# for i in list_of_products:
#     location = i['location']
#     if location not in location_by_product:
#         location_by_product[location] = []
#         location_by_product[location].append(i)
#
# locations = list(location_by_product.keys())
# locations.sort()
#
# for loc in locations:
#     print('location is: ', loc)
#     locations_products = location_by_product[loc]
#     for p in locations_products:
#         print('Product name: ', p['productname'])
