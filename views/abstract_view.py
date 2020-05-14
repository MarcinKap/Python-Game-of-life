from abc import abstractmethod

from views.observer import Observer


class AbstractView(Observer):
    """
    Abstraction for view strategy
    """

    def __init__(self, model):
        super().__init__()
        self.__model = model

    @abstractmethod
    def show(self, *args):
        pass

