from abc import abstractmethod


class Page:
    """
    The Page interface declares display operations so that child classes can be passed to a common function when moving through the interface.
    """

    @abstractmethod
    def display(self):
        pass
