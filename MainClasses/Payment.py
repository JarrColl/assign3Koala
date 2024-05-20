from PaymentMethod import PaymentMethod


class Payment:
    def __init__(self, payment_method: PaymentMethod, amount: float):
        self.payment_method: PaymentMethod = payment_method
        self.amount: float = amount

    def makePayment(self) -> bool:
        return self.payment_method.makePayment()
