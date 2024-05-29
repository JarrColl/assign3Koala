from MainClasses.DeliveryDriver import DeliveryDriver
from MainClasses.Order import Order

class Delivery:

    def __init__(self, id: int, order: Order, isDelivered: bool):
        self.id: int = id
        self.isDelivered: str = isDelivered
        self.delivery_driver: DeliveryDriver = None
        self.order: Order = order

    def getId(self) -> int:
        return self.id

    def getOrder(self) -> Order:
        return self.order

    def getDeliveryDriver(self) -> DeliveryDriver:
        return self.driver

    def setDeliveryDriver(self, driver: DeliveryDriver):
        self.driver = driver

    def getIsDelivered(self) -> str:
        return self.isDelivered

    def setIsDelivered(self, isDelivered: str):
        self.isDelivered = isDelivered
