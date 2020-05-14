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
                mouse_pos = pygame.mouse.get_pos( )
                if evn.type == QUIT:
                    quit( )
                    exit( )
                if stage == 1 or stage == 2:
                    self.__model.find_input('size_game').handle_event(evn)
                    self.__model.find_input('size_game').update( )

                    stage = self.mousebuttondown_actions_stage_1(self.__model.find_input('size_game').text, evn, stage)
                    self.mousemotion_actions_stage_1(evn)
                if stage == 3:


            screen = self.__model.screen
            screen.fill((255, 255, 255))
            # screen_board.fill(screen_color)

            if stage == 1:
                self.show_game_description_button( )
                self.show_accept_button()
                self.show_size_game_input()

            elif stage == 2:
                self.show_game_description_button( )
                self.show_accept_button()
                self.show_size_game_input()
                self.show_wrong_text_button( )
            # elif stage == 2 and aplication_start == 0:
            #
            # elif stage == 3 or aplication_start == 1:
            print(stage)
            pyg_clock.tick(10)
            display.flip( )

    def show_game_description_button(self):
        self.__model.find_button('game_description').draw(self.__model.screen, (0, 0, 0))

    def show_accept_button(self):
        self.__model.find_button('accept_button').draw(self.__model.screen, (0, 0, 0))

    def show_size_game_input(self):
        self.__model.find_input('size_game').draw(self.__model.screen)

    def show_wrong_text_button(self):
        self.__model.find_button('wrong_text').draw(self.__model.screen, (0,0,0))

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

















        # pyg_init( )
        #
        # screen_color = (255, 255, 255)
        # screen_model = Board((255, 255, 255), 640, 480)
        # screen_board = screen_model.create_board( )
        #
        # # Obiekty stage 1
        # # Opis
        # game_description = Button((255, 255, 255), 145, 30, 350, 30, 18,
        #                           'To jest gra w życie wybierz rozmiar planszy od 8 do 14')
        # # Miejsce do wpisania rozmiaru
        # size_game_input = InputBox(145, 80, 350, 30)
        # wrong_text = Button((255, 255, 255), 145, 120, 350, 30, 18,
        #                     'złe dane')
        # # Przycisk akceptacji
        # accept_button = Button((200, 200, 200), 145, 160, 150, 30, 18, 'akceptuj')
        # # Obiekty stage 2
        # start_button = Button((200, 200, 200), 140, 440, 110, 30, 18, 'Start')
        # stop_button = Button((200, 200, 200), 320 - 55, 440, 110, 30, 18, 'Stop')
        # next_button = Button((200, 200, 200), 390, 440, 110, 30, 18, 'Następna iteracja')
        #
        # pyg_clock = time.Clock( )
        #
        # move_x, move_y = 1, 1
        #
        #
        #
        # aplication_start = 0
        # stage = 1
        # error = 0
        # while True:
        #     for evn in event.get( ):
        #         mouse_pos = pygame.mouse.get_pos( )
        #         if evn.type == QUIT:
        #             quit( )
        #             exit( )
        #         if stage == 1:
        #             size_game_input.handle_event(evn)
        #
        #             if evn.type == pygame.MOUSEBUTTONDOWN:
        #                 if accept_button.isOver(mouse_pos):
        #                     if size_game_input.text.isdigit( ) and 8 <= int(size_game_input.text) <= 14:
        #                         stage = 2
        #                         error = 0
        #                         number_of_cells = int(size_game_input.text)
        #
        #                         # board_game = GameBoard(number_of_cells)
        #
        #                         cells = []
        #                         k = (640 - 30 * number_of_cells) / 2
        #                         randomlist = [(0, 0, 0), (200, 200, 200)]
        #                         for i in range(number_of_cells):
        #                             row = []
        #                             for j in range(number_of_cells):
        #                                 row.append(
        #                                     Button(random.choice(randomlist), 30 * i + k, 30 * j + 10, 23, 23, 18, ''))
        #                             cells.insert(i, row)
        #                     else:
        #                         error = 1
        #             if evn.type == pygame.MOUSEMOTION:
        #                 if accept_button.isOver(mouse_pos):
        #                     accept_button.color = (150, 150, 150)
        #                 else:
        #                     accept_button.color = (200, 200, 200)
        #             size_game_input.update( )
        #         if stage == 2 or stage == 3:
        #             if evn.type == pygame.MOUSEBUTTONDOWN:
        #                 for i in range(number_of_cells):
        #                     for j in range(number_of_cells):
        #                         if cells[i][j].isOver(mouse_pos):
        #                             if cells[i][j].color == (200, 200, 200):
        #                                 cells[i][j].color = (0, 0, 0)
        #                             elif cells[i][j].color == (0, 0, 0):
        #                                 cells[i][j].color = (200, 200, 200)
        #                 if start_button.isOver(mouse_pos):
        #                     print('zaczyna sie')
        #                     stage = 3
        #                 if stop_button.isOver(mouse_pos):
        #                     print('stop')
        #                     stage = 2
        #                 if next_button.isOver(mouse_pos):
        #                     print('nastepna iteracja')
        #                     aplication_start = 1
        #
        #             if evn.type == pygame.MOUSEMOTION:
        #                 if start_button.isOver(mouse_pos):
        #                     start_button.color = (150, 150, 150)
        #                 elif stop_button.isOver(mouse_pos):
        #                     stop_button.color = (150, 150, 150)
        #                 elif next_button.isOver(mouse_pos):
        #                     next_button.color = (150, 150, 150)
        #                 else:
        #                     stop_button.color = (200, 200, 200)
        #                     next_button.color = (200, 200, 200)
        #                     start_button.color = (200, 200, 200)
        #
        #     screen_board.fill(screen_color)
        #     if stage == 1:
        #         game_description.draw(screen_board, (0, 0, 0))
        #         size_game_input.draw(screen_board)
        #         accept_button.draw(screen_board, (0, 0, 0))
        #         if error == 1:
        #             wrong_text.draw(screen_board, (255, 0, 0))
        #     elif stage == 2 and aplication_start == 0:
        #         for i in range(number_of_cells):
        #             for j in range(number_of_cells):
        #                 cells[i][j].draw(screen_board)
        #         start_button.draw(screen_board)
        #         stop_button.draw(screen_board)
        #         next_button.draw(screen_board)
        #
        #     elif stage == 3 or aplication_start == 1:
        #
        #         status = check_status(cells, number_of_cells)
        #         cells = change_status(cells, status, number_of_cells)
        #
        #         for i in range(number_of_cells):
        #             for j in range(number_of_cells):
        #                 cells[i][j].draw(screen_board)
        #
        #         start_button.draw(screen_board)
        #         stop_button.draw(screen_board)
        #         next_button.draw(screen_board)
        #         aplication_start = 0
        #
        #     pyg_clock.tick(10)
        #     display.flip( )
