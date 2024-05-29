from typing import List, Literal

from DatabaseConnection import DatabaseConnection
from MainClasses.Cart import Cart
from MainClasses.Invoice import Invoice
from MainClasses.MenuItem import MenuItem
from MainClasses.Table import Table

db = DatabaseConnection()


class Order:
    def __init__(
        self,
        cart: Cart,
        tableId: int,
        id: int = None,
        status: Literal["Cooking", "Cooked", "Paid"] = "Cooking",
    ):
        if id:
            self.id = id
        else:
            order_dict = db.getTableData("orders")
            next_id = max(order_dict, key=lambda x: x["id"])["id"] + 1
            self.id: int = next_id

        self.menu_items: List[MenuItem] = cart.getAllItems()
        self.invoice: Invoice = None
        self.table: int = tableId
        self.status: Literal["Cooking", "Cooked", "Paid"] = status

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
