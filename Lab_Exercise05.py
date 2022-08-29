"""
Application file:               Lab_Exercise_05.py
Author/Programmer:              Ann Fernando
Application Created Date:       10th February 2022
Description:                    This is a Banking application where it creates chequing accounts for the users.
                                Application creates an account and all transactions of this account are saved in file.

                                The application provides a menu with four options
                                    1.Deposit Amount
                                    2.Show all transactions
                                    3.Withdraw amount
                                    4.End Application

                                User inputs are account number, amount to be deposited and amount to be withdrawn.
"""


def display_menu():
    """
    Function Name:              display_menu()
    Author/Programmer:          Ann Fernando
    Date of implementation:     10th February 2022
    Parameters passed:          None
    :return:                    User selected menu option

    Description:                This function displays the menu options to the user and input the user option and return
                                it to the main function.

    """
    menu = """
            1. Enter 'd' to: Deposit Amount
            2. Enter 't' to: Show all transactions
            3. Enter 'w' to: Withdraw amount
            4. Enter 'e' to: End Application     
           """
    print(menu)
    option = input("\nEnter your menu option : \t")
    return option


def deposit_amount(account_no):
    """
    Function Name:              deposit_amount(account_no)
    Author/Programmer:          Ann Fernando
    Date of implementation:     10th February 2022
    Parameters passed:          account_no
    :return:                    none

    Description:                This function receives the account number and asks for user the amount to be deposited.
                                The user entered amount will be deposited to the account. Displays a success message
                                once successfully deposited.
    """
    import datetime
    import re

    amount = input("Enter the amount to be deposited :\t")
    if float(amount) < 0:
        print("$" + str(float(amount)) + " is not a valid amount to be deposited...")
        print("%50s" % "...Transaction is completed...")
    else:
        account = open(account_no, 'r')
        records = account.readlines()
        lastrecord = re.split("[:,{}\']", records[-1])
        account.close()

        datetime_str = datetime.datetime.now().strftime("%d/%m/%Y") + " at " \
                       + datetime.datetime.now().strftime("%H:%M:%S")
        transaction_info = {'transaction': 'Deposit Amount', 'completion': datetime_str,
                            'prev_bal': float(lastrecord[26].strip()), 'trans_amount': float(amount),
                            'balance': (float(lastrecord[26].strip()) + float(amount))}
        account = open(account_no, 'a')
        account.write(str(transaction_info) + "\n")
        account.close()
        print("Balance before the current deposit :\t")
        print("%50s" % ("$" + amount + " is successfully deposited..."))


def display_transactions(account_no):
    """
    Function Name:              display_transactions(account_no)
    Author/Programmer:          Ann Fernando
    Date of implementation:     10th February 2022
    Parameters passed:          account_no
    :return:                    none

    Description:                This function receives the account number and displays all the transactions related to
                                that account number in a tabular format.
    """
    import re
    account_info = open(account_no, 'r')
    heading = "%120s\n%120s\n\n%80s\n%75s\n\n%24s%24s%24s%24s%24s\n" % ("Ann Fernando", "N01517411",
                                                                        "Transaction Details...", "Account No : "
                                                                        + account_no, "Transaction Type",
                                                                        "Trans. Completed On", "Previous Balance",
                                                                        "Trans. Amount", "Balance")
    print(heading)
    transaction = {}
    for transaction_line in account_info:
        transaction = transaction_line.strip()
        record = re.split("[:,{}\']", transaction)
        print("%22s%26s%24s%24s%24s\n" % (record[5].strip(), record[11].strip() + ":" + record[12].strip() + ":"
                                          + record[13].strip(), "$" + record[18].strip(), "$" + record[22].strip(),
                                          "$" + record[26].strip()))
    account_info.close()


def withdraw_amount(account_no):
    """
    Function Name:              withdraw_amount(account_no)
    Author/Programmer:          Ann Fernando
    Date of implementation:     10th February 2022
    Parameters passed:          account_no
    :return:                    none

    Description:                This function receives the account number and asks for user the amount to be withdrawn.
                                The user entered amount will be withdrawn from the account. Displays a success message
                                once successfully withdrawn.
    """
    import datetime
    import re

    amount = input("Enter the amount to be withdrawn :\t")
    if float(amount) < 0:
        print("$" + amount + " is not a valid amount to be withdrawn...")
        print("%50s" % "...Transaction is completed...")
    else:
        account = open(account_no, 'r')
        records = account.readlines()
        lastrecord = re.split("[:,{}\']", records[-1])
        account.close()

        if float(amount) > float(lastrecord[26]):
            print("Transaction is failed. No sufficient amount in the account.")
            print("Amount : $" + amount + "is higher than the current balance of the account : $" + lastrecord[26])
        else:
            datetime_str = datetime.datetime.now().strftime("%d/%m/%Y") + " at " \
                           + datetime.datetime.now().strftime("%H:%M:%S")
            transaction_info = {'transaction': 'Withdraw Amount', 'completion': datetime_str,
                                'prev_bal': float(lastrecord[26]), 'trans_amount': float(amount),
                                'balance': (float(lastrecord[26].strip("\'")) - float(amount))}
            account = open(account_no, 'a')
            account.write(str(transaction_info) + "\n")
            account.close()
            print("Balance before the current withdrawal :\t")
            print("%50s" % ("$" + amount + " is successfully withdrawn..."))


def main():
    """
    Function Name:              display_menu()
    Author/Programmer:          Ann Fernando
    Date of implementation:     10th February 2022
    Parameters passed:          None
    :return:                    User selected menu option

    Description:                This function displays the menu options to the user and input the user option and return
                                it to the main function.
    """
    import os
    import datetime
    transaction_info = {}
    account_no = ""
    while True:
        if account_no == "":
            account_no = input("Enter Account Number:\t")
        if not os.path.exists(account_no):
            print("Creating a new bank account...")
            datetime_str = datetime.datetime.now().strftime("%d/%m/%Y") + " at " \
                           + datetime.datetime.now().strftime("%H:%M:%S")
            transaction_info = {'transaction': 'Open Account', 'completion': datetime_str,
                                'prev_bal': 0.00, 'trans_amount': 0.00, 'balance': 0.00}
            account = open(account_no, 'a')
            string = str(transaction_info) + '\n'
            account.write(string)
            account.close()
        else:
            print("Account exists...")

        option = display_menu()

        if option == 'd':
            deposit_amount(account_no)
        elif option == 't':
            display_transactions(account_no)
        elif option == 'w':
            withdraw_amount(account_no)
        elif option == 'e':
            print("\n Application is ended!")
            break
        else:
            print("\n Please enter a valid option from : 'd', 't', 'w' or 'e'...")


main()
