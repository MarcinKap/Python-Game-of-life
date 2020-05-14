import random

import pygame

from models.button import Button


class GameBoard:
    def __init__(self, size):
        self.__size = size
        self.__cells = self.create_random_cells(size)

    @property
    def size(self):
        return self.__size

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, val):
        self.__cells = val

    def create_random_cells(self, size):
        cells = []
        k = (640 - 30 * size) / 2
        randomlist = [(0, 0, 0), (200, 200, 200)]
        for i in range(size):
            row = []
            for j in range(size):
                row.append(
                    Button(random.choice(randomlist), 30 * i + k, 30 * j + 10, 23, 23, 18, ''))
            cells.insert(i, row)
        return cells

    # get all neighbour cells for cell with coordinates as row and column
    def get_neighbour_cells(self, row, column):
        neighbour_cells = list( )
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if i >= 0 and j >= 0 and not (i == row and j == column) and not j > self.size - 1 \
                        and not i > self.size - 1:
                    neighbour_cells.append(self.cells[i][j])
        return neighbour_cells

    def get_next_state(self):
        new_cells = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append((255, 255, 255))
            new_cells.insert(i, row)

        for i in range(self.size):
            for j in range(self.size):
                neighbours = self.get_neighbour_cells(i, j)
                # liczba zywych sasiadow
                filtered = 0
                # print('komorka: ', i, j)
                # print('kolor: ', old_cells[i][j].color)

                # sprawdza ilosc zywych sasiadow
                for neighbour in neighbours:
                    # print(neighbour.color)
                    # print('sasiad')
                    if neighbour.color == (0, 0, 0):
                        filtered = filtered + 1
                # print('komorka: ', i, j, 'ilosc zywych sasiadow: ', filtered)

                # print('ilosc zywych sasiadow: ', filtered)

                # martwa komorka
                if self.cells[i][j].color == (200, 200, 200):
                    if filtered == 3:
                        # new_cells[i][j].color = (0, 0, 0)
                        new_cells[i][j] = (0, 0, 0)
                    else:
                        new_cells[i][j] = (200, 200, 200)

                # zywa komorka
                if self.cells[i][j].color == (0, 0, 0):
                    if filtered == 3 or filtered == 2:
                        new_cells[i][j] = (0, 0, 0)
                    else:
                        new_cells[i][j] = (200, 200, 200)

        return new_cells

    def change_cell_color(self, array):
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].color = array[i][j]

    def new_state(self):
        state = self.get_next_state()
        self.change_cell_color(state)
