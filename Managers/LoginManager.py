from DatabaseConnection import DatabaseConnection
from MainClasses.Staff import Staff
from MainClasses.Role import Role


class LoginManager:

    def __init__(self, db: DatabaseConnection):
        self.staff = None
        self.db: DatabaseConnection = db

    def login(self, username: str, password: str) -> bool:
        staff_list = self.db.getTableData("staff")
        # TODO: When the staff object is created, use the read in data to create the staff object and store it.
        staff_dict = next(
            (
                staff
                for staff in staff_list
                if (staff["username"] == username and staff["password"] == password)
            ),
            None,
        )
        if staff_dict:
            role_list = self.db.getTableData("roles")
            role_dict = next(
                (role for role in role_list if (role["id"] == staff_dict["id"])),
                None,
            )
            role = Role(role_dict["id"], role_dict["name"], role_dict["description"])
            self.staff = Staff(staff_dict["id"], staff_dict["name"], role)
            return True

        return False

    def checkAccess(self, staff: Staff, role: Role):
        pass
