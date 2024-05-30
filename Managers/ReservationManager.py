from typing import List

from DatabaseConnection import DatabaseConnection
from MainClasses.Reservation import Reservation
from MainClasses.Table import Table
from Managers.TableManager import TableManager

class ReservationManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.reservations: List[Reservation] = []
        self.table_manager = TableManager(self.db)

    def readItemsFromDB(self):
        reservation_dict = self.db.getTableData("reservations")
        self.table_manager.readItemsFromDB()
        for reservation in reservation_dict:
            table = self.table_manager.getTable(reservation["id"])
            self.reservations.append(
                Reservation(reservation["id"], table, reservation.get("time_slot", None))
            )

    def _saveItemsToDB(self):
        reservation_dict = [reservation.asDict() for reservation in self.reservations]
        self.db.writeTableData("reservations", reservation_dict)

    def addReservation(self, reservation: Reservation):
        self.reservations.append(reservation)
        self._saveItemsToDb()

    # def editReservation(self, reservation_id: int, table_id: int):
    #     reservations = []
    #     for res in self.reservations:
    #         if res.getId() == reservation_id:
    #             res.setTable(Table(table_id, "occupied"))
    #         res = self.to_dict(res)
    #         reservations.append(res)
    #     self.db.writeTableData("reservation", reservations)
    #     return True

    def removeReservation(self, id: int):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                del self.reservations[i]
        self._saveItemsToDB()

    def editReservation(self, reservation: Reservation):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == reservation.id:
                self.reservations[i] = reservation
        self._saveItemsToDB()

    def getReservations(self):
        return self.reservations

    def getReservation(self, id: int) -> Reservation:
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                return self.reservations[i]
