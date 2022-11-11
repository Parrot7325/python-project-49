from brain_games.scripts.game_logic import right_or_wrong
from random import randint


def gen_quest():
    x = randint(0, 20)
    y = randint(0, 20)
    quest = str(x) + ' ' + str(y)

    minimum = min(x, y)
    gcd = 1
    for delimiter in range(1, minimum + 1):
        if x % delimiter == 0 and y % delimiter == 0:
            gcd = delimiter
        if x == 0 or y == 0:
            gcd = max(x, y)
    return (quest, str(gcd))


def main():
    print('Congratulations, Tirion!')
    QUEST = 'Find the greatest common divisor of given numbers.'
    right_or_wrong(QUEST, gen_quest)


if __name__ == '__main__':
    main()
