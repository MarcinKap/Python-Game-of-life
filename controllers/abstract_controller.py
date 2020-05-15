from abc import ABC, abstractmethod


class AbstractController(ABC):
    """
    Abstract controller is a abstraction for all controllers
    """

    def __init__(self, model, view):
        super( ).__init__( )
        self.model = model
        self.view = view
