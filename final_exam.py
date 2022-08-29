"""
Application file:               final_exam.py
Author/Programmer:              Ann Fernando
Application Created Date:       19th April 2022
Description:                    This has two classes Item and Product where Product class inherits from Item class.
                                Implementation includes str, accessor and mutator methods.
"""


class Item:
    def __init__(self, Item_name=None):
        self.Item_name = Item_name

    def __str__(self):
        Item_information = "Item Name:\t\t\t{}\n".format(self.Item_name)
        return Item_information

    def getItem_name(self):
        return self.Item_name

    def setItem_name(self, Item_name):
        self.Item_name = Item_name


class Product(Item):
    def __init__(self, Item_name=None, product_price=None, product_code=None):
        super().__init__(Item_name)
        self.product_price = product_price
        self.product_code = product_code

    def __str__(self):
        product_info = super().__str__()
        product_info += "Product Price: \t\t${}\nProduct Code:\t\t{}".format(self.product_price, self.product_code)
        return product_info

    def get_product_price(self):
        return self.product_price

    def get_product_code(self):
        return self.product_code

    def set_product_price(self, product_price):
        self.product_price = product_price

    def set_product_code(self, product_code):
        self.product_code = product_code


def main():
    product1 = Product("Computer", 875.55, "C4321")
    product2 = Product("Book", 105.97, "B2134")
    product3 = Product("Computer bag", 85.66, "CB01234")
    print(product1)
    print(product2)
    print(product3)


main()
