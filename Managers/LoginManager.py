from ..DatabaseConnection import DatabaseConnection
from ..MainClasses.Staff import Staff


class LoginManager:

    def __init__(self, db: DatabaseConnection):
        self.db: DatabaseConnection = db

    def login(username: str, password: str):
        pass

    def checkAccess(staff: Staff, permission: str):
        pass
