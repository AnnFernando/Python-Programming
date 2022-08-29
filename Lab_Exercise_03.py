"""
Application file:               Lab_Exercise_03.py
Author/Programmer:              Ann Fernando
Application Created Date:       27th January 2022
Description:                    This is a vehicle registration application where it registers a vehicle with a unique
                                identity which is Vehicle Insurance Number(VIN).

                                The application provides a menu with six options
                                    1.Register a vehicle
                                    2.Search a vehicle by Make
                                    3.Search a vehicle by VIN
                                    4.Remove a vehicle by VIN
                                    5.Display all registered vehicles
                                    2.End Application

                                User inputs are make, color and VIN of the vehicle.

"""


def main():
    """
    Function Name:              main()
    Author/Programmer:          Ann Fernando
    Date of implementation:     27th January 2022
    :return:                    None

    Description:                This function gets user inputs on vehicle details : make, color and VIN and registers
                                a vehicle with the unique identity of VIN.

                                This performs several validations on following and displays appropriate error messages
                                to the user.
                                1.The user entered menu option is validated
                                2.The user entered VIN is validated. (should be unique)
                                3.When searching a vehicle by make, user entered brand is validated
                                4.When searching a vehicle by VIN, user entered VIN is validated
                                5.When removing a vehicle by VIN, user entered VIN is validated

    """

    menu = """
        Vehicle Registration Application
        
        1.  Enter 1 to : Register a vehicle
        2.  Enter 2 to : Search a vehicle by Make
        3.  Enter 3 to : Search a vehicle by Vehicle Identifier (VIN)
        4.  Enter 4 to : Remove a vehicle by Vehicle Identifier (VIN)
        5.  Enter 5 to : Display all registered vehicles
        6.  Enter 6 to : End Application
    """
    vehicles = []

    while True:
        print(menu)
        print("Please enter a valid menu option...")
        option = input("Enter your menu option : \t")
        heading = "%120s\n%120s\n\n%40s%40s%40s\n" % ("Ann Fernando", "N01517411", "Make of Vehicle", "Color of Vehicle"
                                                      , "VIN of Vehicle")
        if option == '1':
            # registering a new vehicle and display the registered
            make = input("Enter the make of the vehicle : \t")
            color = input("Enter the color of the vehicle : \t")
            vin = input("Enter the VIN of the vehicle : \t\t")
            # if vin is empty ask the user to re-enter
            if not vin:
                print("Please enter VIN of the vehicle. It is mandatory for the vehicle registration.")
                vin = input("Enter the VIN of the vehicle : \t")
            onevehicle = [make, color, vin]

            # Registering the first vehicle in the system
            if not vehicles:
                print("\nNo registered vehicle in the system. Registering the first vehicle...")
                vehicles.append(onevehicle)
                print("Vehicle of Make : {}, Color : {} and VIN : {} is successfully registered".format(make, color,
                                                                                                        vin))
                print(heading + "%40s%40s%40s\n" % (vehicles[0][0], vehicles[0][1], vehicles[0][2]))
            else:
                # Validates VIN before registering
                print("Checking available records on the validity of entered VIN...")
                record_exists = False
                for i in range(len(vehicles)):
                    if vehicles[i][2] == vin:
                        print("Entered VIN is already registered in the system. \nPlease enter valid details.")
                        record_exists = True
                        break
                if not record_exists:
                    vehicles.append(onevehicle)
                    print("Vehicle of Make : {}, Color : {} and VIN : {} is successfully registered".format(make,
                                                                                                            color, vin))
                    print(heading + "%40s%40s%40s\n" % (vehicles[-1][0], vehicles[-1][1], vehicles[-1][2]))

        elif option == '2':
            # Searching the vehicle by Make
            makesearch = input("Please enter the make of the vehicle for searching : ")
            makestring = ""
            for i in range(len(vehicles)):
                if vehicles[i][0] == makesearch:
                    makestring += "%40s%40s%40s\n" % (vehicles[i][0], vehicles[i][1], vehicles[i][2])

            if not makestring:
                print("No vehicle has been registered with the Make {}".format(makesearch))
            else:
                print(heading+makestring)

        elif option == '3':
            # Searching the vehicle by VIN
            vinsearch = input("Please enter the VIN of the vehicle for searching : ")
            if not vehicles:
                print("No vehicle has been registered with the VIN {}".format(vinsearch))
            for i in range(len(vehicles)):
                if vehicles[i][2] == vinsearch:
                    print(heading + "%40s%40s%40s\n" % (vehicles[i][0], vehicles[i][1], vehicles[i][2]))
                    break
                elif i + 1 is len(vehicles):
                    print("No vehicle has been registered with the VIN {}".format(vinsearch))

        elif option == '4':
            # Removing the vehicle when VIN is given
            vindelete = input("Please enter the VIN of the vehicle for removing the registered record : ")
            if not vehicles:
                print("No vehicle has been registered with the VIN {}".format(vindelete))
            for i in range(len(vehicles)):
                if vehicles[i][2] == vindelete:
                    del vehicles[i]
                    print("Vehicle with VIN {} is now removed from the system".format(vindelete))
                    break
                elif i + 1 is len(vehicles):
                    print("No vehicle has been registered with the VIN {}".format(vindelete))

        elif option == '5':
            # Displaying registered vehicle records

            if not vehicles:
                print("No vehicles have been registered in the system.")
            else:
                vehicle_string = ""
                for i in range(len(vehicles)):
                    vehicle_string += "%40s%40s%40s\n" % (vehicles[i][0], vehicles[i][1], vehicles[i][2])

                print("\nDisplaying all registered vehicles...\n\n"+heading + vehicle_string)

        elif option == '6':
            print("Application is Ended.")
            break
        else:
            print("Please enter a valid menu option : from 1 to 6 inclusive...")


main()
