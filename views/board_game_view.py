from models.game_board import GameBoard
from views.abstract_view import AbstractView


class BoardView(AbstractView):

    def __init__(self, model):
        super().__init__(model)
        self.__main_window = GameBoard()
        self.model.add_observer(self)

    # @property
    # def main_window(self):
    #     return self.__main_window
    #
    #
    # def show(self, *args):
    #     self.