from DatabaseConnection import DatabaseConnection
from MainClasses.Reservation import Reservation
from MainClasses.Table import Table
from typing import List


class ReservationManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.reservations: List[Reservation] = []

    def _saveItemsToDB(self):
        reservation_dict = [
            reservation.asDict() for reservation in self.reservations
        ]
        self.db.writeTableData("tables", reservation_dict)


    def addReservation(self, reservation: Reservation):
        self.reservations.append(reservation)
        self._saveItemsToDb()

    def editReservation(self, reservation_id: int, table_id: int):
        reservations = []
        for res in self.reservations:
            if res.getId() == reservation_id:
                res.setTable(Table(table_id, "occupied"))
            res = self.to_dict(res)
            reservations.append(res)
        self.db.writeTableData("reservation", reservations)
        return True

    def removeReservation(self, id: int):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                del self.reservations[i]
        self.db.writeTableData("reservations", self.reservations)

    # def editReservation(self, reservation: Reservation):
    #     for i in range(0, len(self.reservations)):
    #         if self.reservations[i].id == reservation.id:
    #             self.reservations[i] = reservation
    #     self.db.writeTableData("reservations", self.reservations)

    def getReservations(self) -> List[Reservation]:
        reservations = self.db.getTableData("reservations")
        table_dict = self.db.getTableData("tables")
        for reservation in reservations:
            for table in table_dict:
                    if table['id'] == reservation['tableId']:
                        new_table = Table(table['id'], table['status'])
                        self.reservations.append(Reservation(reservation['id'], new_table))
        return self.reservations

    def getReservation(self, id: int) -> Reservation:
        self.reservations = self.db.getTableData("reservations")
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                return self.reservations[i]
