from brain_games.game_logic import right_or_wrong
from brain.games.games.brain_prime import prime_game


def main():
    QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    right_or_wrong(QUEST, prime_game)


if __name__ == '__main__':
    main()
