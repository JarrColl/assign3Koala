class Role:
    def __init__(self, role_id: int, name: str, desc: str):
        self.id: int = role_id
        self.name: str = name
        self.desc: str = desc

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def getDesc(self) -> str:
        return self.desc
