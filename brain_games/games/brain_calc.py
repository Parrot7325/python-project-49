#!/usr/bin/env python3
from random import randint, choice


DOINGS = ('+', '-', '*')


def make_result(first_number, second_number, doing):
    if doing == '+':
        result = first_number + second_number
    elif doing == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return result


def calc_game():
    print('What is the result of the expression?')
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    doing = choice(DOINGS)
    result = make_result(first_random_number, second_random_number, doing)
    expression = f'{first_random_number} {doing} {second_random_number}'
    return expression, str(result)
