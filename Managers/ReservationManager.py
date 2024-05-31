from typing import List, Optional

from DatabaseConnection import DatabaseConnection
from MainClasses.Reservation import Reservation
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
            table = self.table_manager.getTable(reservation["table_id"])

            if table:
                self.reservations.append(
                    Reservation(reservation["id"], table, reservation["time_slot"])
                )
            else:
                print("Found reservation with an invalid table.")

    def _saveItemsToDB(self):
        reservation_dict = [reservation.asDict() for reservation in self.reservations]
        self.db.writeTableData("reservations", reservation_dict)

    def addReservation(self, reservation: Reservation):
        self.reservations.append(reservation)
        self._saveItemsToDB()

    def removeReservation(self, id: int):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                del self.reservations[i]
                break
        self._saveItemsToDB()
        return True

    def editReservation(self, reservation: Reservation):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == reservation.id:
                self.reservations[i] = reservation
        self._saveItemsToDB()
        return True

    def getAllReservations(self):
        self.readItemsFromDB()
        return self.reservations

    def getReservation(self, id: int) -> Optional[Reservation]:
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                return self.reservations[i]
        return None
