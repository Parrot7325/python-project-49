from random import randint


def gen_progression():
    progression = []
    length = randint(7, 13)
    random_number = randint(0, 10)
    step = randint(2, 10)
    while length > 0:
        progression.append(random_number)
        random_number += step
        length -= 1
    return progression


def progression_game():
    progression = gen_progression()
    delete = randint(0, len(progression) - 1)
    right_answer = progression[delete]
    progression[delete] = '..'
    quest = ''
    for number in progression:
        quest += str(number)
        quest += ' '
    return quest, str(right_answer)
