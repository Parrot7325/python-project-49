from brain_games.scripts.game_logic import right_or_wrong
from random import randint


def gen_quest():
    x = randint(0, 1000)

    def is_even(x):
        return (x % 2 == 0)

    if is_even(x):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (x, right_answer)


def main():
    QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'
    right_or_wrong(QUEST, gen_quest)


if __name__ == '__main__':
    main()
