from ..DatabaseConnection import DatabaseConnection
from ..MainClasses.Reservation import Reservation
from typing import List


class ReservationManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db
        self.reservations: List[Reservation] = []

    def addReservation(reservation: Reservation):
        pass

    def removeReservation(id: int):
        pass

    # TODO: add the args
    def editReservation():
        pass

    # TODO: add get a single reservation function?????
    def getReservations() -> List[Reservation]:
        pass

    def getReservation() -> Reservation:
        pass
