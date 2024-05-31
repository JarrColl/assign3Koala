from typing import Literal


class Table:
    def __init__(self, id: int, status: str):
        self.id: int = id
        self.status: str = status

    def getId(self) -> int:
        return self.id

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status: Literal["free", "occupied"]) -> None:
        self.status = status

    def asDict(self):
        return {"id": self.id, "status": self.status}
