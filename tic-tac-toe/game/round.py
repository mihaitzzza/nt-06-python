from game.board import Board
from game.players import Player
from utils.constants import WINNING_SOLUTIONS


class Round:
    """This represents a single game"""

    def __init__(self, player_1: Player, player_2: Player, number: int):
        """
        Init a single game round.
        :param player_1: First player
        :param player_2: Second player
        :param number: The current round index.
        """
        self._player_1 = player_1
        self._player_2 = player_2
        self._current_turn = 0
        self._number = number
        self._board = Board()
        self._winner = None

    @property
    def winner(self):
        return self._winner

    def _is_over(self, player):
        for win_solution in WINNING_SOLUTIONS:
            win_set = set()

            for x, y in win_solution:
                win_set.add(self._board.cells[x][y].value)

            if len(win_set) == 1 and player.sign in win_set:
                return True

        return False

    def play(self):
        while self._current_turn < 9:
            current_player = self._player_1 if self._current_turn % 2 == 0 else self._player_2

            print('\nThis is the current board.')
            self._board.show()
            empty_cells = self._board.get_empty_cells()
            empty_positions = [cell.position for cell in empty_cells]
            print(f'Pick one empty space. Your options: {empty_positions}')

            choice = input('> ')
            try:
                choice = int(choice)

                if choice not in empty_positions:
                    raise ValueError()
            except ValueError:
                print('Option not available.')
                continue

            marked_cell = [cell for cell in empty_cells if cell.position == choice][0]
            self._board.mark(current_player, marked_cell)

            if self._current_turn >= 4:
                # Check if someone won the game
                if self._is_over(current_player):
                    self._winner = current_player
                    break

            self._current_turn += 1

        if self._winner is None:
            print('\n\nRound ended in a draw!')
        else:
            self._winner.wins += 1
            print(f'\n\n{self._winner.name} won the game!!! Total wins: {self._winner.wins}')
