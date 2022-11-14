from brain_games.game_logic import right_or_wrong
from random import randint


def prime_game():
    x = randint(1, 100)
    not_prime = 0
    for d in range(2, x):
        if x % d == 0:
            not_prime += 1
    if not_prime > 0:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    if x == 1:
        right_answer = 'no'
    return (x, right_answer)

