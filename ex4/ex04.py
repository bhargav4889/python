# Exercise: E002-V1
# Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
# "type" must be from "company,contact,billing,shipping".
# "company" must be a Customer object which is the parent object.
# Apply Multiple possible validation for phone number and email
# Does not allowed number in name,city,state and country
#
import datetime

import re
from datetime import *


class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.type = type
        self.state = state
        self.company = company
        self.country = country
        self.city = city
        self.street = street
        self.phone = phone
        self.email = email
        self.name = name

    def validation(self):
        if type(self.name) is int or type(self.city) is int or type(self.state) is int or type(self.country) is int:
            raise ValueError("Invalid Type Enter")

    def valid_phone(self):
        if type(self.phone) is not int or len(str(self.phone)) != 10:
            raise ValueError("Invalid Phone Number")

    def valid_email(self):
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', self.email) or type(self.email) is int:
            raise ValueError("Invalid email format.")


company_customer = Customer(name="Sunny", company=None, country='India', street="Abc Street", state="Gujarat",
                            city="Rajkot", email="Suuny@gmail.com", phone=9865321470, type="Company")
contact_customer = Customer(name="Justdial", country="India", street="Xyz Street", company=company_customer,
                            phone=9874563021, email="Justdial@gmail.com", state="Rajasthan", city="Jaipur",
                            type="Contact")
billing_customer = Customer(name="Miracle", country="India", city="Upleta", company=company_customer, street="New Abc",
                            state="Gujarat", email="Miracle@gmail.com", phone=9876652301, type="Billing")

shipping_customer = Customer(name="E-kart", street="New Plaza Road", state="Karnataka", city="Bengaluru",
                             company=company_customer, country="India", email="Ekart@gmail.com", phone=98786355412,
                             type="shipping")


# Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
# "company", "billing", "shipping" are objects of Customer.
# "date" must be today or the future. Does not allow past date.
# "total_amount" auto calculated based on different products inside order.
# "order_lines" is list of objects of "OrderLine"
# create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
# "order" is the object of Order.
# "subtotal" is auto calculated based on quantity and price.
class Order:
    def __init__(self, number, company, shipping, billing, date, order_lines):
        self.number = number
        self.company = company
        self.shipping = shipping
        self.billing = billing
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.order_lines = order_lines
        self.datevalid()

    def datevalid(self):
        current_date = datetime.now().date()
        if self.date >= current_date:
            pass
            #     print(self.date)
        else:
            print("Past Date Entered")

    def total(self):
        total_amount = 0
        for i in self.order_lines:
            total_amount += i.subtotal
            # print(total_amount)


class OrderLine:
    def __init__(self, order, quantity, price, product):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calc()
        # print(self.subtotal)

    def calc(self):
        return self.quantity * self.price


Apple = OrderLine(order=None, quantity=5, price=65999, product="iphone-12")
Mi = OrderLine(order=None, quantity=2, price=16999, product="MiNote-10")

Banana = OrderLine(order=None, quantity=25, price=15, product="Banana")
Orange = OrderLine(order=None, quantity=50, product="Oranges", price=21)

i_20 = OrderLine(order=None, quantity=10, price=159999, product="i-20")
HondaCity = OrderLine(order=None, quantity=6, product="Honda-City", price=175999)

Tomato = OrderLine(order=None, quantity=50, product="Tomato", price=20)
Potato = OrderLine(order=None, quantity=100, product="Potato", price=20)
Onion = OrderLine(order=None, quantity=75, price=18, product="Onion")

order_mobiles = Order(number=1, company=company_customer, shipping=shipping_customer, billing=billing_customer,
                      date="2023-12-31", order_lines=[Apple, Mi])
order_vegetables = Order(number=2, company=company_customer, shipping=shipping_customer, billing=billing_customer,
                         date="2024-01-21", order_lines=[Tomato, Potato, Onion])
order_cars = Order(number=3, company=company_customer, billing=billing_customer, shipping=shipping_customer,
                   date="2023-07-30", order_lines=[HondaCity, i_20])
order_fruits = Order(number=4, company=company_customer, shipping=shipping_customer, billing=billing_customer,
                     date="2023-06-23", order_lines=[Banana, Orange])

Apple.order = order_mobiles
Mi.order = order_mobiles

i_20.order = order_cars
HondaCity.order = order_cars

Orange.order = order_fruits
Banana.order = order_fruits

Tomato.order = order_vegetables
Onion.order = order_vegetables
Potato.order = order_fruits

# Display Order and Customer Information
# Sort orders based on "date".
# User can filter the current month orders
# Search Orders from its number.
# List/Display all orders of a specific product.
#
Order_List = [order_mobiles, order_cars, order_fruits, order_vegetables]
today = datetime.today()

for i in Order_List:
    if i.date.month == today.month:
        print("This Month Order No: ", i.number, "\n""Date is: ", i.date, "\n")


def sort_by_date(list1):
    length = len(list1)
    for i in range(0, length - 1):
        for j in range(length - i - 1):
            if list1[j].date > list1[j + 1].date:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


# sort_by_date(Order_List)

# for i in Order_List:
#     print("Date:", i.date, '\n'"Order-No: ", i.number)


def order_no(no):
    for i in Order_List:
        if i.number == no:
            print(i.company, i.date)
            break
        else:
            print("No Order Found")
#
#
# order_no(no=2)
