from abc import abstractmethod, ABC

from ..Managers.LoginManager import LoginManager


class Page(ABC):
    """
    The Page interface declares display operations so that child classes can be passed to a common function when moving through the interface.
    """

    @abstractmethod
    def display(self, login_manager: LoginManager):
        pass
