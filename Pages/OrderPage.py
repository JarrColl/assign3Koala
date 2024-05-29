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

from DatabaseConnection import DatabaseConnection
from MainClasses.Order import Order
from Managers.TableManager import TableManager
from OptionSelection import OptionSelection
from Pages.CartPage import CartPage
from Pages.Page import Page

db = DatabaseConnection()
table_manager = TableManager(db)

ORDER_MENU = ["Create an Order", "Open an Order"]


class OrderPage(Page):
    def display(login_manager):
        while True:
            selection_index = OptionSelection.show(ORDER_MENU, "Order Menu: ", "Return")

            match selection_index:
                case 0:  # Create an Order
                    table_manager.readItemsFromDB()
                    tables = table_manager.getTables()
                    # TODO: check if return in -1 to cancel
                    OptionSelection.show(
                        [table["id"] for table in tables],
                        "What table is the order for?",
                        "Cancel",
                    )
                    cart = CartPage.display()
                    new_order = Order(cart)

                case 1:
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

                    order_index = OptionSelection.show(
                        order_list, "Select an Order", "Return to home."
                    )
                case -1:
                    break
