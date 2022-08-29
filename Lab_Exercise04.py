"""
Application file:               Lab_Exercise_04.py
Author/Programmer:              Ann Fernando
Application Created Date:       03rd February 2022
Description:                    This is a warehouse inventory application where it stores information about the sales
                                items and allows the user to perform below given activities.

                                The application provides a menu with five options
                                    1.Add an inventory
                                    2.Perform inventory sales
                                    3.Display all inventory
                                    4.Check inventory item in stock
                                    5.End Application

                                User inputs are item name, item identifier (ID), item location in the warehouse,
                                item quantity and unit price of item.

"""


def add_items(inventory):
    """
    Function Name:              add_items(inventory)
    Author/Programmer:          Ann Fernando
    Date of implementation:     03rd February 2022
    Parameters passed:          inventory dictionary data structure
    :return:                    inventory dictionary data structure

    Description:                This function gets user inputs on the item to be added to the inventory : item name,
                                item identifier (ID), item location in the warehouse, item quantity and
                                unit price of item

                                This performs several checks.
                                a) If inventory is empty directly add the user item to the inventory
                                b) If no match found for the item in the inventory directly add the item
                                   to the directory
                                c) If item is existing, then new quantity, price and location is updated accordingly


    """
    item_name = input("Enter the name of the item:\t")
    item_id = input("Enter the Item ID:\t")
    ilocation = input("Enter the location to be stored in shelf: \t")
    iquantity = input("Enter the quantity of the item: \t")
    unit_price = input("Enter the unit price of the item:\t")

    index = len(inventory)
    # Inventory has no stock, so directly adding the user item.
    if not inventory:
        print("\nNo existing items in the inventory..Registering as a new item...\n")
        inventory = {++index: {"name": item_name.strip(), "itemid": item_id.strip(), "location": ilocation.strip(),
                               "quantity": int(iquantity), "uprice": '%.2f' % float(unit_price)}}
        print("Item : {} with Item ID : {} is successfully added to the inventory\n".format(item_name, item_id))
    else:
        # Inventory is not empty, search for an item match
        record_exists = False
        for item_index in inventory:
            # item exists in the inventory
            if inventory[item_index]["name"] == item_name and inventory[item_index]["itemid"] == item_id:
                print("\nItem exists in the inventory...The entered details will be added to the existing record of "
                      "the item...\n")
                record_exists = True
                # if location has changed, update the new location
                if inventory[item_index]["location"] != ilocation:
                    print("Item exists in the inventory... New location : {} is updated.".format(ilocation))
                    inventory[item_index]["location"] = ilocation.strip()
                # if unit price has changed update the new unit price
                if inventory[item_index]["uprice"] != '%.2f' % float(unit_price):
                    print("Item exists in the inventory... New unit price : ${} is updated."
                          .format('%.2f' % float(unit_price)))
                    inventory[item_index]["uprice"] = '%.2f' % float(unit_price)
                # update the quantity
                print("Item exists in the inventory... Quantity is increased to {}."
                      .format(inventory[item_index]["quantity"] + int(iquantity)))
                inventory[item_index]["quantity"] += int(iquantity)
                break
        # No item with the same name and ID exists in the inventory. Adding the item info to the inventory.
        if not record_exists:
            print("The item entered is a new item...Adding it to the inventory...\n")
            inventory[++index] = {"name": item_name.strip(), "itemid": item_id.strip(), "location": ilocation.strip(),
                                  "quantity": int(iquantity), "uprice": '%.2f' % float(unit_price)}
            print("Item : {} with Item ID : {} is successfully added to the inventory\n".format(item_name, item_id))

    return inventory


def sell_item(inventory):
    """
    Function Name:              sell_item(inventory)
    Author/Programmer:          Ann Fernando
    Date of implementation:     03rd February 2022
    Parameters passed:          inventory dictionary data structure
    :return:                    inventory dictionary data structure

    Description:                This function gets user inputs on the item to be purchased from the inventory :
                                item name and item quantity

                                This function checks:
                                If item exists in the inventory and quantity is sufficient to make the purchase, then
                                item is being sold and an invoice is printed with details.
                                Validations are done to display appropriate info messages to the user based on
                                availability of the items in the inventory.

    """
    if not inventory.items():
        print("Sorry! No items exists in the warehouse inventory to make purchases!")
    else:

        print("Please enter the name and the quantity of the item to be purchased...")
        item_name = input("Enter the name of the item:\t")
        iquantity = input("Enter the quantity of the item: \t")

        heading = "%120s\n%120s\n\n%24s%24s%24s%24s%24s\n" % ("Ann Fernando", "N01517411", "Item Name", "Item ID",
                                                              "Item Quantity", "Item Unit Price", "Total Price")
        purchased = False
        for item_index in inventory:
            # item exists in the inventory and quantity is sufficient to make the purchase.
            if inventory[item_index]["name"] == item_name and inventory[item_index]["quantity"] >= int(iquantity):
                print("\nItem exists in the inventory...The transaction is in progress...")
                inventory[item_index]["quantity"] -= int(iquantity)
                purchased = True
                index = item_index
                break

        if purchased:
            total_price = int(iquantity) * float(inventory[index]["uprice"])
            tax_amount = 0.13 * int(iquantity) * float(inventory[index]["uprice"])
            print(heading + "%24s%24s%24s%24s%24s\n%90s%30s\n%90s%30s\n" % (inventory[index]["name"],
                                                                            inventory[index]["itemid"],
                                                                            int(iquantity),
                                                                            inventory[index]["uprice"], "$" +
                                                                            '%.2f' % total_price,
                                                                            "Tax Amount:", "$" + '%.2f' % tax_amount,
                                                                            "Total Amount to pay:",
                                                                            "$" + '%.2f' % (total_price + tax_amount)))
        else:
            print("\nSorry..The item requested with the required quantity is not available "
                  "currently at the inventory...")
            print("We don't have item {} in quantity {} currently in the stock".format(item_name, iquantity))

    return inventory


def display_inventory(inventory):
    """
    Function Name:              display_inventory(inventory)
    Author/Programmer:          Ann Fernando
    Date of implementation:     03rd February 2022
    Parameters passed:          inventory dictionary data structure
    :return:                    none

    Description:                This function displays the inventory items in a tabular format.

    """

    heading = "%60s\n%120s\n%120s\n\n%24s%24s%24s%24s%24s\n" % ("List of Inventory Items", "Ann Fernando", "N01517411",
                                                                "Item Name", "Item ID", "Location in Pods",
                                                                "Price/Unit", "Quantity in stock")
    inventory_string = ""
    for item_index in inventory:
        inventory_string += "%24s%24s%24s%24s%24s\n" % (inventory[item_index]["name"], inventory[item_index]["itemid"],
                                                        inventory[item_index]["location"],
                                                        "$"+inventory[item_index]["uprice"],
                                                        inventory[item_index]["quantity"])

    if inventory_string == "":
        print("No items in the inventory system...")
    else:
        print(heading + inventory_string)


def search_inventory(inventory):
    """
    Function Name:              search_inventory(item, inventory)
    Author/Programmer:          Ann Fernando
    Date of implementation:     03rd February 2022
    Parameters passed:          none
    :return:                    A list containing a boolean to check the item existence and inventory data structure.

    Description:                This function searches the user given item in the inventory and once found returns that
                                inventory data back to the main function in a list.

    """
    inventorylist = []
    if not inventory.items():
        print("Sorry! No items exists in the warehouse inventory to search!")

    else:
        item = input("Enter item name to check the existence :\t")
        exists = False
        inventory_item = {}
        # search the item in the inventory
        for item_index in inventory:
            if inventory[item_index]["name"] == item:
                exists = True
                inventory_item = {"name": inventory[item_index]["name"], "itemid": inventory[item_index]["itemid"],
                                  "location": inventory[item_index]["location"],
                                  "uprice": inventory[item_index]["uprice"],
                                  "quantity": inventory[item_index]["quantity"]}
                break

        # The list with boolean parameter exists and inventory item data structure.
        inventorylist = [exists, inventory_item]

    return inventorylist


def main():
    """
    Function Name:              add_items()
    Author/Programmer:          Ann Fernando
    Date of implementation:     03rd February 2022
    Parameters passed:          None
    :return:                    None

    Description:                The main() function displays the menu and according to the user entered option the
                                action is performed.

    """

    menu = """
        Warehouse Inventory Application

        a.  Enter a to : Add an inventory
        b.  Enter b to : Perform inventory sales
        c.  Enter c to : Display all inventory
        d.  Enter d to : Check inventory item in stock
        e.  Enter e to : End Application
    """
    inventory = {}
    heading = "%80s\n%120s\n%120s\n\n%24s%24s%24s%24s%24s\n" % ("Item details from inventory stock.", "Ann Fernando",
                                                                "N01517411", "Item Name", "Item ID", "Location in Pods",
                                                                "Price/Unit", "Quantity in stock")
    while True:
        print(menu)
        print("Please enter a valid menu option...")
        option = input("Enter your menu option : \t")
        if option == 'a':
            inventory = add_items(inventory)
        elif option == 'b':
            inventory = sell_item(inventory)
        elif option == 'c':
            display_inventory(inventory)
        elif option == 'd':
            search_list = search_inventory(inventory)
            if len(search_list) != 0:
                if not search_list[0]:
                    print("Sorry! Searched Item is unavailable!")
                else:
                    print("Item is in stock, details are given below...\n")
                    item_dict = search_list[1].values()
                    print(heading + "%24s%24s%24s%24s%24s\n" % (list(item_dict)[0], list(item_dict)[1],
                                                                list(item_dict)[2], "$"+list(item_dict)[3],
                                                                list(item_dict)[4]))
        elif option == 'e':
            print("Application is Ended.")
            break
        else:
            print("Please enter a valid menu option : from 1 to 5 inclusive...")


main()








