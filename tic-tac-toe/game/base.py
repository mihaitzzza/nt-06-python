from game.round import Round


class Game:
    """The represents the whole game functionality."""

    def __init__(self, player_1, player_2, number_of_games):
        """
        Init a Tic-Tac-Toe game.

        :param player_1: This is the first player object.
        :param player_2: This is the second player object.
        :param number_of_games: This is the total number of games to be played.
        """

        self._player_1 = player_1
        self._player_2 = player_2
        self._max_rounds = number_of_games
        self._current_round = 0
        self._rounds = [
            Round(player_1, player_2, index)
            for index in range(number_of_games)
        ]
        self._max_wins = number_of_games // 2 + 1
        self._winner = None

    @property
    def winner(self):
        return self._winner

    def play(self):
        for round_ in self._rounds:
            round_.play()

            if round_.winner.wins == self._max_wins:
                self._winner = round_.winner
                break
