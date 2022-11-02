from random import randint
import prompt
import sys

name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
print(f'Hello, {name}!\nWhat is the result of the expression?')
won_games = 0
while won_games < 3:
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
    answer = int(input(f'Question: {expression}\nYour answer: '))
    if answer == result:
        print('Correct!')
        won_games += 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
        sys.exit()
sys.exit()
