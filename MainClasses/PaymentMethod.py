from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """
    Abstract class for implementing a strategy pattern for payment methods.
    """

    @abstractmethod
    def makePayment() -> bool:
        pass
