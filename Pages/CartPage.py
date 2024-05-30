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
            selection_index = OptionSelection.show(
                INIT_OPTIONS, "Cart Menu Options: ", "Cancel"
            )
            os.system("cls" if os.name == "nt" else "clear")

            match selection_index:
                case 0:
                    item_list = [
                        item.name + " - $" + str(item.price)
                        for item in menu_manager.getAllItems()
                    ]
                    item_index = OptionSelection.show(
                        item_list, "Select an Item to add: ", "Cancel"
                    )
                    if item_index > -1:
                        self.cart.addItem(menu_manager.getAllItems()[item_index])

                case 1:
                    if len(self.cart.getAllItems()) > 0:
                        item_list = [
                            item.name + " - $" + str(item.price)
                            for item in self.cart.getAllItems()
                        ]
                        item_index = OptionSelection.show(
                            item_list, "Select an Item to add: ", "Cancel"
                        )
                        if item_index > -1:
                            self.cart.removeItem(item_index)
                    else:
                        print("There are no items to remove.")

                case 2:
                    return self.cart

                case -1:
                    break
        return None
