import pickle
import os
import re


def save_data(file_name):
    x1 = [
        {"car_dealer": "ABC Chevy", "vehicle_info": "Ford;VINF01234;White;Sedan;FWD", "city": "Toronto"},
        {"car_dealer": "Nissan North", "vehicle_info": "Nissan;VINN01234;Grey;SUV;AWD", "city": "Thunder Bay"},
        {"car_dealer": "GMC City", "vehicle_info": "GMC;VINGMC01234;Black;Truck;AWD", "city": "Toronto"},
        {"car_dealer": "Lexus GTA", "vehicle_info": "Lexus;VINL01234;White;SUV;AWD", "city": "Markham"},
        {"car_dealer": "Nissan GTA", "vehicle_info": "Nissan;VINN4567;White;Sedan;FWD", "city": "Brampton"}
    ]

    file_info = open(file_name, 'ab')
    for data in x1:
        pickle.dump(data, file_info)

    file_info.close()


def search_info(file_name):
    """
    Function Name:              search_info(file_name)
    Author/Programmer:          Ann Fernando
    Date of implementation:     22nd February 2022
    Parameters passed:          file_name
    :return:                    none

    Description:                This function receives the file name.It asks the user to enter the vehicle make for
                                the search. It displays the information if the user entered make does exist in the data
                                file. If no data exits then displays a message.
    """

    # file with vehicle data exists
    if os.path.exists(file_name):
        # user input : vehicle make
        vehicle_make = input("Enter the vehicle make for searching :\t")
        vehicle_data = open(file_name, 'r')
        vehicle_data1 = vehicle_data.readlines()
        index = 0
        record_exits = False
        heading = "%120s\n%120s\n\n%20s%20s%20s%20s%20s%20s\n" % ("Ann Fernando", "N01517411", "Dealer Name",
                                                                  "Vehicle Make", "City", "Vehicle Color",
                                                                  "Vehicle Type", "Drive Type")
        record = ""
        for vehicle_data1 in vehicle_data:
            print(vehicle_data1)
            # checks for the make of the vehicle
            if (vehicle_make.strip()) in vehicle_data1['car_dealer']:
                record_exits = True
                print(heading)
                vehicle_details = re.split(";", vehicle_data1['vehicle_info'])
                record += "%20s%20s%20s%20s%20s%20s\n" % (vehicle_data1[index]['car_dealer'], vehicle_data1['car_dealer'],
                                                          vehicle_details[0], vehicle_details[2], vehicle_details[3],
                                                          vehicle_details[4])
            ++index
        # display the information
        if record_exits:
            print(heading)
            print(record)
        else:
            print("Vehicle is not available at any dealership...")
    # file with vehicle data doesn't exist
    else:
        print("SYSTEM ERROR! NO DATA FILE FOUND!")


def main():
    file_name = "Vehicles"
    file_info = open(file_name, "a")
    file_info.close()

    choices = """
                1. Enter 1 to save data
                2. Enter 2 to search a vehicle
                3. Enter 3 to end application

    """
    while True:
        print(choices)
        my_choice = input("Enter your choice\t")
        if my_choice == '1':
            save_data(file_name)
        elif my_choice == '2':
            search_info(file_name)
        elif my_choice == '3':
            print("Application ending...\n")
            break
        else:
            print("Enter valid input ......")


main()

"""

In this application, you can search vehicle by its make (e.g. Ford, GMC, Nissan etc.)
When you execute option 1, function save_data(file_name) is executed that will save data in the file.

Source code for main function is given below:


def main():
    file_name = "File name goes here"
    file_info = open(file_name, "MODE")
    file_info.close()

    choices = '''
                1. Enter 1 to save data
                2. Enter 2 to search a vehicle
                3. Enter 3 to end application

    '''
    while True:
        print(choices)
        my_choice = input("Enter your choice\t")
        if my_choice == '1':
            save_data(file_name)
        elif my_choice == '2':
            search_info(file_name)
        elif my_choice == '3':
            print("Application ending...\n")
            break
        else:
            print("Enter valid input ......")


main()




Function save_data (file_name) is given below:


def save_data(file_name):
    x1 = [
          {"car_dealer": "ABC Chevy", "vehicle_info": "Ford;VINF01234;White;Sedan;FWD", "city": "Toronto"},
          {"car_dealer": "Nissan North", "vehicle_info": "Nissan;VINN01234;Grey;SUV;AWD", "city": "Thunder Bay"},
          {"car_dealer": "GMC City", "vehicle_info": "GMC;VINGMC01234;Black;Truck;AWD", "city": "Toronto"},
          {"car_dealer": "Lexus GTA", "vehicle_info": "Lexus;VINL01234;White;SUV;AWD", "city": "Markham"},
          {"car_dealer": "Nissan GTA", "vehicle_info": "Nissan;VINN4567;White;Sedan;FWD", "city": "Brampton"}

          ]

    file_info = open(file_name, "MODE to open file")
    for data in x1:
        pickle.dump(data, file_info)

    file_info.close()




Your task:
write function search_info(file_name) 

Information saved in the file is of the format:

  {"car_dealer": "Nissan GTA", "vehicle_info": "Nissan;VINN4567;White;Sedan;FWD", "city": "Brampton"}

This dictionary structure has:

"car_dealer" as a key, "vehicle_info" as a key and "city" as a key

 For the key "car_dealer", value associated to the key is a string which has car_dealer name

 For the key "vehicle_info", value associated to the key is a string, which has first value car manufacturer, second value in
 the string is VIN number of the vehicle, third value in the string is the color of the vehicle and fourth value in the string
 is vehicle type (e.g. sedan, SUV, sports etc.) and fifth element in the string is drive type (e.g. FWD, AWD etc.)

 For the key "city", the value associated to the key is the string city name.


Your task is to implement function search_info(file_name)
The application asks user to enter the vehicle make that you are looking for?

User enters the vehicle make. This information is in the string "vehicle_info".

If the vehicle is NOT in the file, then following information is displayed:


Enter your choice	2
Enter vehicle make that you are looking for:	Mitsubishi
Vehicle is not available at any dealership..

                1. Enter 1 to save data
                2. Enter 2 to search a vehicle
                3. Enter 3 to end application


If the vehicle is found then following information is displayed:


Enter your choice	2
Enter vehicle make that you are looking for:	Lexus
                                                                                                                     Muhammad Khan
                                                                                                                           N012345
                   Dealer Name        Vehicle Make                City            Vehicle Color        Vehicle Type     Drive Type
                     Lexus GTA               Lexus             Markham                    White                 SUV            AWD


                1. Enter 1 to save data
                2. Enter 2 to search a vehicle
                3. Enter 3 to end application

If there are more than one vehicles, then following information is displayed showing multiple vehicles:


Enter your choice	2
Enter vehicle make that you are looking for:	Nissan
                                                                                                                     Muhammad Khan
                                                                                                                           N012345
                   Dealer Name        Vehicle Make                City            Vehicle Color        Vehicle Type     Drive Type
                  Nissan North              Nissan         Thunder Bay                     Grey                 SUV            AWD
                    Nissan GTA              Nissan            Brampton                    White               Sedan            FWD


                1. Enter 1 to save data
                2. Enter 2 to search a vehicle
                3. Enter 3 to end application


"""