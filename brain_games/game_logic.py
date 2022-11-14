import sys
import prompt


def play_3_rounds(quest_global, gen_right):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{quest_global}')
    won_games = 0
    while won_games < 3:
        rights = gen_right()
        right_answer = rights[1]
        answer = input(f'Question: {rights[0]}\nYour answer: ')
        if answer == right_answer:
            won_games += 1
            print('Correct!')
        else:
            print(f'''
'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
Let's try again, {name}!''')
            sys.exit()
    print(f'Congratulations, {name}!')
