from MainClasses.PaymentMethod import PaymentMethod


class Cash(PaymentMethod):
    def makePayment(self) -> bool:
        print("Processing cash payment")
        return True

    @property
    def name(self) -> str:
        return "Cash"
