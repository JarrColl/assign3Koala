from typing import List

from MenuItem import MenuItem


class Order:
    def __init__(self) -> None:
        self.menuItems: List[MenuItem] = []

    def AddMenuItem(self, menuItem: MenuItem):
        self.menuItems.append(menuItem)
