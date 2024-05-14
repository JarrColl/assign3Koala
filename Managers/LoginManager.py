from ..DatabaseConnection import DatabaseConnection
from ..MainClasses.Staff import Staff


class LoginManager:

    def __init__(self, db: DatabaseConnection):
        self.staff = None
        self.db: DatabaseConnection = db

    def login(self, username: str, password: str):
        staff_list = self.db.getTableData("staff")
        # TODO: When the staff object is created, use the read in data to create the staff object and store it.
        next(
            (
                staff
                for staff in staff_list
                if (staff["username"] == username and staff["password"] == password)
            ),
            None,
        )

    def checkAccess(self, staff: Staff, permission: str):
        pass
