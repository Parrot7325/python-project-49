from random import randint


def is_even(number):
    return number % 2 == 0


<<<<<<< HEAD
QUESTION = ('Answer "yes" if the number is even, '
            'otherwise answer "no".')
<<<<<<< HEAD
=======
QUESTION = '''
Answer "yes" if the number is even, 'otherwise answer "no".'''
>>>>>>> parent of 34150f5 (Кортеж заменен на f-строки)
=======
>>>>>>> 63ab1c2be87df2d5bdc7b20a1274fb11a5ee141e


def even_game():
    random_number = randint(0, 1000)
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return QUESTION, random_number, right_answer
