class Invoice:
    def __init__(self, id: int, value: float):
        self._id: int = id
        self._value: float = value
        self._is_paid: bool = False

    def getId(self) -> int:
        return self._id

    def setPaid(self):
        self._is_paid = True

    def getValue(self) -> float:
        return self._value
