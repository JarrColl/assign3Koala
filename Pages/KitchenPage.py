# List the orders that have status prepraring
# Edit the status of order and save to database
import os
from typing import List

from DatabaseConnection import DatabaseConnection
from MainClasses.Cart import Cart
from MainClasses.Order import Order
from Managers.MenuManager import MenuManager
from Pages.Page import Page

db = DatabaseConnection()
menu_manager = MenuManager(db)


class KitchenPage(Page):

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display(login_manager) -> bool:
        order_dict = db.getTableData("orders")
        menu_manager.readItemsFromDB()
        paid_orders = [order for order in order_dict if (order["status"] == "Cooking")]
        order_list: List[Order] = []

        for order in paid_orders:
            menu_item_ids = order["menu_items"]
            menu_items = list(
                filter(
                    lambda item: item.getId() in menu_item_ids,
                    menu_manager.getAllItems(),
                )
            )
            # print(menu_items)
            cart = Cart()
            for item in menu_items:
                cart.addItem(item)
            order_list.append(
                Order(cart, order["table_id"], order["id"], order["status"])
            )

        KitchenPage.printOrders(order_list)

    @staticmethod
    def printOrders(order_list):
        while True:
            found = False
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
                print("__________________________________________________")
                user_input = input(
                    "Enter 'q' to exit, 'u' to mark an order as 'Cooked': "
                )
                if user_input == "q":
                    return "q"
                elif user_input == "u":
                    order_id_to_update = input("Enter the order ID to update status: ")
                    for order in order_list:
                        if str(order.getId()) == order_id_to_update:
                            order.setStatus("Cooked")
                            KitchenPage.update_order_status(order)
                            print("Order status updated to Cooked")
                            order_list.remove(order)
                            KitchenPage.clear_screen()
                            found = True
                            break
                    if not found:
                        KitchenPage.clear_screen()
                        print(
                            "Invalid order ID, please enter 'u' to update order status again."
                        )
                else:
                    KitchenPage.clear_screen()
                    print(
                        "Invalid input, please enter 'q' to exit or 'u' to update order status."
                    )

    @staticmethod
    def printItems(menu_items):
        for item in menu_items:
            id_str = str(item.getId())
            name_str = item.getName()
            price_str = str(item.getPrice())
            print(f"Item ID: {id_str} - Name: {name_str} - Price: {price_str}")

    @staticmethod
    def update_order_status(new_order: Order):
        order_dict = db.getTableData("orders")

        # Find the order with the specified ID and update its status
        for i in range(0, len(order_dict)):
            if order_dict[i]["id"] == new_order.getId():
                order_dict[i]["status"] = "Cooked"
                break

        db.writeTableData("orders", order_dict)
