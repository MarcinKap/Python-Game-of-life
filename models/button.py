import pygame


class Button( ):
    def __init__(self, color, x, y, width, height, font_size, text='', name=''):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__font_size = font_size
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        self.__color= val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.__width = val

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, val):
        self.__text = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, val):
        self.__font_size = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width( ) / 2), self.y + (self.height / 2 - text.get_height( ) / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def action(self):
        print('cos')
