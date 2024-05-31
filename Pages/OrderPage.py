# List all orders
# Select an existing order or create a new one.
#
# If selecting an order: Can select to move to the payment phase.
#   Change paid status to paid.
# If creating an order: Go to cart page to add items.
# Take the returned item list and save it to the database, ask if a delivery should be created and then add it to the delivery database if true.
# List available tables to select from
# Remember to mark the table associated with the order as occupied
# when adding a delivery, randomly select a delivery driver

import os
from typing import List

from DatabaseConnection import DatabaseConnection
from MainClasses.Cart import Cart
from MainClasses.Delivery import Delivery
from MainClasses.MenuItem import MenuItem
from MainClasses.Order import Order
from Managers.LoginManager import LoginManager
from Managers.MenuManager import MenuManager
from Managers.TableManager import TableManager
from OptionSelection import OptionSelection
from Pages.CartPage import CartPage
from Pages.Page import Page
from Pages.PaymentPage import PaymentPage

# from Pages.PaymentPage import PaymentPage

db = DatabaseConnection()
table_manager = TableManager(db)
menu_manager = MenuManager(db)
menu_manager.readItemsFromDB()

ORDER_MENU = ["Create an Order", "View an Order"]
VIEW_ORDER_OPTIONS = ["Pay for Order"]


class OrderPage(Page):
    @staticmethod
    def display(login_manager: LoginManager) -> bool:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            selection_index = OptionSelection.show(ORDER_MENU, "Order Menu: ", "Return")
            os.system("cls" if os.name == "nt" else "clear")

            match selection_index:
                case 0:  # Create an Order
                    OrderPage.createOrder()
                case 1:
                    OrderPage.viewOrder(login_manager)
                case -1:
                    break
        return True

    @staticmethod
    def printCart(items: List[MenuItem]):
        if len(items) > 0:
            print("-----------------------------")
            print("Order Items")
            for item in items:
                print(f"{item.getName()} - {item.getPrice()}")
            print("-----------------------------")

    @staticmethod
    def createOrder():
        order_dict = db.getTableData("orders")
        table_manager.readItemsFromDB()
        tables = table_manager.getTables()
        table_id = OptionSelection.show(
            [str(table.getId()) + " - " + table.getStatus() for table in tables],
            "What table is the order for?",
            "Cancel",
        )
        if table_id == -1:
            return

        cart = CartPage().display()
        if not cart:
            return

        new_order = Order(cart, table_id)
        order_dict.append(new_order.asDict())

        while True:
            do_delivery = input(
                "Do you want to create a delivery for this order?(y/n): "
            )
            if do_delivery == "y":
                address = input("Enter the address for the order: ")
                delivery = Delivery(new_order, address)
                deliveries = db.getTableData("deliveries")
                deliveries.append(delivery.asDict())
                db.writeTableData("deliveries", deliveries)

                break
            elif do_delivery == "n":
                break

        table = table_manager.getTable(table_id)
        if table:
            table.setStatus("occupied")
            table_manager.editTable(table)
        db.writeTableData("orders", order_dict)

    @staticmethod
    def viewOrder(login_manager: LoginManager):
        table_manager.readItemsFromDB()
        order_dict = db.getTableData("orders")
        order_list = [
            "Order ID: "
            + str(order["id"])
            + ", Table ID: "
            + str(order["table_id"])
            + ", Status: "
            + order["status"]
            for order in order_dict
        ]

        order_index = OptionSelection.show(order_list, "Select an Order", "Return.")
        if order_index == -1:
            return
        order = order_dict[order_index]

        os.system("cls" if os.name == "nt" else "clear")
        items = []
        for item_id in order["menu_items"]:
            item = menu_manager.getItem(item_id)
            if item:
                items.append(item)
        OrderPage.printCart(items)

        if order["status"] != "Paid":
            view_options = VIEW_ORDER_OPTIONS
        else:
            view_options = []
        view_order_option = OptionSelection.show(
            view_options, f"Order: { order["id"] }", "Return"
        )
        if view_order_option == 0:  # Pay for order
            os.system("cls" if os.name == "nt" else "clear")
            if PaymentPage.display(login_manager):
                print("payment successfull")
                order["status"] = "Paid"
                order_dict[order_index] = order

                table = table_manager.getTable(order["table_id"])
                if table:
                    table.setStatus("free")
                    table_manager.editTable(table)


                db.writeTableData("orders", order_dict)
                input("Press enter to continue...")
            else:
                return
        else:
            return
