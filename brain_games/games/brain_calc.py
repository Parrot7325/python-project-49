from random import randint, choice


def choose_operation(first_number, second_number):
    doing = choice('+' '-' '*')
    if doing == '+':
        result = first_number + second_number
        expression = f'{first_number} + {second_number}'
    elif doing == '-':
        result = first_number - second_number
        expression = f'{first_number} - {second_number}'
    else:
        result = first_number * second_number
        expression = f'{first_number} * {second_number}'
    return expression, str(result)


def calc_game():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    return choose_operation(first_random_number, second_random_number)
