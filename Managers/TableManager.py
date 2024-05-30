from typing import List

from DatabaseConnection import DatabaseConnection
from MainClasses.Table import Table


class TableManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.tables: List[Table] = []

    def readItemsFromDB(self):
        table_dict = self.db.getTableData("tables")
        self.tables = [Table(table["id"], table["status"]) for table in table_dict]

    def _saveItemsToDB(self):
        table_dict = [
            {"id": table.getID(), "status": table.getStatus()} for table in self.tables
        ]
        self.db.writeTableData("tables", table_dict)

    def addTable(self, table: Table):
        self.tables.append(table)
        self._saveItemsToDB()

    def removeTable(self, id: int):
        for i in range(0, len(self.tables)):
            if self.tables[i].getId() == id:
                del self.tables[i]
        self._saveItemsToDB()

    def editTable(self, table: Table):
        for i in range(0, len(self.tables)):
            if self.tables[i].getId() == id:
                self.tables[i] = table
        self._saveItemsToDB()

    def getTables(self) -> List[Table]:
        return self.tables

    def getTable(self, id: int) -> Table:
        for i in range(0, len(self.tables)):
            if self.tables[i].getId() == id:
                return self.tables[i]
