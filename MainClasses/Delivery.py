from typing import Optional

from DatabaseConnection import DatabaseConnection
from MainClasses.DeliveryDriver import DeliveryDriver
from MainClasses.Order import Order

db = DatabaseConnection()


class Delivery:
    def __init__(
        self, order: Order, address: str, id: int = None, isDelivered: bool = False
    ):
        if id:
            self.id = id
        else:
            delivery_dict = db.getTableData("deliveries")
            if len(delivery_dict) > 0:
                next_id = max(delivery_dict, key=lambda x: x["id"])["id"] + 1
            else:
                next_id = 0
            self.id: int = next_id

        self.address: str = address
        self.delivery_driver: Optional[DeliveryDriver] = None
        self.order: Order = order
        self.is_delivered: bool = isDelivered

    def getId(self) -> int:
        return self.id

    def getOrder(self) -> Order:
        return self.order

    def getDeliveryDriver(self) -> DeliveryDriver:
        return self.driver

    def setDeliveryDriver(self, driver: DeliveryDriver):
        self.driver = driver

    def getIsDelivered(self) -> bool:
        return self.is_delivered

    def setIsDelivered(self, isDelivered: bool):
        self.is_delivered = isDelivered

    def getAddress(self) -> str:
        return self.address

    def setAddress(self, address: str):
        self.address = address

    def asDict(self):
        return {
            "id": self.id,
            "address": self.address,
            "delivery_driver": self.delivery_driver,
            "order_id": self.order.getId(),
            "is_delivered": self.is_delivered,
        }
