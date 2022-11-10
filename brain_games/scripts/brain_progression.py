from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import right_or_wrong
from random import randint


def gen_quest():
    progression = []
    length = randint(7, 13)
    x = randint(0, 10)
    step = randint(2, 10)
    while length > 0:
        progression.append(x)
        x += step
        length -= 1

    delete = randint(0, length)
    right_answer = progression[delete]
    progression[delete] = '..'
    quest = ''
    for x in progression:
        quest += str(x)
        quest += ' '
    return(quest, str(right_answer))


def main():
    right_or_wrong('What number is missing in the progression?', gen_quest)


if __name__ == '__main__':
    main()
