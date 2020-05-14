# from controller.abstract_controller import AbstractController
from tkinter import messagebox

import pygame

from controllers.abstract_controller import AbstractController
from models.button import Button
from models.game_board import GameBoard
from models.input_box import InputBox


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

    def addInput(self, input):
        self.model.add_input(input)

    def create_buttons(self):
        # Opis
        game_description = Button((255, 255, 255), 145, 30, 350, 30, 18,
                                  'To jest gra w życie wybierz rozmiar planszy od 8 do 14', 'game_description')
        wrong_text = Button((255, 255, 255), 145, 120, 350, 30, 18, 'złe dane', 'wrong_text')
        # Przycisk akceptacji
        accept_button = Button((200, 200, 200), 145, 160, 150, 30, 18, 'akceptuj', 'accept_button')
        # Przyciski stage 2
        start_button = Button((200, 200, 200), 140, 440, 110, 30, 18, 'Start', 'start_button')
        stop_button = Button((200, 200, 200), 320 - 55, 440, 110, 30, 18, 'Stop', 'stop_button')
        next_button = Button((200, 200, 200), 390, 440, 110, 30, 18, 'Następna iteracja', 'next_button')

        self.model.add_button(game_description)
        self.model.add_button(wrong_text)
        self.model.add_button(accept_button)
        self.model.add_button(start_button)
        self.model.add_button(stop_button)
        self.model.add_button(next_button)

    def create_inputs(self):
        size_game_input = InputBox(145, 80, 350, 30, name='size_game')
        self.addInput(size_game_input)

    def create_game_board(self, size):
        self.model.game_board(GameBoard(size))

