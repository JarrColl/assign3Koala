from typing import List

from MenuItem import MenuItem

class Cart:
    def __init__(self):
        self.menuItems: List[MenuItem] = []

    def addItem(self, menuItem:MenuItem):
        self.menuItems.append(menuItem)

    def removeItem(self, menuItem:MenuItem):
        for item in self.menuItems:
            if(item == menuItem):
                self.menuItems.remove(item)

    def getAllItems(self):
        return self.menuItems

    def getItem(self, index):
        return self.menuItems[index]

    def totalCost(self):
        total = 0
        for item in self.menuItems:
            total += item.getPrice()
        return total


