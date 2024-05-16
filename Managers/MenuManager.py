from ..DatabaseConnection import DatabaseConnection
from ..MainClasses.MenuItem import MenuItem
from typing import List


class MenuManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.items: List[MenuItem] = []

    def addItem(self, item: MenuItem):
        self.items.append(item)

    def removeItem(self, id: int):
        pass

    def editItem(self, item: MenuItem):
        pass

    def getItem(self, id: int) -> MenuItem:
        pass
