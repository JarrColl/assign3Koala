from typing import List
from Order import Order
from ..MainClasses.DeliveryDriver import DeliveryDriver


class Delivery:

    def __init__(self, id: int, order: Order, status: str):
        self.id: int = id
        self.status: str = status
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

    def getStatus(self) -> str:
        return self.status

    def setStatus(self, status: str):
        self.status = status
