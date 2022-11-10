import prompt
from random import randint
import sys

name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
print(f'Hello, {name}!')
won_games = 0
while won_games < 3:
    x = randint(0, 10000000000000000000000000000000)
    if x % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    print(f'''
Answer "yes" if the number is even, otherwise answer "no".
Question: {x}''')
    answer = input('Your answer: ')
    if answer == right_answer:
        print('Correct!')
        won_games += 1
    else:
        print(f'''
"{answer}" is wrong answer ;(. Correct answer was '{right_answer}'.
Lets's try again, {name}''')
        won_games = 0
print(f'Congratulations, {name}!')
sys.exit()
