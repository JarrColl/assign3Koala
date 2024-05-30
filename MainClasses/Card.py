from MainClasses.PaymentMethod import PaymentMethod


class Card(PaymentMethod):
    def makePayment(self) -> bool:
        print("Processing card payment")
        return True

    @property
    def name(self) -> str:
        return "Card"
