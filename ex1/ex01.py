# Create one class named "category" with members "name", "code", "no_of_products"

class Category:
    def __init__(self, name, no_of_products):
        self.name = name
        self.no_of_products = no_of_products

    def display_all(self):
        print('\n', 'CategoryName: ', self.name, '\n', 'No_Of_Products: ', self.no_of_products)


c = Category()
c.display_all()


# --------------------------------------#

# Create one class named "product" with member "name", "code", "category", "Price"

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def displayproductdetails(self):
        print('\n', 'Product Name: ', self.name, '\n', 'Category: ', self.category, '\n', 'Product Price: ', self.price)


#
#
pr = Product()
pr.displayproductdetails()

# ----------------------------------------------#

# Create three objects of a category.

cat1 = Category(name='Mobile', no_of_products=100)
cat2 = Category(name='Bike', no_of_products=200)
cat3 = Category(name='Car', no_of_products=300)
cat1.display_all()
cat2.display_all()
cat3.display_all()

# ----------------------------------------------#

# Create 10 different products. The code must be unique.

product1 = Product(name='iPhone-5', category='Mobile', price=199)
product2 = Product(name='iPhone-6', category='Mobile', price=299)
product3 = Product(name='iPhone-6s', category='Mobile', price=399)
product4 = Product(name='iPhone-7', category='Mobile', price=499)
product5 = Product(name='iPhone-8+', category='Mobile', price=599)
product6 = Product(name='iPhone-X', category='Mobile', price=699)
product7 = Product(name='iPhone-XR', category='Mobile', price=799)
product8 = Product(name='iPhone-11', category='Mobile', price=899)
product9 = Product(name='iPhone-12', category='Mobile', price=999)
product10 = Product(name='iPhone-13', category='Mobile', price=1199)

list1 = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

for i in list1:
    print('\n', 'Product Name: ', i.name, '\n', 'Category: ', i.category, '\n', 'Product-Price: ', i.price)

# ----------------------------------------------#

# Print category info with its no_of_products
category_info = {
    'Mobile': 100,
    'Car': 200,
    'Bike': 300
}
for i, j in category_info.items():
    print('\n', 'Category-Name is: ', i, '\n', 'No_Of_Products: ', j)

# dict methods
# dict.keys()=> keys print
# dict.values()=> values only print
# dict.items()=>keys&values are print

# ----------------------------------------------#
# Sort and Print products based on price ( Price High to Low and Low to High) with all details.
# use bubble sort

products = {'Mobile': 1000, 'Bottle': 500, 'Fruits': 900}
productslist = list(products.items())
print(productslist)

length = len(productslist)
print(length)

# price low to high
for i in range(length - 1):
    for j in range(i + 1, length):
        if productslist[i] > productslist[j]:
            temp = productslist[i]
            productslist[i] = productslist[j]
            productslist[j] = temp
print('Product_Price_Low_To_High', '\n', productslist)

# price high to low
for i in range(length - 1):
    for j in range(i + 1, length):
        if productslist[i] < productslist[j]:
            temp = productslist[i]
            productslist[i] = productslist[j]
            productslist[j] = temp
print('Product_Price_High_To_Low', '\n', productslist)

# ----------------------------------------------#

# Search product using its code.
# use in & not-in operator
products = ['Mobile', 'Car', 'Bike', 'Bottle', 'Glasses', 'T-shirt']
search = input('Enter Word To Search: ')
if search in products:
    print('Word is Found in List: ', search)
else:
    print('Word is Not Found in List: ', search)
