from datetime import datetime
from MainClasses.Table import Table


class Reservation:
    def __init__(self, id: int, table: Table, time_slot):
        self.id: int = id
        self.table: Table = table
        self.time_slot = time_slot

    def getId(self) -> int:
        return self.id

    def setId(self, id: int):
        self.id = id

    def getTable(self) -> Table:
        return self.table

    def setTable(self, table: Table):
        self.table = table

    def getTimeSlot(self):
        return self.time_slot

    def setTimeSlot(self, time_slot: str):
        self.time_slot = time_slot

    def asDict(self):
        return {
            'id': self.id,
            'tableId': self.table.getId(),
            'time_slot': self.time_slot,
        }
