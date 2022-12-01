#!/usr/bin/env python3
from random import randint


def is_even(number):
    return number % 2 == 0


QUESTION = (
    'Answer "yes" if the number is even, '
    'otherwise answer "no".')


def even_game():
    random_number = randint(0, 1000)
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return QUESTION, random_number, right_answer
