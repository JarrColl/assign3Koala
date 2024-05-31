# list deliveries
# Mark as delivered
import os

from DatabaseConnection import DatabaseConnection
from Managers.LoginManager import LoginManager
from OptionSelection import OptionSelection
from Pages.Page import Page

db = DatabaseConnection()


class DeliveryPage(Page):
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display(login_manager: LoginManager) -> bool:
        options = ["List Deliveries", "Mark a Delivery as Delivered"]
        while True:
            DeliveryPage.clear_screen()
            selection_index = OptionSelection.show(
                options, "Delivery Menu: ", "Return to home"
            )
            DeliveryPage.clear_screen()
            if selection_index == 0:
                DeliveryPage.list_deliveries()
            elif selection_index == 1:
                DeliveryPage.mark_delivery()
            else:
                break
        return True

    @staticmethod
    def list_deliveries():
        deliveries = db.getTableData("deliveries")
        DeliveryPage.print_deliveries(deliveries)

    @staticmethod
    def print_deliveries(deliveries):
        print("----------Deliveries----------")
        header = "| {:<5} | {:<20} | {:<10} |".format("ID", "Order ID", "Status")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for delivery in deliveries:
            if delivery["is_delivered"]:
                status = "Delivered"
            else:
                status = "Ready..."
            print(
                "| {:<5} | {:<20} | {:<10} |".format(
                    delivery["id"], delivery["order_id"], status
                )
            )

        print("-" * len(header))

        while True:
            return OptionSelection.show([], "Delivery Menu: ", "Return")

    @staticmethod
    def mark_delivery():
        while True:
            DeliveryPage.clear_screen()
            deliveries = db.getTableData("deliveries")

            delivery_list = [
                f"Delivery ID: {delivery['id']}, Order ID: {delivery['order_id']}, Is Delivered: {delivery['is_delivered']}"
                for delivery in deliveries
            ]
            delivery_index = OptionSelection.show(
                delivery_list, "Select a Delivery to mark as delivered", "Return"
            )

            if delivery_index == -1:
                break

            delivery_id = deliveries[delivery_index]["id"]
            DeliveryPage.update_delivery_status(delivery_id)
            input("Press enter to continue.")

    @staticmethod
    def update_delivery_status(delivery_id):
        deliveries = db.getTableData("deliveries")
        delivery = next((d for d in deliveries if d["id"] == delivery_id), None)
        if delivery and not delivery["is_delivered"]:
            delivery["is_delivered"] = True
            db.writeTableData("deliveries", deliveries)
            print(f"Delivery {delivery_id} has been marked as delivered.")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Invalid ID or delivery already delivered.")
