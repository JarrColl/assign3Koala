from typing import List

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
        cart: Cart,
        status: str,
        table: Table,
        delivery: Delivery = None,
    ):
        # This sucks, and wouldn't be a problem with a sql db but we didn't bother using one because 
        # what is the point we are only here to show OOP design being implemented, not our sql database abilities
        order_dict = db.getTableData("orders")
        # TODO: FINISH THIS
        self.id: int = 
        

        self.menu_items: List[MenuItem] = cart.getAllItems()
        self.invoice: Invoice = None
        self.delivery: Delivery = delivery
        self.table: Table = table
        self.status: str = status # Cooking, Cooked, Paid

    def getAllItems(self) -> List[MenuItem]:
        return self.menu_items

    def getId(self) -> int:
        return self.id

    def getInvoice(self) -> Invoice:
        return self.invoice

    def setInvoice(self, invoice: Invoice):
        self.invoice = invoice

    def getDelivery(self) -> Delivery:
        return self.delivery

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status: str):
        self.status = status

    def getTable(self) -> Table:
        return self.table

    def getTotalCost(self):
        total = 0
        for item in self.menu_items:
            total += item.getPrice()
        return total

