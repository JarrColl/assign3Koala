from Table import Table
from datetime import datetime


class Reservation:
    def __init__(self, id: int, table: Table, time_slot: datetime):
        self.id: int = id
        self.table: str = table

    def getId(self) -> int:
        return self.id

    def setId(self, id: int):
        self.id = id

    def getTable(self) -> Table:
        return self.table

    def setTable(self, table: Table):
        self.table = table
