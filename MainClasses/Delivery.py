from typing import List
from Order import Order

class Delivery:

    def __init__(self, id, order, status):
        self.id = id
        self.status = status
        self.driver = None
        self.order = order


    def getId(self):
        return self.id

    def getOrder(self):
        return self.order

    def getDriver(self):
        return self.driver

    def setDriver(self, driver):
        self.driver = driver

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

