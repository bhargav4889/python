#  Create one class named "category" with members "name", "code", "no_of_products"

class Category:
    def __init__(self, name=None, code=None, no_of_products=0):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products

    def display(self):
        print("Category Name: ", self.name, '\n'"Code is: ", self.code, '\n''No Of Products: ', self.no_of_products)

    def __str__(self):
        return self.name


# c1.display()

# Create one class named "product" with member "name", "code", "category", "Price"

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.category.no_of_products += 1
        self.price = price

    def info(self):
        print("Product name: ", self.name, '\n''Product Code: ', self.code, '\n''Category is: ', self.category,
              '\n''Price is: ', self.price)

    def __str__(self):
        return self.name


#
# iphone = Product(name='iphone-12', code=1, category=Mobile, price=21000)
# iphone.info()

# Create three objects of a category.
vegetable = Category(name='Vegetable', no_of_products=0, code=20)
bikes = Category(name="Bikes", no_of_products=0, code=21)
fruits = Category(name="Fruits", no_of_products=0, code=12)

# Create 10 different products.The code must be unique.

Corns = Product(name='Corns', code=1, category=vegetable, price=200)
Onions = Product(name='Onion', code=2, category=vegetable, price=100)
Bananas = Product(name='banana', code=3, category=fruits, price=100)
HondaDio = Product(name="Honda-Dio", code=3, category=bikes, price=399999)
HondaShine = Product(name='Honda-Shine', code=4, category=bikes, price=499999)
Potatos = Product(name="Potato", code=5, category=vegetable, price=200)
Peas = Product(name='Peas', code=7, category=vegetable, price=100)
Watermelon = Product(name='WaterMelon', code=8, category=fruits, price=300)
Orange = Product(name='Orange', code=9, category=fruits, price=124)
Mango = Product(name='Mango', code=10, category=fruits, price=200)

# Print category info with its no_of_products

vegetable.display()
bikes.display()
fruits.display()

# Sort and Print products based on price ( Price High to Low and Low to High) with all details
list_of_products = [Corns, Onions, Bananas, HondaDio, HondaShine, Potatos, Peas, Watermelon, Orange, Mango]


#
# price low to high
def lower_to_upper(list1):
    length = len(list1)
    for i in range(0, length - 1):
        for j in range(length - i - 1):
            if list1[j].price > list1[j + 1].price:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


lower_to_upper(list1=list_of_products)

for i in list_of_products:
    print("Product-Name: ", i.name, '\n''Price: ', i.price)


# price high to low
def upper_to_lower(list1):
    length = len(list1)
    for i in range(0, length - 1):
        for j in range(length - i - 1):
            if list1[j].price < list1[j + 1].price:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


upper_to_lower(list1=list_of_products)

for i in list_of_products:
    print("Product-Name: ", i.name, '\n''Price: ', i.price)

# Search product using its code.

code = int(input("Enter Code: "))
for i in list_of_products:
    if code == i.code:
        print("Product Name is: ", i.name, '\n'"Product Code: ", i.code)
