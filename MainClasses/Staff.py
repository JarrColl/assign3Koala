from MainClasses.Role import Role


class Staff:
    def __init__(self, id, name: str, role: Role):
        self.id: int = id
        self.name: str = name
        self.role: Role = role

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getRole(self) -> Role:
        return self.role

    def setRole(self, role: Role):
        self.role = role
