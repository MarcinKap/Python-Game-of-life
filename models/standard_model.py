# from model.abstract_model import AbstractModel
from models.abstract_model import AbstractModel


class StandardModel(AbstractModel):

    def __init__(self, board, game_logic):
        super().__init__(board, game_logic)

    # notify observer about new changes in model
    def notify(self, data):
        for observer in self.observer_list:
            observer.update()

    # make next iteration for the board using game logic and notify view
    def next_iteration(self):
        self.game_logic.check_status(self.board)
        self.notify(self)

    # change state of single cell and notify about changes view
    def change_cell_state(self, row, column):
        self.game_logic.change_cell_status(self.board, row, column)
        self.notify(self)

