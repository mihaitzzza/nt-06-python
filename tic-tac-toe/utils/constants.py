SINGLE_GAME_OPTION = 1
BEST_OUT_OF_3 = 2
BEST_OUT_OF_5 = 3
EXIT = 0

MAIN_MENU_OPTIONS = {
    SINGLE_GAME_OPTION: 'Play a single game',
    BEST_OUT_OF_3: 'Play 2 out of 3 games',
    BEST_OUT_OF_5: 'Play 3 out of 5 games',
    EXIT: 'Quit game',
}

GAME_TYPE = {
    SINGLE_GAME_OPTION: 1,
    BEST_OUT_OF_3: 3,
    BEST_OUT_OF_5: 5,
    EXIT: 0,
}

WINNING_SOLUTIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]
