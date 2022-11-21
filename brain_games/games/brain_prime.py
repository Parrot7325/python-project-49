from random import randint


def is_prime(number):
    not_prime = 0
    if number == 1:
        return False
    for delimiter in range(2, number):
        if number % delimiter == 0:
            not_prime += 1
    return not_prime == 0


def prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    random_number = randint(1, 100)
    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return random_number, right_answer
