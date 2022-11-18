from random import randint, choice


def choose_operation(x, y):
    doing = choice('+', '-', '*')
    if doing == '+':
        result = x + y
        expression = f'{x} + {y}'
    elif doing == '-':
        result = x - y
        expression = f'{x} - {y}'
    else:
        result = x * y
        expression = f'{x} * {y}'
    return (expression, str(result))


def calc_game():
    x = randint(0, 100)
    y = randint(0, 100)
    return (choose_operation(x, y))
