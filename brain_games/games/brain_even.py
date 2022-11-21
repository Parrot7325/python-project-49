from random import randint


def is_even(number):
    return number % 2 == 0


def even_game():
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    random_number = randint(0, 1000)
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return random_number, right_answer
