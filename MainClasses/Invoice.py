class Invoice:
    def __init__(self, id: int, value: float):
        self.id: int = id
        self.value: float = value
        self.is_paid: bool = False

    def getId(self) -> int:
        return self.id

    def setPaid(self):
        self.is_paid = True

    def getPaid(self):
        return self.is_paid

    def getValue(self) -> float:
        return self.value
