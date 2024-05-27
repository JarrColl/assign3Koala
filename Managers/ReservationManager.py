from DatabaseConnection import DatabaseConnection
from MainClasses.Reservation import Reservation
from typing import List


class ReservationManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.reservations: List[Reservation] = []

    def addReservation(self, reservation: Reservation):
        self.reservations.append(reservation)

    def removeReservation(self, id: int):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                del self.reservations[i]

    def editReservation(self, reservation: Reservation):
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == reservation.id:
                self.reservations[i] = reservation

    def getReservations(self) -> List[Reservation]:
        return self.reservations

    def getReservation(self, id: int) -> Reservation:
        for i in range(0, len(self.reservations)):
            if self.reservations[i].id == id:
                return self.reservations[i]
