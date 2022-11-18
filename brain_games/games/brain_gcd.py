from random import randint


def find_gcd(x, y):
    minimum = min(x, y)
    gcd = 1
    for delimiter in range(1, minimum + 1):
        if x % delimiter == 0 and y % delimiter == 0:
            gcd = delimiter
    if x == 0 or y == 0:
        gcd = max(x, y)
    return str(gcd)


def gcd_game():
    x = randint(0, 20)
    y = randint(0, 20)
    quest = str(x) + ' ' + str(y)
    gcd = find_gcd(x, y)
    return quest, gcd
