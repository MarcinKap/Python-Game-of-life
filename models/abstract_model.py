from abc import ABC, abstractmethod


class AbstractModel(ABC):
    def __init__(self, board, game_logic):
        super().__init__()
        self.__board = board
        self.__game_logic = game_logic
        self.__observer_list = list()

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, val):
        self.__board = val

    @property
    def game_logic(self):
        return self.__game_logic

    @game_logic.setter
    def game_logic(self, val):
        self.__game_logic = val

    @property
    def observer_list(self):
        return self.__observer_list

    def add_observer(self, observer):
        self.observer_list.append(observer)

    @abstractmethod
    def notify(self, data):
        pass

    @abstractmethod
    def next_iteration(self):
        pass

    @abstractmethod
    def change_cell_state(self, row, column):
        pass
