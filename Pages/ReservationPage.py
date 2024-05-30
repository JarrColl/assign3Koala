# List reservations
# Add Reservation
# Delete Reservation
# Edit Reservation
import os

from DatabaseConnection import DatabaseConnection
from MainClasses.Reservation import Reservation
from MainClasses.Table import Table
from Managers.LoginManager import LoginManager
from Managers.ReservationManager import ReservationManager
from Pages.Page import Page

db = DatabaseConnection()
reservation_manager = ReservationManager(db)
reservation_list = reservation_manager.getReservations()


class ReservationPage(Page):

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display(login_manager: LoginManager) -> bool:
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
        return True

    @staticmethod
    def printReservation():
        for reservation in reservation_list:
            print(
                "----------Reservation ID: " + str(reservation.getId()) + "----------"
            )
            print(
                "Table ID: "
                + str(reservation.getTable().getId())
                + "   |   Time Slot: "
                + reservation.getTimeSlot()
            )
        print("_____________________________________")

    @staticmethod
    def getTimeSlot():
        time_slots = ["Breakfast Hour", "Lunch Hour", "Dinner Hour"]
        print("Available Time Slots:")
        for idx, slot in enumerate(time_slots):
            print(f"{idx + 1}. {slot}")
        time_slot_index = int(input("Choose a time slot (number): ").strip()) - 1
        if time_slot_index not in range(len(time_slots)):
            print("Invalid time slot choice.")
            input("Press Enter to continue...")
            return None
        return time_slots[time_slot_index]

    @staticmethod
    def getAvailableTables(time_slot):
        table_dict = db.getTableData("tables")
        reserved_table_ids = [
            res.getTable().getId()
            for res in reservation_list
            if res.getTimeSlot() == time_slot
        ]
        available_tables = [
            table for table in table_dict if table["id"] not in reserved_table_ids
        ]
        return available_tables

    @staticmethod
    def addReservation():
        time_slot = ReservationPage.getTimeSlot()
        if not time_slot:
            return

        available_tables = ReservationPage.getAvailableTables(time_slot)
        if not available_tables:
            print("No available tables for this time slot.")
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
        if table_id not in [table["id"] for table in available_tables]:
            print("Invalid Table ID.")
            input("Press Enter to continue...")
            ReservationPage.clear_screen()
            return

        reserved_table = Table(table_id, "occupied")
        new_reservation_id = reservation_list[len(reservation_list) - 1].getId() + 1
        if new_reservation_id:
            rev = Reservation(new_reservation_id, reserved_table, time_slot)
            reservation_manager.addReservation(rev)
            print(f"Reservation created with ID: {new_reservation_id}")
        else:
            print("Failed to create reservation.")
        input("Press Enter to continue...")
        return

    @staticmethod
    def editReservation():
        if not reservation_list:
            print("No reservations found.")
            input("Press Enter to continue...")
            return

        ReservationPage.printReservation()
        reservation_id = int(input("Enter the Reservation ID to edit: ").strip())
        reservation = next(
            (res for res in reservation_list if res.getId() == reservation_id), None
        )
        if not reservation:
            print("Invalid Reservation ID.")
            input("Press Enter to continue...")
            return

        time_slot = ReservationPage.getTimeSlot()
        if not time_slot:
            return

        available_tables = ReservationPage.getAvailableTables(time_slot)
        if not available_tables:
            print("No available tables for this time slot.")
            input("Press Enter to continue...")
            return

        print("Available Tables:")
        for table in available_tables:
            print(f"Table ID: {table['id']} Status: {table['status']}")

        new_table_id = int(input("Enter the new Table ID: ").strip())
        if new_table_id not in [table["id"] for table in available_tables]:
            print("Invalid Table ID.")
            input("Press Enter to continue...")
            return

        new_reservation = Reservation(
            reservation_id, Table(new_table_id, "free"), time_slot
        )
        if reservation_manager.editReservation(new_reservation):
            print(f"Reservation {reservation_id} updated successfully.")
        else:
            print("Failed to update reservation.")
        input("Press Enter to continue...")

    @staticmethod
    def removeReservation():
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
        reservation = next(
            (res for res in reservation_list if res.getId() == reservation_id), None
        )
        if not reservation:
            print("Invalid Reservation ID.")
            input("Press Enter to continue...")
            return

        if reservation_manager.removeReservation(reservation_id):
            print(f"Reservation {reservation_id} removed successfully.")
        else:
            print("Failed to remove reservation.")
        input("Press Enter to continue...")
