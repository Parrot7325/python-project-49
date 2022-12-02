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


QUESTION = 'What number is missing in the progression?'


def play():
    progression = gen_progression()
    random_index = randint(0, len(progression) - 1)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    quest = ''
    for number in progression:
        quest += str(number)
        quest += ' '
    return quest, str(right_answer)
