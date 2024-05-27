from DatabaseConnection import DatabaseConnection
from MainClasses.Table import Table
from typing import List


class TableManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.tables: List[Table] = []

    def addTable(self, table: Table):
        self.tables.append(table)

    def removeTable(self, id: int):
        for i in range(0, len(self.tables)):
            if self.tables[i].id == id:
                del self.tables[i]

    def editTable(self, table: Table):
        for i in range(0, len(self.tables)):
            if self.tables[i].id == id:
                self.tables[i] = table

    def getTables(self) -> List[Table]:
        return self.tables

    def getTable(self, id: int) -> Table:
        for i in range(0, len(self.tables)):
            if self.tables[i].id == id:
                return self.tables[id]
