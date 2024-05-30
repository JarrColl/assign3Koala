from MainClasses.PaymentMethod import PaymentMethod


class GiftCard(PaymentMethod):
    def makePayment(self) -> bool:
        print("Processing gift card payment")
        return True

    @property
    def name(self) -> str:
        return "Gift Card"
