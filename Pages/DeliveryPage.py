# list deliveries
# Mark as delivered
from DatabaseConnection import DatabaseConnection
from MainClasses.MenuItem import (
    MenuItem,
)  # Assuming MenuItem will be used as DeliveryItem
from OptionSelection import OptionSelection
from Pages.Page import Page

db = DatabaseConnection()


class DeliveryPage(Page):
    @staticmethod
    def display(login_manager):
        options = ["List Deliveries", "Mark a Delivery as Delivered", "Return"]
        while True:
            selection_index = OptionSelection.show(options, "Delivery Menu: ", "Return")
            if selection_index == 0:
                DeliveryPage.list_deliveries()
            elif selection_index == 1:
                DeliveryPage.mark_delivery()
            else:
                break

    @staticmethod
    def list_deliveries():
        deliveries = db.getTableData("deliveries")
        DeliveryPage.print_deliveries(deliveries)

    @staticmethod
    def print_deliveries(deliveries):
        print("----------Deliveries----------")
        header = "| {:<5} | {:<20} | {:<10} |".format("ID", "Description", "Status")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for delivery in deliveries:
            print(
                "| {:<5} | {:<20} | {:<10} |".format(
                    delivery["id"], delivery["description"], delivery["status"]
                )
            )

        print("-" * len(header))

    @staticmethod
    def mark_delivery():
        deliveries = db.getTableData("deliveries")
        delivery_list = [
            f"Delivery ID: {delivery['id']}, Description: {delivery['description']}, Status: {delivery['status']}"
            for delivery in deliveries
        ]
        delivery_index = OptionSelection.show(
            delivery_list, "Select a Delivery to mark as delivered", "Return to home."
        )
        if delivery_index is not None and delivery_index != -1:
            delivery_id = deliveries[delivery_index]["id"]
            DeliveryPage.update_delivery_status(delivery_id)

    @staticmethod
    def update_delivery_status(delivery_id):
        deliveries = db.getTableData("deliveries")
        delivery = next((d for d in deliveries if d["id"] == delivery_id), None)
        if delivery and delivery["status"] != "delivered":
            db.updateDeliveryStatus(delivery_id, "delivered")
            print(f"Delivery {delivery_id} has been marked as delivered.")
        else:
            print("Invalid ID or delivery already delivered.")
