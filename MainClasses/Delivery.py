from MainClasses.DeliveryDriver import DeliveryDriver

#TODO: change isDelivered to isDelivered

class Delivery:

    def __init__(self, id: int, order: int, isDelivered: bool):
        self.id: int = id
        self.isDelivered: str = isDelivered
        self.delivery_driver: DeliveryDriver = None
        self.orderId: int = order

    def getId(self) -> int:
        return self.id

    def getOrder(self) -> int:
        return self.order

    def getDeliveryDriver(self) -> DeliveryDriver:
        return self.driver

    def setDeliveryDriver(self, driver: DeliveryDriver):
        self.driver = driver

    def getIsDelivered(self) -> str:
        return self.isDelivered

    def setIsDelivered(self, isDelivered: str):
        self.isDelivered = isDelivered
