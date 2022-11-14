from random import randint

def choose_operation(x, y):
    doing = randint(0, 2)
    if doing == 0:
        result = x + y
        expression = f'{x} + {y}'
    elif doing == 1:
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
