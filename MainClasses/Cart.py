from typing import List

from MainClasses.MenuItem import MenuItem


class Cart:
    def __init__(self):
        self.menuItems: List[MenuItem] = []

    def addItem(self, menuItem: MenuItem):
        self.menuItems.append(menuItem)

    def removeItem(self, index: int):
        del self.menuItems[index]

    def getAllItems(self) -> List[MenuItem]:
        return self.menuItems

    def getItem(self, index) -> MenuItem:
        return self.menuItems[index]

    def getTotalCost(self) -> float:
        total = 0
        for item in self.menuItems:
            total += item.getPrice()
        return total
