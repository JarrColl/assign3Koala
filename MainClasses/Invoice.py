from Payment import Payment

class Invoice:
    def __init__(self, id: int, payment: Payment):
        self._id = id
        self._payment = payment

    def getId(self) -> int:
        return self._id

    def getPayment(self) -> Payment:
        return self._payment
