# List reservations
# Add Reservation
# Delete Reservation
# Edit Reservation
import os
from DatabaseConnection import DatabaseConnection
from Pages.Page import Page
from MainClasses.Reservation import Reservation
from MainClasses.Table import Table
from Managers.ReservationManager import ReservationManager
from typing import List

db = DatabaseConnection()
reservation_manager = ReservationManager(db)
reservation_dict = reservation_manager.getReservations()


class ReservationPage(Page):

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def display(login_manager):
        while True:
            ReservationPage.clear_screen()
            # table_dict = db.getTableData("tables")
            reservation_list: List[Reservation] = []
            reservation_list = reservation_dict
            """
            for reservation in reservation_dict:
                for table in table_dict:
                    if table['id'] == reservation['tableId']:
                        new_table = Table(table['id'], table['status'])
                        reservation_list.append(Reservation(reservation['id'], new_table))
"""
            ReservationPage.printReservation(reservation_list)
            print("\nOptions: (a)dd, (e)dit, (r)emove, (q)uit")
            user_input = input("Enter your choice: ").strip().lower()

            if user_input == "q":
                break
            elif user_input == "a":
                ReservationPage.clear_screen()
                ReservationPage.addReservation()
                ReservationPage.clear_screen()
            elif user_input == "e":
                break
                # ReservationPage.editReservation()
            elif user_input == "r":
                break
                # ReservationPage.removeReservation()

    def printReservation(reservation_list: List[Reservation]):
        for reservation in reservation_list:
            print(
                "----------Reservation ID: " + str(reservation.getId()) + "----------"
            )
            print(
                "Table ID: "
                + str(reservation.getTable().getId())
                + " Status: "
                + reservation.getTable().getStatus()
            )

    def addReservation():
        table_dict = db.getTableData("tables")
        available_tables = [table for table in table_dict if table["status"] == "free"]
        if not available_tables:
            print("No available tables.")
            input("Press Enter to continue...")
            return

        print("Available Tables:")
        for table in available_tables:
            print(f"Table ID: {table['id']} Status: {table['status']}")

        table_id = int(input("Enter the Table ID to reserve: ").strip())
        if table_id not in [table["id"] for table in available_tables]:
            print("Invalid Table ID.")
            input("Press Enter to continue...")
            ReservationPage.clear_screen()
            return

        reserved_table = Table(table_id, "occupied")
        for table in table_dict:
            if table["id"] == table_id:
                table["status"] = "occupied"
        db.writeTableData("tables", table_dict)
        new_reservation_id = len(reservation_dict) + 1
        if new_reservation_id:
            rev = Reservation(new_reservation_id, reserved_table)
            reservation_manager.addReservation(rev)
            print(f"Reservation created with ID: {new_reservation_id}")
        else:
            print("Failed to create reservation.")
            ReservationPage.clear_screen()
        input("Press Enter to continue...")
        return

    """
    def editReservation():
        reservation_dict = reservation_manager.getReservations()
        if not reservation_dict:
            print("No reservations found.")
            input("Press Enter to continue...")
            return

        ReservationPage.printReservation(reservation_dict)
        reservation_id = int(input("Enter the Reservation ID to edit: ").strip())
        reservation = next((res for res in reservation_dict if res['id'] == reservation_id), None)
        if not reservation:
            print("Invalid Reservation ID.")
            input("Press Enter to continue...")
            return

        table_dict = db.getTableData("tables")
        available_tables = [table for table in table_dict if table['status'] == 'available' and table['id'] != reservation['tableId']]
        if not available_tables:
            print("No available tables.")
            input("Press Enter to continue...")
            return

        print("Available Tables:")
        for table in available_tables:
            print(f"Table ID: {table['id']} Status: {table['status']}")

        new_table_id = int(input("Enter the new Table ID: ").strip())
        if new_table_id not in [table['id'] for table in available_tables]:
            print("Invalid Table ID.")
            input("Press Enter to continue...")
            return

        if reservation_manager.updateReservation(reservation_id, new_table_id):
            print(f"Reservation {reservation_id} updated successfully.")
        else:
            print("Failed to update reservation.")
        input("Press Enter to continue...")


    def removeReservation():
        reservation_dict = reservation_manager.getReservations()
        if not reservation_dict:
            print("No reservations found.")
            input("Press Enter to continue...")
            return

        ReservationPage.printReservation(reservation_dict)
        reservation_id = int(input("Enter the Reservation ID to remove: ").strip())
        reservation = next((res for res in reservation_dict if res['id'] == reservation_id), None)
        if not reservation:
            print("Invalid Reservation ID.")
            input("Press Enter to continue...")
            return

        if reservation_manager.deleteReservation(reservation_id):
            print(f"Reservation {reservation_id} removed successfully.")
        else:
            print("Failed to remove reservation.")
        input("Press Enter to continue...")
    """
