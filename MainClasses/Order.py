from typing import List, Literal, Optional

from DatabaseConnection import DatabaseConnection
from MainClasses.Cart import Cart
from MainClasses.Invoice import Invoice
from MainClasses.MenuItem import MenuItem

db = DatabaseConnection()


class Order:
    def __init__(
        self,
        cart: Cart,
        table_id: int,
        id: Optional[int] = None,
        status: Literal["Cooking", "Cooked", "Paid"] = "Cooking",
    ):
        if id:
            self.id = id
        else:
            order_dict = db.getTableData("orders")
            if len(order_dict) > 0:
                next_id = max(order_dict, key=lambda x: x["id"])["id"] + 1
            else:
                next_id = 0
            self.id: int = next_id

        self.menu_items: List[MenuItem] = cart.getAllItems()
        self.invoice: Optional[Invoice] = None
        self.table: int = table_id
        self.status: Literal["Cooking", "Cooked", "Paid"] = status

    def getAllItems(self) -> List[MenuItem]:
        return self.menu_items

    def getId(self) -> int:
        return self.id

    def getInvoice(self) -> Optional[Invoice]:
        return self.invoice

    def setInvoice(self, invoice: Invoice):
        self.invoice = invoice

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status: Literal["Cooking", "Cooked", "Paid"]):
        self.status = status

    def getTable(self) -> int:
        return self.table

    def getTotalCost(self):
        total = 0
        for item in self.menu_items:
            total += item.getPrice()
        return total

    def asDict(self):
        menu_items = [item.getId() for item in self.menu_items]
        return {
            "id": self.id,
            "menu_items": menu_items,
            "invoice_id": self.invoice,
            "table_id": self.table,
            "status": self.status,
        }
