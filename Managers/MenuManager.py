from typing import List, Optional

from DatabaseConnection import DatabaseConnection
from MainClasses.MenuItem import MenuItem


class MenuManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.items: List[MenuItem] = []

    def readItemsFromDB(self):
        item_dict = self.db.getTableData("menu")
        self.items = [
            MenuItem(item["id"], item["name"], item["price"]) for item in item_dict
        ]

    def _saveItemsToDB(self):
        items_dict = [item.asDict() for item in self.items]
        self.db.writeTableData("menu", items_dict)

    def addItem(self, item: MenuItem):
        self.items.append(item)
        self._saveItemsToDB()

    def removeItem(self, id: int):
        for i in range(0, len(self.items)):
            if self.items[i].id == id:
                del self.items[i]
                break
        self._saveItemsToDB()

    def editItem(self, item: MenuItem):
        for i in range(0, len(self.items)):
            if self.items[i].id == item.id:
                self.items[i] = item
        self._saveItemsToDB()

    def getItem(self, id: int) -> Optional[MenuItem]:
        for i in range(0, len(self.items)):
            if self.items[i].id == id:
                return self.items[i]
        return None

    def getAllItems(self) -> List[MenuItem]:
        return self.items
