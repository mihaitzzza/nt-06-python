from sqlalchemy.orm.attributes import flag_modified
from random import randrange
from flask import Blueprint, request
from auth import token_required
from database.models import Game
from database import db

game_urls = Blueprint('game', __name__)


def check_winner(board):
    first_row = {board[0][0], board[0][1], board[0][2]}
    first_row_empty_space = '' in first_row
    if len(first_row) == 1 and not first_row_empty_space:
        return True, 1, 'You' if 'X' in first_row else 'CPU'

    second_row = {board[1][0], board[1][1], board[1][2]}
    second_row_empty_space = '' in second_row
    if len(second_row) == 1 and not second_row_empty_space:
        return True, 2, 'You' if 'X' in first_row else 'CPU'

    third_row = {board[2][0], board[2][1], board[2][2]}
    third_row_empty_space = '' in third_row
    if len(third_row) == 1 and not third_row_empty_space:
        return True, 3, 'You' if 'X' in third_row else 'CPU'

    left_col = {board[0][0], board[1][0], board[2][0]}
    left_col_empty_space = '' in left_col
    if len(left_col) == 1 and not left_col_empty_space:
        return True, 4, 'You' if 'X' in left_col else 'CPU'

    middle_col = {board[0][1], board[1][1], board[2][1]}
    middle_col_empty_space = '' in middle_col
    if len(middle_col) == 1 and not middle_col_empty_space:
        return True, 5, 'You' if 'X' in middle_col else 'CPU'

    right_col = {board[0][2], board[1][2], board[2][2]}
    right_col_empty_space = '' in right_col
    if len(right_col) == 1 and not right_col_empty_space:
        return True, 6, 'You' if 'X' in right_col else 'CPU'

    primary_diag = {board[0][0], board[1][1], board[2][2]}
    primary_diag_empty_space = '' in primary_diag
    if len(primary_diag) == 1 and not primary_diag_empty_space:
        return True, 7, 'You' if 'X' in primary_diag else 'CPU'

    secondary_diag = {board[0][2], board[1][1], board[2][0]}
    secondary_diag_empty_space = '' in secondary_diag
    if len(secondary_diag) == 1 and not secondary_diag_empty_space:
        return True, 8, 'You' if 'X' in secondary_diag else 'CPU'

    is_game_ready = (
        not first_row_empty_space and
        not second_row_empty_space and
        not third_row_empty_space and
        not left_col_empty_space and
        not middle_col_empty_space and
        not right_col_empty_space and
        not primary_diag_empty_space and
        not secondary_diag_empty_space
    )
    return is_game_ready, 0, None


@game_urls.route("/stats/")
@token_required
def get_stats(current_user):
    game = Game.query.filter(Game.user_id == current_user.id).first()

    if game:
        is_done, win_type, _ = check_winner(game.moves)

        if is_done or win_type:
            db.session.delete(game)
            db.session.commit()

            game = None

    return {
        "wins": current_user.wins,
        "draws": current_user.draws,
        "loses": current_user.loses,
        "game": bool(game),
    }


@game_urls.route("/play/", methods=("POST",))
@token_required
def start_game(current_user):
    game = Game.query.filter(Game.user_id == current_user.id).first()

    if not game:
        game = Game(user=current_user)
        db.session.add(game)
        db.session.commit()

    is_done, win_type, winner = check_winner(game.moves)

    return {
        "board": game.moves,
        "winType": win_type,
        "winner": winner,
        "isDone": is_done,
    }


@game_urls.route("/move/", methods=("POST",))
@token_required
def set_move(current_user):
    game = Game.query.filter(Game.user == current_user).first()

    if not game:
        raise Exception("Game is not available.")

    data = request.get_json()
    row = data["row"]
    col = data["col"]

    if game.moves[row][col] != "":
        raise Exception("Move is not available")

    game.moves[row][col] = "X"
    cpu_move = None
    _, win_type, winner = check_winner(game.moves)

    if win_type:
        current_user.wins += 1
    else:
        available_moves = []
        for row_index, row in enumerate(game.moves):
            for col_index, cell in enumerate(row):
                if cell == "":
                    available_moves.append({
                        "row": row_index,
                        "col": col_index,
                    })

        if len(available_moves) > 0:
            cpu_move_index = randrange(0, len(available_moves))
            cpu_move = available_moves[cpu_move_index]

            game.moves[cpu_move["row"]][cpu_move["col"]] = "O"

            _, win_type, winner = check_winner(game.moves)

            if win_type:
                current_user.loses += 1
        else:
            current_user.draws += 1

    flag_modified(game, "moves")
    db.session.add(game)
    db.session.commit()

    return {
        "cpu": cpu_move,
        "winType": win_type,
        "winner": winner,
    }
