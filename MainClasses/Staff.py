from MainClasses.Role import Role


class Staff:
    def __init__(self, id, name: str, role: Role):
        self._id: int = id
        self._name: str = name
        self._role: str = role

    def getName(self) -> str:
        return self._name

    def setName(self, name: str):
        self._name = name

    def getRole(self) -> str:
        return self._role

    def setRole(self, role: str):
        self._role = role
