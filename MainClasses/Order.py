from typing import List

from MainClasses.Cart import Cart
from MainClasses.Invoice import Invoice
from MainClasses.Delivery import Delivery
from MainClasses.Table import Table
from MenuItem import MenuItem


class Order:
    def __init__(
        self,
        id: int,
        cart: Cart,
        status: str,
        table: Table,
        delivery: Delivery = None,
    ):
        self.id: int = id
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

