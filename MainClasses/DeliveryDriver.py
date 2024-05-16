class DeliveryDriver:

    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def getDescription(self) -> str:
        return self.description
