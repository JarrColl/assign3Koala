# List reservations
# Add Reservation
# Delete Reservation
# Edit Reservation
import os
from DatabaseConnection import DatabaseConnection
from Pages.Page import Page
from MainClasses.Reservation import Reservation
from MainClasses.Table import Table
from typing import List


db = DatabaseConnection()


class ReservationPage(Page):

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(login_manager):
        reservation_dict = db.getTableData("reservation")
        table_dict = db.getTableData("tables")
        reservation_list: List[Reservation] = []


        for reservation in reservation_dict:
            for table in table_dict:
                if table['id'] == reservation['tableId']:
                    new_table = Table(table['id'], table['status'])

            reservation_list.append(Reservation(reservation['id'], new_table))

        ReservationPage.printReservation(reservation_list)

    def printReservation(reservation_list):
        for reservation in reservation_list:
            print('Reservation ID: ' + str(reservation.getId()))
            print('Table ID: ' + str(reservation.getTable().getId()) + " Status: " + reservation.getTable().getStatus())

        while True:
            user_input = input("Enter q to exit: ")
            if user_input == "q":
                return "q"




