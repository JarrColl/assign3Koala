# List the orders that have status prepraring
# Edit the status of order and save to database
import os
from DatabaseConnection import DatabaseConnection
from OptionSelection import OptionSelection
from Pages.Page import Page
from MainClasses.Order import Order
from MainClasses.MenuItem import MenuItem
from MainClasses.Cart import Cart
from typing import List
import time


db = DatabaseConnection()


class KitchenPage(Page):

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def display(login_manager):
        order_dict = db.getTableData("orders")
        menu_dict = db.getTableData("menu")
        paid_orders = [
            order
            for order in order_dict
            if (order["status"] == "Paid" or order["status"] == "Cooking")
        ]
        order_list: List[Order] = []

        for order in paid_orders:
            menu_item_ids = order["menu_items"]
            filtered_menu_items = [
                item for item in menu_dict if item["id"] in menu_item_ids
            ]
            menu_items = [
                MenuItem(item["id"], item["name"], item["price"])
                for item in filtered_menu_items
            ]
            cart = Cart()
            for item in menu_items:
                cart.addItem(item)
            order_list.append(
                Order(order["id"], cart, order["status"], order["table_id"])
            )

        KitchenPage.printOrder(order_list)

    def printOrder(order_list):
        while True:
            founded = False
            if (len(order_list)) == 0:
                print("No order available")
                user_input = input("Enter 'q' to exit: ")
                if user_input == "q":
                    return "q"
                else:
                    KitchenPage.clear_screen()
                    print("!!!!Invalid input, please enter 'q' to exit!!!!")
            else:
                for order in order_list:
                    print("-------Order ID: " + str(order.getId()) + "-------")
                    print("Status: " + order.getStatus())
                    KitchenPage.printItems(order.getAllItems())
                user_input = input("Enter 'q' to exit, 'u' to update order status: ")
                if user_input == "q":
                    return "q"
                elif user_input == "u":
                    order_id_to_update = input("Enter the order ID to update status: ")
                    for order in order_list:
                        if str(order.getId()) == order_id_to_update:
                            new_status = input("Enter the new status: ")
                            order.setStatus(new_status)
                            KitchenPage.update_order_status(
                                order_id_to_update, new_status
                            )
                            print(f"Order status updated to {new_status}")
                            if new_status == "Cooked":
                                order_list.remove(order)
                            time.sleep(1)
                            KitchenPage.clear_screen()
                            founded = True
                            break
                    if not founded:
                        KitchenPage.clear_screen()
                        print(
                            "!!!!Invalid order ID, please enter 'u' to update order status again!!!!"
                        )
                else:
                    KitchenPage.clear_screen()
                    print(
                        "!!!!Invalid input, please enter 'q' to exit or 'u' to update order status.!!!!"
                    )

    def printItems(menu_items):

        for item in menu_items:
            id_str = str(item.getId())
            name_str = item.getName()
            price_str = str(item.getPrice())
            print(f"Item ID: {id_str} - Name: {name_str} - Price: {price_str}")

    def update_order_status(order_id: str, new_status: str):
        order_dict = db.getTableData("orders")

        # Find the order with the specified ID and update its status
        for order in order_dict:
            if str(order["id"]) == order_id:
                order["status"] = new_status
                break

        db.writeTableData("orders", order_dict)
