from abc import ABC, abstractmethod

from Managers.LoginManager import LoginManager


class Page(ABC):
    """
    The Page interface declares display operations so that child classes can be passed to a common function when moving through the interface.
    """

    @staticmethod
    @abstractmethod
    def display(login_manager: LoginManager) -> bool:
        pass
