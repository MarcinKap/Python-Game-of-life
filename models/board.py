# from model.cell import Cell
# from model.cell_state import CellState
import random

import pygame

from controllers.board_game_controller import BoardGameController
from models.board_game import BoardGame
from views.board_game_view import BoardGameView


class Board:
    def __init__(self, color, x_size, y_size):
        self.__x_size = x_size
        self.__color = color
        self.__y_size = y_size
        self.__game_board = self.create_empty_game_board( )
        self.__buttons = []
        self.__inputs = []
        self.__screen = self.create_board()

    @property
    def x_size(self):
        return self.__x_size

    @property
    def y_size(self):
        return self.__y_size

    @property
    def color(self):
        return self.__color

    @property
    def game_board(self):
        return self.__game_board

    @property
    def screen(self):
        return self.__screen

    def game_board_setter(self, game_board):
        self.__game_board = game_board

    # create board
    def create_board(self):
        return pygame.display.set_mode((self.__x_size, self.__y_size))

    def create_empty_game_board(self):
        model = BoardGame(1)
        view = BoardGameView(model)
        controller = BoardGameController(model, view)
        return controller

    def add_button(self, button):
        self.__buttons.append(button)

    def add_input(self, input_form):
        self.__inputs.append(input_form)

    def find_button(self, name):
        for button in self.__buttons:
            if button.model.name == name:
                return button

    def find_input(self, name):
        for input in self.__inputs:
            if input.model.name == name:
                return input