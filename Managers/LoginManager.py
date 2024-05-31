from DatabaseConnection import DatabaseConnection
from MainClasses.Role import Role
from MainClasses.Staff import Staff


class LoginManager:

    def __init__(self, db: DatabaseConnection):
        self.staff = None
        self.db: DatabaseConnection = db

    def login(self, username: str, password: str) -> bool:
        staff_list = self.db.getTableData("staff")
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
                (role for role in role_list if (role["id"] == staff_dict["role"])),
                None,
            )

            if not role_dict:
                print("the user accounts role is invalid, speak to your administrator")
                return False

            role = Role(role_dict["id"], role_dict["name"], role_dict["description"])
            self.staff = Staff(staff_dict["id"], staff_dict["name"], role)
            return True

        return False

    def checkAccess(self, staff: Staff, role: Role):
        if staff.getRole().getId() == role.getId():
            return True
        return False
