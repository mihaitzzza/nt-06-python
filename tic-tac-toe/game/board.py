import itertools
from game.players import Player


class Cell:
    """This class represents the cell of a board

    Each cell can have a particular sign or can be empty.
    """

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._value = None

    @property
    def position(self):
        return self._x * 3 + self._y + 1

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    # def set_value(value):
    #   self._value = value
    # cell = Cell()
    # cell.set_value('X') <<<[JAVA - Using a setter] vs [PYTHON Using a property/setter]>>> cell.value = 'X'

    @property
    def is_empty(self):
        return self._value is None

    def mark(self, player: Player):
        self._value = player.sign


class Board:
    """This class represents the board

    A board is composed of 9 cells.
    """

    def __init__(self):
        self._config = [
            [Cell(0, col_index) for col_index in range(3)],  # (0, 0), (0, 1), (0, 2)
            [Cell(1, col_index) for col_index in range(3)],  # (1, 0), (1, 1), (1, 2)
            [Cell(2, col_index) for col_index in range(3)],  # (2, 0), (2, 1), (2, 2)
        ]

    @property
    def cells(self):
        return self._config

    @staticmethod
    def mark(player: Player, cell: Cell):
        if not cell.is_empty:
            raise ValueError('Cell is not empty!')

        cell.mark(player)

    def get_empty_cells(self) -> list[Cell]:
        empty_cells = [
            [cell for cell in row if cell.is_empty]
            for row in self._config
        ]  # this is a matrix

        return list(itertools.chain.from_iterable(empty_cells))

    def show(self):
        print('+---+---+---+')
        for row in self._config:
            for cell_index, cell in enumerate(row):
                end_char = '' if cell_index < len(row) - 1 else '|\n'
                cell_value = cell.position if cell.value is None else cell.value
                print(f'| {cell_value} ', end=end_char)

            print('+---+---+---+')
