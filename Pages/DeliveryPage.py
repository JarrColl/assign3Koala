# list deliveries
# Mark as delivered
import os
from DatabaseConnection import DatabaseConnection
from MainClasses.MenuItem import MenuItem  # Assuming MenuItem will be used as DeliveryItem
from OptionSelection import OptionSelection
from Pages.Page import Page
import time

db = DatabaseConnection()

class DeliveryPage(Page):
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display(login_manager):
        options = ["List Deliveries", "Mark a Delivery as Delivered"]
        while True:
            selection_index = OptionSelection.show(options, "Delivery Menu: ", "Return to home")
            if selection_index == 0:
                DeliveryPage.clear_screen()
                DeliveryPage.list_deliveries()
                DeliveryPage.clear_screen()
            elif selection_index == 1:
                DeliveryPage.clear_screen()
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
        header = "| {:<5} | {:<20} | {:<10} |".format("ID", "Order ID", "Status")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for delivery in deliveries:
            if delivery['isDelivered']:
                status = 'Delivered'
            else:
                status = 'Ready...'
            print("| {:<5} | {:<20} | {:<10} |".format(delivery['id'], delivery['orderID'], status ))

        print("-" * len(header))

        while True:
            return OptionSelection.show([], "Delivery Menu: ", "Return")


    @staticmethod
    def mark_delivery():
        deliveries = db.getTableData("deliveries")
        delivery_list = [
            f"Delivery ID: {delivery['id']}, Order ID: {delivery['orderID']}, Is Delivered: {delivery['isDelivered']}"
            for delivery in deliveries
        ]
        delivery_index = OptionSelection.show(delivery_list, "Select a Delivery to mark as delivered", "Return")
        if delivery_index is not None and delivery_index != -1:
            delivery_id = deliveries[delivery_index]['id']
            DeliveryPage.update_delivery_status(delivery_id)


    @staticmethod
    def update_delivery_status(delivery_id):
        deliveries = db.getTableData("deliveries")
        delivery = next((d for d in deliveries if d['id'] == delivery_id), None)
        if delivery and delivery['isDelivered'] != True:
            delivery['isDelivered'] = True
            db.writeTableData("deliveries", deliveries)
            print(f"Delivery {delivery_id} has been marked as delivered.")
        else:
            print("Invalid ID or delivery already delivered.")
