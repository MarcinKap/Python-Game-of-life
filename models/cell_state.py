from enum import Enum

# rezprezentuje status komórki żyje/nie żyje
class CellStatus(Enum):
    dead = (200, 200, 200)
    alive = (0, 0, 0)