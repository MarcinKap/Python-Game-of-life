# from model.abstract_model import AbstractModel
from models.abstract_model import AbstractModel


class StandardModel(AbstractModel):

    def __init__(self, board, game_logic):
        super().__init__(board, game_logic)

    def notify(self, data):
        for observer in self.observer_list:
            observer.update()

    def next_iteration(self):
        self.game_logic.check_status(self.board)
        self.notify(self)

    def change_cell_state(self, row, column):
        self.game_logic.change_cell_status(self.board, row, column)
        self.notify(self)

