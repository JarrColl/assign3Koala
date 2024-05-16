from ..DatabaseConnection import DatabaseConnection
from ..MainClasses.Table import Table
from typing import List


class TableManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.tables: List[Table] = []

    def addTable(table: Table):
        pass

    def removeTable(id: int):
        pass

    def editTable():
        pass

    def getTables() -> List[Table]:
        pass

    def getTable() -> Table:
        pass
