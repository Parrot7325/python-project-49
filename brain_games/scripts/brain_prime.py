from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import right_or_wrong
from random import randint


def gen_quest():
    x = randint(0, 100)
    not_prime = 0
    for d in range(2, x):
        if x % d == 0:
            not_prime += 1
    if not_prime > 0:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    return(x, right_answer)


def main():
    right_or_wrong('Answer "yes" if given number is prime. Otherwise answer "no".', gen_quest)


if __name__ == '__main__':
    main()
