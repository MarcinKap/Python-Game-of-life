# from view.abstract_view import AbstractView
# from view.board_window import BoardWindow
import random
from operator import pos

from numpy import copy

from models import input_box
from models.board import Board
from models.button import Button
from models.game_board import GameBoard
from models.input_box import InputBox
from views.abstract_view import AbstractView
import pygame
from pygame import init as pyg_init, draw, time, event, QUIT, display


class BoardView(AbstractView):
    def __init__(self, model):
        super( ).__init__(model)
        self.__model = model

    def update(self, arg):
        print('')

    # Uruchamianie głównego programu
    def show(self, *args):

        # Zadanie będzie podzielone na części (stage)
        # Część 1: Wybieramy rozmiar planszy
        # Część 2: Pojawia się plansza
        # Część 3: Rusza gra
        pyg_init( )
        pyg_clock = time.Clock( )

        aplication_start = 0
        stage = 1
        error = 0

        while True:
            for evn in event.get( ):
                if evn.type == QUIT:
                    quit( )
                    exit( )
                if stage == 1 or stage == 2:
                    self.__model.find_input('size_game').handle_event(evn)
                    self.__model.find_input('size_game').update( )
                    stage = self.mousebuttondown_actions_stage_1(self.__model.find_input('size_game').text, evn, stage)
                    self.mousemotion_actions_stage_1(evn)
                if stage == 3 or stage == 4 or stage == 5:
                    stage = self.mousebuttondown_actions_stage_3(evn, stage)
                    self.mousemotion_actions_stages_3_4_5(evn)
            screen = self.__model.screen
            screen.fill((255, 255, 255))

            if stage == 1:
                self.show_game_description_button( )
                self.show_accept_button( )
                self.show_size_game_input( )

            elif stage == 2:
                self.show_game_description_button( )
                self.show_accept_button( )
                self.show_size_game_input( )
                self.show_wrong_text_button( )
            elif stage == 3:
                self.show_board_game( )
                self.show_start_button( )
                self.show_stop_button( )
                self.show_next_button( )

            elif stage == 4 or stage == 5:
                self.__model.game_board.new_state( )
                self.show_board_game( )
                self.show_start_button( )
                self.show_stop_button( )
                self.show_next_button( )
                if stage == 5:
                    stage = 3

            pyg_clock.tick(10)
            display.flip( )

    def show_game_description_button(self):
        self.__model.find_button('game_description').draw(self.__model.screen, (0, 0, 0))

    def show_accept_button(self):
        self.__model.find_button('accept_button').draw(self.__model.screen, (0, 0, 0))

    def show_size_game_input(self):
        self.__model.find_input('size_game').draw(self.__model.screen)

    def show_wrong_text_button(self):
        self.__model.find_button('wrong_text').draw(self.__model.screen, (0, 0, 0))

    def mousebuttondown_actions_stage_1(self, size_game_input, evn, stage):
        mouse_pos = pygame.mouse.get_pos( )
        if evn.type == pygame.MOUSEBUTTONDOWN:
            if self.__model.find_button('accept_button').isOver(mouse_pos):
                if size_game_input.isdigit( ) and 8 <= int(size_game_input) <= 14:
                    self.__model.game_board_setter(GameBoard(int(size_game_input)))
                    return 3
                else:
                    return 2
        elif stage == 2:
            return 2

        return 1

    def mousemotion_actions_stage_1(self, evn):
        mouse_pos = pygame.mouse.get_pos( )
        if evn.type == pygame.MOUSEMOTION:
            if self.__model.find_button('accept_button').isOver(mouse_pos):
                self.__model.find_button('accept_button').color = (150, 150, 150)
            else:
                self.__model.find_button('accept_button').color = (200, 200, 200)
        return 1

    def show_board_game(self):
        for i in range(self.__model.game_board.size):
            for j in range(self.__model.game_board.size):
                self.__model.game_board.cells[i][j].draw(self.__model.screen)

    def show_start_button(self):
        self.__model.find_button('start_button').draw(self.__model.screen, (0, 0, 0))

    def show_stop_button(self):
        self.__model.find_button('stop_button').draw(self.__model.screen, (0, 0, 0))

    def show_next_button(self):
        self.__model.find_button('next_button').draw(self.__model.screen, (0, 0, 0))

    def mousebuttondown_actions_stage_3(self, evn, stage):
        mouse_pos = pygame.mouse.get_pos( )
        if evn.type == pygame.MOUSEBUTTONDOWN:
            for i in range(self.__model.game_board.size):
                for j in range(self.__model.game_board.size):
                    if self.__model.game_board.cells[i][j].isOver(mouse_pos):
                        if self.__model.game_board.cells[i][j].color == (200, 200, 200):
                            self.__model.game_board.cells[i][j].color = (0, 0, 0)
                        elif self.__model.game_board.cells[i][j].color == (0, 0, 0):
                            self.__model.game_board.cells[i][j].color = (200, 200, 200)
            if self.__model.find_button('start_button').isOver(mouse_pos):
                print('zaczyna sie')
                return 4
            elif self.__model.find_button('stop_button').isOver(mouse_pos):
                print('stop')
                return 3
            elif self.__model.find_button('next_button').isOver(mouse_pos):
                print('nastepna iteracja')
                return 5
        return stage

    def mousemotion_actions_stages_3_4_5(self, evn):
        mouse_pos = pygame.mouse.get_pos( )
        if evn.type == pygame.MOUSEMOTION:
            if self.__model.find_button('start_button').isOver(mouse_pos):
                self.__model.find_button('start_button').color = (150, 150, 150)
                self.__model.find_button('stop_button').color = (200, 200, 200)
                self.__model.find_button('next_button').color = (200, 200, 200)
            elif self.__model.find_button('stop_button').isOver(mouse_pos):
                self.__model.find_button('stop_button').color = (150, 150, 150)
                self.__model.find_button('next_button').color = (200, 200, 200)
                self.__model.find_button('start_button').color = (200, 200, 200)
            elif self.__model.find_button('next_button').isOver(mouse_pos):
                self.__model.find_button('next_button').color = (150, 150, 150)
                self.__model.find_button('stop_button').color = (200, 200, 200)
                self.__model.find_button('start_button').color = (200, 200, 200)
            else:
                self.__model.find_button('stop_button').color = (200, 200, 200)
                self.__model.find_button('next_button').color = (200, 200, 200)
                self.__model.find_button('start_button').color = (200, 200, 200)
