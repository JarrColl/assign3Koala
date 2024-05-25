from DatabaseConnection import DatabaseConnection
from MainClasses.MenuItem import MenuItem
from typing import List


class MenuManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.items: List[MenuItem] = []

    def addItem(self, item: MenuItem):
        self.items.append(item)

    def removeItem(self, id: int):
        for i in range(0, len(self.items)):
            if self.items[i].id == id:
                self.items.remove(i)
                break

    def editItem(self, item: MenuItem):
        for i in range(0, len(self.items)):
            if self.items[i].id == item.id:
                self.items[i] = item

    def getItem(self, id: int) -> MenuItem:
        for i in range(0, len(self.items)):
            if self.items[i].id == id:
                return self.items[i]
