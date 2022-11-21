from random import randint


def find_gcd(first_number, second_number):
    minimum = min(first_number, second_number)
    gcd = 1
    for delimiter in range(1, minimum + 1):
        if first_number % delimiter == 0 and second_number % delimiter == 0:
            gcd = delimiter
    if first_number == 0 or second_number == 0:
        gcd = max(first_number, second_number)
    return str(gcd)


def gcd_game():
    print('Find the greatest common divisor of given numbers.')
    first_random_number = randint(0, 20)
    second_random_number = randint(0, 20)
    quest = str(first_random_number) + ' ' + str(second_random_number)
    gcd = find_gcd(first_random_number, second_random_number)
    return quest, gcd
