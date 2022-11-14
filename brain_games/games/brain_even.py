from random import randint


def is_even(x):
    return (x % 2 == 0)


def even_game():
    x = randint(0, 1000)
    if is_even(x):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return x, right_answer
