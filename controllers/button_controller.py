import pygame

from controllers.abstract_controller import AbstractController
from models.abstract_model import AbstractModel


class ButtonController(AbstractController):

    def __init__(self, button_model, button_view):
        super( ).__init__(button_model, button_view)

    def setter(self, color, x, y, width, height, font_size, text='', name=''):
        self.model.color = color
        self.model.x = x
        self.model.y = y
        self.model.width = width
        self.model.height = height
        self.model.font_size = font_size
        self.model.text =text
        self.model.name = name

    def set_color(self, color):
        self.model.color = color
    def get_color(self):
        return self.model.color


    def mousemotion_shading(self):
        mouse_pos = pygame.mouse.get_pos( )
        if self.model.isOver(mouse_pos):
            self.model.color = (150, 150, 150)
        else:
            self.model.color = (200, 200, 200)


    def mousebuttondown_changing_color(self):
        if self.model.color == (200, 200, 200):
            self.model.color = (0, 0, 0)
        elif self.model.color == (0, 0, 0):
            self.model.color = (200, 200, 200)
