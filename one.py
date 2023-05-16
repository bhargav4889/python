# Example-1

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
                newfirstname = input("Enter New Firstname: ")
                user_info['firstname'] = newfirstname

            elif updatechoice == 2:
                newlastname = input("Enter New Lastname: ")
                user_info['lastname'] = newlastname

            elif updatechoice == 3:
                newage = int(input("Enter New Age: "))
                user_info['age'] = newage

            elif updatechoice == 4:
                newemail = input("Enter New Email: ")
                user_info['email'] = newemail

            elif updatechoice == 5:
                newaddress = input("Enter New Address: ")
                user_info['address'] = newaddress

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
            print("4). Enter your email")
            print("5). Enter your address")
            print("6). Enter your phone")
            print("0). Exit(Stop)")
            newchoice = int(input("Select Option: "))

            if newchoice == 0:
                break

            elif newchoice == 1:
                Firstname = input("Enter First Name: ")
                add_insert('firstname', Firstname)

            elif newchoice == 2:
                Lastname = input("Enter Last Name: ")
                add_insert('lastname', Lastname)

            elif newchoice == 3:
                Age = int(input("Enter Your Age: "))
                add_insert('age', Age)

            elif newchoice == 4:
                Email = input("Enter Your Email: ")
                add_insert('email', Email)

            elif newchoice == 5:
                Address = input("Enter Your Address: ")
                add_insert('address', Address)

            elif newchoice == 6:
                Phone = int(input("Enter Phone Number: "))
                add_insert('phone', Phone)

    elif choice == 2:
        email = input('Enter Email: ')
        update_email(email_id=email)

    elif choice == 3:
        display_user_info()

    elif choice == 4:
        break
