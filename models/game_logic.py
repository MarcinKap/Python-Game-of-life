# from model.abstract_game_logic import AbstractGameLogic
# from model.cell_state import CellState
# from model.cell import Cell
from models.abstracts_logic import AbstractLogic


class GameLogic(AbstractLogic):

    # Metoda sprawdza dla każdej komorki czy powinna być martwa czy żywa
    def check_status(self, old_cells, size):
        new_cells = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append((255, 255, 255))
            new_cells.insert(i, row)

        for i in range(size):
            for j in range(size):
                neighbours = get_neighbour_cells(i, j, size, old_cells)

                # liczba zywych sasiadow
                filtered = 0
                # print('komorka: ', i, j)
                # print('kolor: ', old_cells[i][j].color)
                for neighbour in neighbours:
                    # print('sasiad')
                    if neighbour.color == (0, 0, 0):
                        filtered = filtered + 1
                print('komorka: ', i, j, 'ilosc zywych sasiadow: ', filtered)

                # print('ilosc zywych sasiadow: ', filtered)

                # martwa komorka
                if old_cells[i][j].color == (200, 200, 200):
                    if filtered == 3:
                        # new_cells[i][j].color = (0, 0, 0)
                        new_cells[i][j] = (0, 0, 0)
                    else:
                        new_cells[i][j] = (200, 200, 200)

                # zywa komorka
                if old_cells[i][j].color == (0, 0, 0):
                    if filtered == 3 or filtered == 2:
                        new_cells[i][j] = (0, 0, 0)
                    else:
                        new_cells[i][j] = (200, 200, 200)

        return new_cells

    # this method change state of cell for opposite,
    # cell is localized based on row and column
    def change_cell_status(self, old_cells, new_cells, size):
        for i in range(size):
            for j in range(size):
                old_cells[i][j].color = new_cells[i][j]
        return old_cells


