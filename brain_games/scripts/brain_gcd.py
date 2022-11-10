from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import right_or_wrong
from random import randint


def gen_quest():
    x = randint(0, 20)
    y = randint(0, 20)
    quest = str(x) + ' ' + str(y)

    minimum = min(x, y)
    for d in range (1, minimum + 1):
        if x % d == 0 and y % d == 0:
            gcd = d
    return(quest, str(gcd))


def main():
    right_or_wrong('Find the greatest common divisor of given numbers.', gen_quest)


if __name__ == '__main__':
    main()
