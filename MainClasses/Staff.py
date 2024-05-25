from MainClasses.Role import Role


class Staff:
    def __init__(self, name: str, role: Role):
        self.name: str = name
        self.role: str = name

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getRole(self) -> str:
        return self.role

    def setRole(self, role: str):
        self.role = role
