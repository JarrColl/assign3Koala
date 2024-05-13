from ..DatabaseConnection import DatabaseConnection
from ..MainClasses.MenuItem import MenuItem


class MenuManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.items: list(MenuItem) = []

    def addItem(item: MenuItem):
        pass

    def removeItem(id: int):
        pass

    def editItem(item: MenuItem):
        pass

    def getItem(id: int) -> MenuItem:
        pass
