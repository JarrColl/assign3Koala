from DatabaseConnection import DatabaseConnection
from MainClasses.Reservation import Reservation
from MainClasses.Table import Table
from typing import List


class ReservationManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.reservations: List[Reservation] = []

    def to_dict(self, reservation: Reservation):
        return {
            'id': reservation.getId(),
            'tableId': reservation.getTable().getId()
        }

    def addReservation(self, reservation: Reservation):
        self.reservations.append(reservation)
        reservations = []
        for rev in self.reservations:
            rev = self.to_dict(rev)
            reservations.append(rev)
        self.db.writeTableData("reservation", reservations)


    def removeReservation(self, id: int):
        for r in self.reservations:
            if r.getId() == id:
                self.reservations.remove(r)
        reservations = []
        count = 1
        for rev in self.reservations:
            rev.setId(count)
            count += 1
            rev = self.to_dict(rev)
            reservations.append(rev)
        self.db.writeTableData("reservation", reservations)
        return True

    def editReservation(self, reservation: Reservation):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == reservation.id:
                self.reservations[i] = reservation
        self.db.writeTableData("reservation", self.reservations)

    def getReservations(self) -> List[Reservation]:
        reservations = self.db.getTableData("reservation")
        table_dict = self.db.getTableData("tables")
        for reservation in reservations:
            for table in table_dict:
                    if table['id'] == reservation['tableId']:
                        new_table = Table(table['id'], table['status'])
                        self.reservations.append(Reservation(reservation['id'], new_table))
        return self.reservations

    def getReservation(self, id: int) -> Reservation:
        self.reservations = self.db.getTableData("reservation")
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                return self.reservations[i]
