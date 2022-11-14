from brain_games.game_logic import right_or_wrong
from random import randint


def even_game():
    x = randint(0, 1000)

    def is_even(x):
        return (x % 2 == 0)

    if is_even(x):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (x, right_answer)

