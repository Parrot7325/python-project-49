from brain_games.scripts.game_logic import right_or_wrong
from random import randint


def gen_right():
    x = randint(0, 100)
    y = randint(0, 100)
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


def main():
    #print('What is the result of the expression? ') Убрать
    right_or_wrong('What is the result of the expression?', gen_right)


if __name__ == '__main__':
    main()
