class Table:
    def __init__(self, id: int, status: str):
        self._id: int = id
        self._status: str = status
    
    def getId(self) -> int:
        return self._id
    
    def getStatus(self) -> str:
        return self._status
    
    def setStatus(self, status: str) -> None:
        self._status = status
