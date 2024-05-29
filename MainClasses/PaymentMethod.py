from abc import abstractmethod, ABC


class PaymentMethod(ABC):
    """
    Abstract class for implementing a strategy pattern for payment methods.
    """

    @abstractmethod
    def makePayment() -> bool:
        pass
