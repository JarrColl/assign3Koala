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
from Pages.PaymentPage import PaymentPage

db = DatabaseConnection()
table_manager = TableManager(db)

ORDER_MENU = ["Create an Order", "Open an Order"]
VIEW_ORDER_OPTIONS = ["Pay for Order"]


class OrderPage(Page):
    def display(self, login_manager):
        while True:
            selection_index = OptionSelection.show(ORDER_MENU, "Order Menu: ", "Return")

            match selection_index:
                case 0:  # Create an Order
                    OrderPage.createOrder()
                case 1:
                    OrderPage.viewOrder()
                case -1:
                    break

    @staticmethod
    def createOrder():
        order_dict = db.getTableData("orders")
        table_manager.readItemsFromDB()
        tables = table_manager.getTables()
        table_id = OptionSelection.show(
            [table["id"] for table in tables], "What table is the order for?", "Cancel"
        )
        if table_id == -1:
            return

        cart = CartPage.display()
        new_order = Order(cart, table_id)
        order_dict.append(new_order.asDict())
        db.writeTableData("orders", order_dict)

    @staticmethod
    def viewOrder():
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
        order: Order = order_dict[order_index]

        view_order_option = OptionSelection(VIEW_ORDER_OPTIONS, f"Order: { order.getId() }", "Cancel")
        if view_order_option == 0: # Pay for order
            pass
            #TODO: uncomment when ryan finishes the payment page
            # if PaymentPage.display():
                # order.setStatus("Paid")
        else: 
            return
