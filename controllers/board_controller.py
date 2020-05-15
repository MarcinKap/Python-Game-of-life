# from controller.abstract_controller import AbstractController
from tkinter import messagebox

import pygame

from controllers.abstract_controller import AbstractController
from controllers.board_game_controller import BoardGameController
from controllers.button_controller import ButtonController
from controllers.input_box_controller import InputBoxController
from models.button import Button
from models.board_game import BoardGame
from models.input_box import InputBox
from views.board_game_view import BoardGameView
from views.button_view import ButtonView
from views.input_box_view import InputBoxView


class BoardController(AbstractController):

    def __init__(self, game_model, game_view):
        super( ).__init__(game_model, game_view)
        # self.__stopTimer = True
        # self.__bind_start_page_buttons()

    # def mousebuttondown(self, evn, button):
    #     mouse_pos = pygame.mouse.get_pos( )
    #     if evn.type == pygame.MOUSEBUTTONDOWN:
    #         if(button.isOver(mouse_pos)):
    def add_button(self, button):
        self.model.add_button(button)

    def add_input(self, input):
        self.model.add_input(input)

    def create_buttons(self):
        self.create_button((255, 255, 255), 145, 30, 350, 30, 18,
                           'To jest gra w życie wybierz rozmiar planszy od 8 do 14', 'game_description')
        self.create_button((255, 255, 255), 145, 120, 350, 30, 18, 'złe dane', 'wrong_text')
        self.create_button((200, 200, 200), 145, 160, 150, 30, 18, 'akceptuj', 'accept_button')
        self.create_button((200, 200, 200), 140, 440, 110, 30, 18, 'Start', 'start_button')
        self.create_button((200, 200, 200), 320 - 55, 440, 110, 30, 18, 'Stop', 'stop_button')
        self.create_button((200, 200, 200), 390, 440, 110, 30, 18, 'Następna iteracja', 'next_button')

        # game_description = Button((255, 255, 255), 145, 30, 350, 30, 18,
        #                           'To jest gra w życie wybierz rozmiar planszy od 8 do 14', 'game_description')
        # wrong_text = Button((255, 255, 255), 145, 120, 350, 30, 18, 'złe dane', 'wrong_text')
        # # Przycisk akceptacji
        # accept_button = Button((200, 200, 200), 145, 160, 150, 30, 18, 'akceptuj', 'accept_button')
        # # Przyciski stage 2
        # start_button = Button((200, 200, 200), 140, 440, 110, 30, 18, 'Start', 'start_button')
        # stop_button = Button((200, 200, 200), 320 - 55, 440, 110, 30, 18, 'Stop', 'stop_button')
        # next_button = Button((200, 200, 200), 390, 440, 110, 30, 18, 'Następna iteracja', 'next_button')
        #
        # self.model.add_button(game_description)
        # self.model.add_button(wrong_text)
        # self.model.add_button(accept_button)
        # self.model.add_button(start_button)
        # self.model.add_button(stop_button)
        # self.model.add_button(next_button)

    def create_inputs(self):
        self.create_input(145, 80, 350, 30, name='size_game')

    def create_input(self, x, y, w, h, text='', name=''):
        model = InputBox(x, y, w, h, text, name)
        view = InputBoxView(model)
        controller = InputBoxController(model, view)
        self.add_input(controller)

    def create_game_board(self, size):
        model = BoardGame(size)
        view = BoardGameView(model)
        controller = BoardGameController(model, view)
        self.model.game_board(controller)

    def create_button(self, color, x, y, width, height, font_size, text='', name=''):
        model = Button(color, x, y, width, height, font_size, text, name)
        view = ButtonView(model)
        controller = ButtonController(model, view)
        self.add_button(controller)
