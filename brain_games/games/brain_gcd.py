from random import randint


def gcd_game():
    x = randint(0, 20)
    y = randint(0, 20)
    quest = str(x) + ' ' + str(y)

    minimum = min(x, y)
    gcd = 1
    for delimiter in range(1, minimum + 1):
        if x % delimiter == 0 and y % delimiter == 0:
            gcd = delimiter
    if x == 0 or y == 0:
        gcd = max(x, y)
    return (quest, str(gcd))

