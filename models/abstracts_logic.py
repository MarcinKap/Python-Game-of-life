from abc import ABC, abstractmethod


class AbstractLogic(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def check_status(self):
        pass

    @abstractmethod
    def change_cell_status(self, board, row, column):
        pass