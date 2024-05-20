class Table:
    def __init__(self, table_id: int, status: str):
        self._id = table_id
        self._status = status
    
    def getId(self) -> int:
        return self._id
    
    def getStatus(self) -> str:
        return self._status
    
    def setStatus(self, status: str) -> None:
        self._status = status
