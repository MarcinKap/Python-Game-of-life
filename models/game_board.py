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
                if i >= 0 and j >= 0 and not (i == row and j == column) and not j > self.size - 1\
                        and not i > self.size - 1:
                    neighbour_cells.append(self.cells[i][j])
        return neighbour_cells
