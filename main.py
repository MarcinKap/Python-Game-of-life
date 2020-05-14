import pygame
from pygame import init as pyg_init, draw, time, event, QUIT, display

from controllers.board_controller import BoardController
from models.board import Board
from views.board_view import BoardView


def main():
    print("zaczynamy")

    board_model = Board((255, 255, 255), 640, 480)
    board_view = BoardView(board_model)
    board_controller = BoardController(board_model, board_view)

    board_controller.create_buttons()
    board_controller.create_inputs()


    board_view.show()

if '__main__' == __name__:
    main( )
