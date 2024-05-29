from datetime import datetime

from MainClasses.Table import Table


class Reservation:
    def __init__(self, id: int, table: Table):
        self.id: int = id
        self.table: Table = table
        # self.time_slot = time_slot

    def getId(self) -> int:
        return self.id

    def setId(self, id: int):
        self.id = id

    def getTable(self) -> Table:
        return self.table

    def setTable(self, table: Table):
        self.table = table
