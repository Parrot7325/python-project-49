import sys
import prompt


def game(start_game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!')
    won_games = 0
    print(start_game.QUESTION)
    while won_games < 3:
        question, correct_answer = start_game.play()
        answer = input(f'Question: {question}\nYour answer: ')
        if answer == correct_answer:
            won_games += 1
            print('Correct!')
        else:
            print(f'''
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            sys.exit()
    print(f'Congratulations, {name}!')
