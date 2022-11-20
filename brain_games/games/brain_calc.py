from random import randint, choice


def make_result(first_number, second_number, doing):
    if doing == '+':
        result = first_number + second_number
    elif doing == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return result


def make_question(first_number, second_number, doing):
    return f'{first_number} {doing} {second_number}'


def choose_operation(first_number, second_number):
    doing = choice('+' '-' '*')
    result = make_result(first_number, second_number, doing)
    expression = make_question(first_number, second_number, doing)
    return expression, str(result)


def calc_game():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    return choose_operation(first_random_number, second_random_number)
