"""
Application file:               Lab_Exercise2.py
Author/Programmer:              Ann Fernando
Application Created Date:       20th January 2022
Description:                    This is a customer registration application where it registers customers and displays
                                the registered customers.

                                The application provides a menu with two options
                                    1.Registering a customer and view all registered customers
                                    2.End Application

                                User inputs are customer full name , customer email address and customer address.
                                Each customer is registered based on the unique identity which is the email address.

"""


def main():

    """
    Function Name:              main()
    Author/Programmer:          Ann Fernando
    Date of implementation:     20th January 2022
    :return:                    None

    Description:                This function gets user inputs on customer details : customer full name , customer email
                                address and customer address and registers a customer with the unique identity of email
                                ID. Validates whether the menu option is valid, the user entered email ID is unique and
                                displays appropriate error messages to the user.

    """

    menu = """
    1.  Enter 1 to register a customer and display all registered customers
    2.  Enter 2 to end application
    """

    customer_info = ""
    customer_exists = False

    while True:
        print(menu)
        option = input("Enter your option from the menu : \t")
        if option == '1':
            print("Please enter valid customer details...")
            full_name = input("Enter Full Name : \t")
            email = input("Enter Email ID : \t")
            address = input("Enter Address : \t")

            # No previous records exists.
            if customer_info == "":
                print("First customer is being registered...")
                customer_info += full_name + "," + email + "," + address
                print("Customer {} with email ID: {} and address: {} is successfully registered!".format(full_name,
                                                                                                        email, address))
            else:
                # Customer records exists. Checking whether the entered customer details are valid.
                customer_records = customer_info.split(';')
                for each_customer in customer_records:
                    customer_fields = each_customer.split(',')
                    if customer_fields[1] == email:
                        print("Customer email address already exists.\nPlease register correct information.")
                        customer_exists = True
                        break
                # No existing customers with given Email ID, So registering the new customer.
                if customer_exists is False:
                    customer_info += ";" + full_name + "," + email + "," + address
                    print("Customer {} with email ID: {} and address: {} is successfully registered!".format(full_name,
                                                                                                             email,
                                                                                                             address))
            # Display of registered customers in a tabular format
            heading = "%120s\n%120s\n\n" % ("Ann Fernando", "N01517411")
            print(heading)
            if customer_info == "":
                print("No customers have been registered")
            else:
                customer_string = "%40s%40s%40s\n" % ("Customer Name", "Customer Email ID", "Customer Address")
                customer_records = customer_info.split(';')
                for each_customer in customer_records:
                    customer_fields = each_customer.split(',')
                    full_name = customer_fields[0]
                    email = customer_fields[1]
                    address = customer_fields[2]
                    customer_string += "%40s%40s%40s\n" % (full_name, email, address)
                print(customer_string)

        elif option == '2':
            print("Application is ended")
            break

        else:
            # User entered menu option is invalid
            print("Please enter a valid option from the menu : Either 1 or 2...")


main()
