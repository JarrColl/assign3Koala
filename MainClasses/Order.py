from typing import List

from ..MainClasses.Cart import Cart
from ..MainClasses.Invoice import Invoice
from ..MainClasses.Delivery import Delivery
from ..MainClasses.Table import Table
from MenuItem import MenuItem


class Order:
    def __init__(
        self,
        id: int,
        cart: Cart,
        invoice: Invoice,
        status: str,
        delivery: Delivery = None,
        table: Table = None,
    ):
        self.menu_items: List[MenuItem] = cart.getAllItems()
        self.id: int = id
        self.invoice: Invoice = invoice
        self.delivery: Delivery = delivery
        self.table: Table = table
        self.status: str = status

    def getAllItems(self) -> List[MenuItem]:
        return self.menu_items

    def getId(self) -> int:
        return self.id

    def getInvoice(self) -> Invoice:
        return self.invoice

    def getDelivery(self) -> Delivery:
        return self.delivery

    def getStatus(self) -> str:
        return self.status

    def getTable(self) -> Table:
        return self.table

    def setStatus(self, status: str):
        self.status = status

    def getTotalCost(self):
        total = 0
        for item in self.menu_items:
            total += item.getPrice()
        return total
