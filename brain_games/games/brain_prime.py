from random import randint


def is_prime(x):
    not_prime = 0
    if x == 1:
        return False
    for d in range(2, x):
        if x % d == 0:
            not_prime += 1
    return not_prime == 0


def prime_game():
    x = randint(1, 100)
    if is_prime(x):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (x, right_answer)
