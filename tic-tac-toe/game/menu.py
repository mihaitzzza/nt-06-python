from game.players import Player
from utils.constants import MAIN_MENU_OPTIONS, GAME_TYPE


class Menu:
    """This class represents all the menus within the game"""
    @staticmethod
    def greet_player(player):
        print(f'Hey, {player.name}, welcome and good luck!')


    @staticmethod
    def get_number_of_games():
        while True:
            print('Choose a game type:')
            for choice_value, choice_text in MAIN_MENU_OPTIONS.items():
                print(f'{choice_value}. {choice_text}')

            choice = input('> ')

            try:
                choice = int(choice)

                if choice not in MAIN_MENU_OPTIONS.keys():
                    raise ValueError()
            except ValueError:
                print('Not a valid option!')
            else:
                break

        return GAME_TYPE[choice]

    @staticmethod
    def get_players():
        player_1 = Player()
        Menu.greet_player(player_1)

        player_2 = Player()
        Menu.greet_player(player_2)

        while True:
            print('Who will be the first player?')
            print(f'1. {player_1.name}')
            print(f'2. {player_2.name}')
            choice = input('> ')

            if choice not in ['1', '2']:
                print('Option not available.')
            else:
                break

        if choice == '1':
            print(f'{player_1} will start the game!')
            player_1.sign = 'X'
            player_2.sign = 'O'

            return player_1, player_2

        print(f'{player_2} will start the game!')
        player_1.sign = 'O'
        player_2.sign = 'X'

        return player_2, player_1
