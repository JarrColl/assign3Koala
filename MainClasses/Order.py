from typing import List, Literal

from DatabaseConnection import DatabaseConnection
from MainClasses.Cart import Cart
from MainClasses.Delivery import Delivery
from MainClasses.Invoice import Invoice
from MainClasses.MenuItem import MenuItem
from MainClasses.Table import Table

db = DatabaseConnection()


class Order:
    def __init__(
        self,
        id: int,
        cart: Cart,
        status: str,
        tableId: int,
        delivery: Delivery = None,
    ):
        # This sucks, and wouldn't be a problem with a sql db but we didn't bother using one because
        # what is the point we are only here to show OOP design being implemented, not our sql database abilities
        order_dict = db.getTableData("orders")
        next_id = max(order_dict, key=lambda x: x["id"])["id"] + 1
        if id < next_id:
            self.id = id
        else:
            self.id: int = next_id

        self.menu_items: List[MenuItem] = cart.getAllItems()
        self.invoice: Invoice = None
        self.delivery: Delivery = delivery
        self.table: int = tableId
        self.status = status
        #self.status = "Cooking"  # Cooking, Cooked, Paid

    def getAllItems(self) -> List[MenuItem]:
        return self.menu_items

    def getId(self) -> int:
        return self.id

    def getInvoice(self) -> Invoice:
        return self.invoice

    def setInvoice(self, invoice: Invoice):
        self.invoice = invoice

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status: Literal["Cooking", "Cooked", "Paid"]):
        self.status = status

    def getTable(self) -> Table:
        return self.table

    def getTotalCost(self):
        total = 0
        for item in self.menu_items:
            total += item.getPrice()
        return total
