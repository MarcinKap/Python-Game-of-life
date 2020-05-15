from views.abstract_view import AbstractView


class InputBoxView(AbstractView):

    def __init__(self, model):
        super( ).__init__(model )
        self.__model = model

    def update(self, arg):
        print('')

    def show(self, screenboard):
        self.__model.draw(screenboard)
