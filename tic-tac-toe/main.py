from game import Menu, Game

if __name__ == '__main__':
    number_of_games = Menu.get_number_of_games()
    player_1, player_2 = Menu.get_players()

    if number_of_games > 0:
        game = Game(player_1, player_2, number_of_games)
        game.play()

        if game.winner is None:
            print('\n\nGAME ENDED IN A DRAW!')
        else:
            print(f'\n\nTHE WINNER OF THE GAME IS: {game.winner}.')

    print('Thank you for playing this game. Good bye!')
