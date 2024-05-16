from typing import List

from MenuItem import MenuItem


class Order:
    def __init__(self, id, cart, invoice, status, delivery=None, table=None):
        self.menuItems: List[MenuItem] = []
        for item in cart.getAllItems():
            self.menuItems.append(item)
        self.id = id
        self.invoice = invoice
        self.delivery = delivery
        self.table = table
        self.status = status

    def getAllItems(self):
        return self.menuItems

    def getId(self):
        return self.id

    def getInvoice(self):
        return self.invoice

    def getDelivery(self):
        return self.delivery

    def getStatus(self):
        return self.status

    def getTable(self):
        return self.table

    def setStatus(self, status):
        self.status = status

    def totalCost(self):
        total = 0
        for item in self.menuItems:
            total += item.getPrice()
        return total



