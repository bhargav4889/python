# Example-2

import re

# --dict--#
user_info = {}


# ----functions----#


def add_insert(key, value):
    user_info[key] = value


def update_email(email_id):
    if email_id == user_info['email']:
        print("Your Info: ", user_info)
        while True:
            print("=== Update Info ===")
            print("1). Update your first name")
            print("2). Update your last name")
            print("3). Update your age")
            print("4). Update your email")
            print("5). Update your address")
            print("6). Update your phone")
            print("0). Exit(Stop)")

            updatechoice = int(input('Select Option to Update: '))

            if updatechoice == 1:
                print('Current Firstname is: ', user_info['firstname'])
                newfirstname = input("Enter New Firstname: ")
                while not newfirstname:
                    print("Firstname not should be Blank ")
                    newfirstname = input("Enter New Firstname(Required): ")
                else:
                    user_info['firstname'] = newfirstname
                    print("Successfully Firstname Updated !")
                    print("New Firstname is ", user_info['firstname'])

            elif updatechoice == 2:
                print('Current Lastname is: ', user_info['lastname'])
                newlastname = input("Enter New Lastname: ")
                while not newlastname:
                    print("Lastname not should be Blank ")
                    newlastname = input("Enter New Lastname(Required): ")
                else:
                    user_info['lastname'] = newlastname
                    print("Successfully Lastname Updated !")
                    print('New Lastname is: ', user_info['lastname'])

            elif updatechoice == 3:
                newage = int(input("Enter New Age: "))
                user_info['age'] = newage

            elif updatechoice == 4:
                print("Current Email is: ", user_info['email'])
                newemail = input("Enter New Email: ")
                while not email:
                    print("Email Should not blank")
                    newemail = input("Enter New Email(Required): ")
                else:
                    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                    if re.fullmatch(reg, newemail):
                        user_info['email'] = newemail
                        print("Successfully Email Updated !")
                        print("New Email is: ", user_info['email'])

            elif updatechoice == 5:
                print("Current Address is: ", user_info['address'])
                newaddress = input("Enter New Address: ")
                while not newaddress:
                    print("Address should not blank")
                    newaddress = input("Enter New Address(Required)")
                else:
                    user_info['address'] = newaddress
                    print("Successfully Address Updated !")
                    print("New Address is: ", user_info['address'])

            elif updatechoice == 6:
                newphone = int(input('Enter New Phone: '))
                user_info['phone'] = newphone

            elif updatechoice == 0:
                break
    else:
        print('Please Enter Correct Email')


def display_user_info():
    print(user_info)


# -----------------#
while True:
    print("1). Add Details")
    print("2). Update Details")
    print("3). Print Details")
    print("4). Exit Details")
    choice = int(input("Select Option: "))
    if choice == 1:
        while True:
            print("===== User'S Info ====")
            print("1). Enter your first name")
            print("2). Enter your last name")
            print("3). Enter your age")
            print("4). Enter your email(Required)")
            print("5). Enter your address")
            print("6). Enter your phone")
            print("0). Exit(Stop)")
            newchoice = int(input("Select Option: "))

            if newchoice == 0:
                break

            elif newchoice == 1:
                Firstname = input("Enter First Name: ")
                while not Firstname:
                    print("Firstname not should be Blank ")
                    Firstname = input("Enter First Name: ")
                else:
                    add_insert('firstname', Firstname)
                    print('Successfully Add')

            elif newchoice == 2:
                Lastname = input("Enter Last Name: ")
                while not Lastname:
                    print("Lastname not should be Blank ")
                    Lastname = input("Enter Lastname Name: ")
                else:
                    add_insert('lastname', Lastname)
                    print('Successfully Add')

            elif newchoice == 3:
                Age = (input("Enter Your Age: "))

            elif newchoice == 4:
                Email = input("Enter Your Email (Required): ")
                while not Email:
                    print("Email is required!")
                    Email = input("Enter your email (Required): ")
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if re.fullmatch(regex, Email):
                    add_insert('email', Email)
                    print('Successfully Add')
                else:
                    print("Enter correct Email: ")
                    Email = input("Enter Email Again: ")

            elif newchoice == 5:
                Address = input("Enter Your Address: ")
                while not Address:
                    print("Address not should be Blank ")
                    Address = input("Enter Address(Required): ")
                else:
                    add_insert('address', Address)
                    print('Successfully Add')
            elif newchoice == 6:
                Phone = (input("Enter Phone Number: "))
                if len(Phone) == 10 & Phone.isdigit():
                    add_insert('phone', Phone)
                else:
                    print("Enter Vaild Phone Number: ")
                    Phone = input("Enter Again Phone: ")

    elif choice == 2:
        email = input('Enter Email: ')
        update_email(email_id=email)

    elif choice == 3:
        display_user_info()

    elif choice == 4:
        break
