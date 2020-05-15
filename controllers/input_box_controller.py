from controllers.abstract_controller import AbstractController


class InputBoxController(AbstractController):

    def __init__(self, button_model, button_view):
        super( ).__init__(button_model, button_view)

    def setter(self, color, x, y, width, height, font_size, text='', name=''):
        self.model.color = color
        self.model.x = x
        self.model.y = y
        self.model.width = width
        self.model.height = height
        self.model.font_size = font_size
        self.model.text = text
        self.model.name = name

    def get_name(self):
        return self.model.name
