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
