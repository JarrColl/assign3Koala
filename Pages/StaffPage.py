# !!! Only accessed by manager role.
# List all staff information
from DatabaseConnection import DatabaseConnection
from Managers.LoginManager import LoginManager
from OptionSelection import OptionSelection


db = DatabaseConnection()

class StaffPage:
    @staticmethod
    def display(login_manager: LoginManager):
        if not login_manager.staff or login_manager.staff.getRole().getName() != "Manager":
            print("Access denied. Only managers can access this page.")
        else:
            staff_data = db.getTableData("staff")
            StaffPage.print_staff_info(staff_data)
        while True:
            return OptionSelection.show([], "Menu: ", "Return")



    @staticmethod
    def print_staff_info(staff_data):
        print("----------Staff Information----------")

        header = "| {:<5} | {:<20} | {:<20} | {:<10} |".format("ID", "Username", "Name", "Role")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for staff in staff_data:
            role = "Manager" if staff['role'] == 0 else "Staff"
            print("| {:<5} | {:<20} | {:<20} | {:<10} |".format(staff['id'], staff['username'], staff['name'], role))

        print("-" * len(header))

