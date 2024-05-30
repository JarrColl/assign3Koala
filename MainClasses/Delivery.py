from typing import Optional

from MainClasses.DeliveryDriver import DeliveryDriver
from MainClasses.Order import Order


class Delivery:

    def __init__(self, id: int, order: Order, address: str, isDelivered: bool = False):
        self.id: int = id
        self.delivery_driver: Optional[DeliveryDriver] = None
        self.order: Order = order
        self.isDelivered: bool = isDelivered

    def getId(self) -> int:
        return self.id

    def getOrder(self) -> Order:
        return self.order

    def getDeliveryDriver(self) -> DeliveryDriver:
        return self.driver

    def setDeliveryDriver(self, driver: DeliveryDriver):
        self.driver = driver

    def getIsDelivered(self) -> bool:
        return self.isDelivered

    def setIsDelivered(self, isDelivered: bool):
        self.isDelivered = isDelivered
