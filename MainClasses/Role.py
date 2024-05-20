class Role:
    def __init__(self, role_id: int, name: str, desc: str, permissions: list):
        self._id = role_id
        self._name = name
        self._desc = desc
        self._permissions = permissions
    
    def getId(self) -> int:
        return self._id
    
    def getName(self) -> str:
        return self._name
    
    def getDesc(self) -> str:
        return self._desc
    
    def getPermissions(self) -> list:
        return self._permissions
