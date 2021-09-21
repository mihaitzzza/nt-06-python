class Player:
    """This class is representing a player.

    A player participating in this game has 2 attributes:
    - the player has a name
    - the player has a sign for playing with (X or O)
    """

    def __init__(self):
        print("What's your name?")
        self._name = input('> ')
        self._sign = None
        self._wins = 0

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, sign):
        self._sign = sign

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins):
        self._wins = wins

    def __str__(self):
        return self._name

    def __repr__(self):
        return self.__str__()
