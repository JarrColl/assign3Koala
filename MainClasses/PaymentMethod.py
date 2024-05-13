from abc import abstractmethod


class PaymentMethod:
    """
    Abstract class for implementing a strategy pattern for payment methods.
    """

    @abstractmethod
    def makePayment():
        pass
