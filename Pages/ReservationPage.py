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
reservation_list = reservation_manager.getReservations()


class ReservationPage(Page):


    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(login_manager):
        table_dict = db.getTableData("tables")
        while True:
            ReservationPage.clear_screen()
            ReservationPage.printReservation()
            print("\nOptions: (a)dd, (e)dit, (r)emove, (q)uit")
            user_input = input("Enter your choice: ").strip().lower()

            if user_input == "q":
                break
            elif user_input == "a":
                ReservationPage.clear_screen()
                ReservationPage.addReservation()
            elif user_input == "e":
                ReservationPage.clear_screen()
                ReservationPage.editReservation()
            elif user_input == "r":
                ReservationPage.clear_screen()
                ReservationPage.removeReservation()


    def printReservation():
        for reservation in reservation_list:
            print('----------Reservation ID: ' + str(reservation.getId()) + "----------")

            print('Table ID: ' + str(reservation.getTable().getId()) + "   |   Status: " + reservation.getTable().getStatus())
        print('_____________________________________')


    def addReservation():
        table_dict = db.getTableData("tables")
        available_tables = [table for table in table_dict if table['status'] == 'free']
        if not available_tables:
            print("No available tables.")
            input("Press Enter to continue...")
            return

        print("Available Tables:")
        for table in available_tables:
            print(f"Table ID: {table['id']} Status: {table['status']}")

        table_id_input = input("Enter the Table ID to reserve: ").strip()
        if not table_id_input.isdigit():
            print("Table ID must be an integer.")
            input("Press Enter to continue...")
            ReservationPage.clear_screen()
            return

        table_id = int(table_id_input)
        if table_id not in [table['id'] for table in available_tables]:
            print("Invalid Table ID.")
            input("Press Enter to continue...")
            ReservationPage.clear_screen()
            return

        reserved_table = Table(table_id, "occupied")
        for table in table_dict:
            if table['id'] == table_id:
                table['status'] = 'occupied'
        db.writeTableData("tables", table_dict)
        new_reservation_id = len(reservation_list) + 1
        if new_reservation_id:
            rev = Reservation(new_reservation_id, reserved_table)
            reservation_manager.addReservation(rev)
            print(f"Reservation created with ID: {new_reservation_id}")
        else:
            print("Failed to create reservation.")
        input("Press Enter to continue...")
        return


    def editReservation():
        table_dict = db.getTableData("tables")
        if not reservation_list:
            print("No reservations found.")
            input("Press Enter to continue...")
            return

        ReservationPage.printReservation()
        reservation_id = int(input("Enter the Reservation ID to edit: ").strip())
        reservation = next((res for res in reservation_list if res.getId() == reservation_id), None)
        old_table_id = reservation.getTable().getId()
        if not reservation:
            print("Invalid Reservation ID.")
            input("Press Enter to continue...")
            return

        available_tables = [table for table in table_dict if table['status'] == 'free']
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

        if reservation_manager.editReservation(reservation_id, new_table_id):
            for table in table_dict:
                if table['id'] == old_table_id:
                    table['status'] = "free"
                if table['id'] == new_table_id:
                    table['status'] = 'occupied'
            db.writeTableData("tables", table_dict)
            print(f"Reservation {reservation_id} updated successfully.")
        else:
            print("Failed to update reservation.")
        input("Press Enter to continue...")


    def removeReservation():
        table_dict = db.getTableData("tables")
        if not reservation_list:
            print("No reservations found.")
            input("Press Enter to continue...")
            return

        ReservationPage.printReservation()
        reservation_id_input = input("Enter the Reservation ID to remove: ").strip()

        if not reservation_id_input.isdigit():
            print("Reservation ID must be an integer.")
            input("Press Enter to continue...")
            ReservationPage.clear_screen()
            return

        reservation_id = int(reservation_id_input)
        reservation = next((res for res in reservation_list if res.getId() == reservation_id), None)
        if not reservation:
            print("Invalid Reservation ID.")
            input("Press Enter to continue...")
            return

        if reservation_manager.removeReservation(reservation_id):
            table_id = reservation.getTable().getId()
            for table in table_dict:
                if table['id'] == table_id:
                    table['status'] = 'free'
            db.writeTableData("tables", table_dict)
            print(f"Reservation {reservation_id} removed successfully.")
        else:
            print("Failed to remove reservation.")
        input("Press Enter to continue...")




