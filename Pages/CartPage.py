# Print the list of items, let the staff select the items to add. Then on completion return the list of menu items back.
# Can remove items.
import os

from DatabaseConnection import DatabaseConnection
from MainClasses.Cart import Cart
from Managers.MenuManager import MenuManager
from OptionSelection import OptionSelection

db = DatabaseConnection()
menu_manager = MenuManager(db)
menu_manager.readItemsFromDB()


INIT_OPTIONS = ["Add an Item", "Remove an Item", "Checkout"]


class CartPage:
    def __init__(self):
        self.cart = Cart()

    def display(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.printCurrentCart()

            selection_index = OptionSelection.show(
                INIT_OPTIONS, "Cart Menu Options: ", "Cancel"
            )
            os.system("cls" if os.name == "nt" else "clear")

            match selection_index:
                case 0:
                    self.addItem()
                case 1:
                    self.removeItem()
                case 2:
                    return self.cart

                case -1:
                    break
        return None

    def printCurrentCart(self):
        if len(self.cart.getAllItems()) > 0:
            print("-----------------------------")
            print("Current Cart")
            for item in self.cart.getAllItems():
                print(f"{item.getName()} - {item.getPrice()}")
            print("-----------------------------")

    def addItem(self):
        item_list = [
            item.name + " - $" + str(item.price) for item in menu_manager.getAllItems()
        ]
        while True:
            self.printCurrentCart()
            item_index = OptionSelection.show(
                item_list, "Select an Item to add: ", "Done"
            )
            if item_index > -1:
                item = menu_manager.getItem(item_index)
                if not item:
                    break
                self.cart.addItem(item)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Added {item.getName()}.")
            else:
                break

    def removeItem(self):
        if len(self.cart.getAllItems()) > 0:
            while True:
                item_list = [
                    item.name + " - $" + str(item.price)
                    for item in self.cart.getAllItems()
                ]
                self.printCurrentCart()
                item_index = OptionSelection.show(
                    item_list, "Select an Item to remove: ", "Done"
                )
                if item_index > -1:
                    self.cart.removeItem(item_index)
                    os.system("cls" if os.name == "nt" else "clear")
                    item = self.cart.getItem(item_index)
                    if not item:
                        break
                    print(f"Removed {item.getName()}.")
                else:
                    break

        else:
            print("There are no items to remove.")
