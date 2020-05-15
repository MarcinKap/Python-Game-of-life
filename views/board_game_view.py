from models.board_game import BoardGame
from views.abstract_view import AbstractView


class BoardGameView(AbstractView):

    def __init__(self, model):
        super().__init__(model)
        self.__model = model

    def update(self, arg):
        print('')

    def show(self, screenboard, color=None):
        if color:
            self.__model.draw(screenboard, color)

        self.__model.draw(screenboard)

        # game_description.draw(screen_board, (0, 0, 0))


    # @property
    # def main_window(self):
    #     return self.__main_window
    #
    #
    # def show(self, *args):
    #     self.