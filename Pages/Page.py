from abc import ABC, abstractmethod


class Page(ABC):
    """
    The Page interface declares display operations so that child classes can be passed to a common function when moving through the interface.
    """

    @abstractmethod
    def display(self, login_manager):
        pass
