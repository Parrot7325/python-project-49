from random import randint


def gen_progression():
    progression = []
    length = randint(7, 13)
    x = randint(0, 10)
    step = randint(2, 10)
    while length > 0:
        progression.append(x)
        x += step
        length -= 1
    return progression


def progression_game():
    progression = gen_progression()
    delete = randint(0, len(progression))
    right_answer = progression[delete]
    progression[delete] = '..'
    quest = ''
    for x in progression:
        quest += str(x)
        quest += ' '
    return (quest, str(right_answer))
