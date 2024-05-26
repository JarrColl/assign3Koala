from typing import List


class Role:
    def __init__(self, role_id: int, name: str, desc: str, permissions: List[str]):
        self._id: int = role_id
        self._name: str = name
        self._desc: str = desc
        self._permissions: List[str] = permissions
    
    def getId(self) -> int:
        return self._id
    
    def getName(self) -> str:
        return self._name
    
    def getDesc(self) -> str:
        return self._desc
    
    def getPermissions(self) -> List[str]:
        return self._permissions
