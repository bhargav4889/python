# Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
class Category:
    def __init__(self, parent='parent', display_name='display', products=[], productname=None, productprice=None):
        self.parent = parent
        self.display_name = display_name
        self.products = products
        self.productname = productname
        self.productprice = productprice
        products.append(productname)
        products.append(productprice)
        print(products)


p1 = Category(productname='iphone', productprice=100)
p2 = Category(productprice=100, productname='watch')
p3 = Category(productprice=200, productname='bike')
p4 = Category(productprice=21, productname='toys')

list1 = [p1, p2, p3, p4]

for i in list1:
    print('\n', 'productname: ', i.productname, '\n', 'productprice: ', i.productprice)
print(p1.parent)
print(p1.display_name)


# ----------------------------------------------#

# Add a new member function to generate “display_name”

class Demo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_name(self):
        print('\n''Your Name: ', self.name, '\n''Your Email: ', self.email)


d = Demo(name='bhargav', email='bhargavkachhhela1@gmail.com')
d.display_name()


# ----------------------------------------------#

# “display_name” has a text value as below.
# Vehicle category without parent then “Vehicle”
# Car category with “Vehicle” as a parent then “Vehicle > Car”
# Petrol category with “Car” as a parent then “Vehicle > Car Petrol”
#
class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        print(self.vehicle)

    class Car:
        def __init__(self, name, parent=None):
            self.name = name
            self.parent = parent

        def display_name(self):
            print('Vehicle >', self.parent, )

    class Fuel:
        def __init__(self, fueltype, parent=None):
            self.fueltype = fueltype
            self.parent = parent

        def display_name(self):
            print('Car >', self.parent)


v = Vehicle('Vehicle')
v.Car('HondaCity', parent=v.Car.__name__).display_name()
v.Fuel('Petrol', parent=v.Fuel.__name__).display_name()


# ----------------------------------------------#

# Create 5 category objects with parent and child relation.
class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.child = []
        if self.parent is not None:
            self.child.append(self.parent)
            # print(self.child)

    def display(self):
        print(self.name, '\n')
        # print(self.parent)
        # print(self.child)


# parent
electronics = Category("Electronics")
food = Category("Food")
watch = Category("Watch")
#
# child
mobile = Category("Mobile", parent=electronics).display()
laptop = Category("Laptop", parent=electronics).display()
fruits = Category("Fruits", parent=food).display()
iwatch = Category("I-Watch", parent=watch).display()
tomato = Category('Tomato', parent=food).display()

# ----------------------------------------------#

# Create 3 product objects in each category.

iphone = Category('iPhone-12', parent=mobile).display()
hp = Category('Hp Laptop', parent=laptop).display()
iwatch7 = Category('iWatch7', parent=iwatch).display()


# ----------------------------------------------#

# Display the Category with its Code, Display Name, and all product details inside that category.

class Category:
    def __init__(self, code, displayname, productid, productname, productprice, productinfo):
        self.code = code
        self.displayname = displayname
        self.productid = productid
        self.productname = productname
        self.productprice = productprice
        self.productinfo = productinfo


class FoodProduct(Category):
    def __init__(self, code, displayname, productid, productname, productprice, productinfo):
        super().__init__(code, displayname, productid, productname, productprice, productinfo)

    def display(self):
        print('\n', 'Category-Code: ', self.code, '\n', 'Display-Name: ', self.displayname, '\n', 'Product-Id: ',
              self.productid,
              '\n', 'Product-Name: ', self.productname, '\n', 'Product-Price: ', self.productprice, '\n',
              'Product-Info: ', self.productinfo)


class DeviceProduct(Category):
    def __init__(self, code, displayname, productid, productname, productprice, productinfo):
        super().__init__(code, displayname, productid, productname, productprice, productinfo)

    def display(self):
        print('\n', 'Category-Code: ', self.code, '\n', 'Display-Name: ', self.displayname, '\n', 'Product-Id: ',
              self.productid,
              '\n', 'Product-Name: ', self.productname, '\n', 'Product-Price: ', self.productprice, '\n',
              'Product-Info: ',
              self.productinfo)


# food class
burger = FoodProduct(code=19, displayname='Fast- Food', productid=11, productname='Burger', productprice=100,
                     productinfo='Chezze Buger', ).display()
pizza = FoodProduct(code=29, displayname='Fast-Food', productid=2, productname='Pizza', productprice=299,
                    productinfo='italian Pizza').display()

# device class
iphone = DeviceProduct(code=21, displayname='mobile', productid=2129, productname='iphone-12', productprice=48888,
                       productinfo='Apple iphone12').display()
hp = DeviceProduct(code=18, displayname='Laptop', productid=2122, productname='Hp Pro', productprice=29999,
                   productinfo='Hp Gaming Laptop').display()

# ----------------------------------------------#

# Display product list by category ( group by category, order by category name).
#
products = [
    {'name': 'Bike', 'category': 'Vehicle'},
    {'name': 'Burger', 'category': 'Food'},
    {'name': 'Laptop', 'category': 'Device'},
    {'name': 'Mobile', 'category': 'Device'},
]

# empty dict
products_by_category = {}

for product in products:
    category = product["category"]
    if category not in products_by_category:
        products_by_category[category] = []
    products_by_category[category].append(product)

categories = list(products_by_category.keys())

categories.sort()

for category in categories:
    print(f"{category}:")
    category_products = products_by_category[category]
    for product in category_products:
        print(f"- {product['name']}")
