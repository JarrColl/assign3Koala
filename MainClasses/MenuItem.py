class MenuItem:
    def __init__(self, id: int, name: str, price: float):
        self.id: int = id
        self.name: str = name
        self.price: float = price

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, price: float):
        self.price = price

    def asDict(self):
        return {"id": self.id, "name": self.name, "price": self.price}
