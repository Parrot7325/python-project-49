from random import randint, choice


OPERATORS = ('+', '-', '*')


def make_result(first_number, second_number, doing):
    if doing == '+':
        result = first_number + second_number
    elif doing == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return result


QUESTION = 'What is the result of the expression?'


def calc_game():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    operator = choice(OPERATORS)
    result = make_result(first_random_number, second_random_number, operator)
    expression = f'{first_random_number} {operator} {second_random_number}'
    return QUESTION, expression, str(result)
