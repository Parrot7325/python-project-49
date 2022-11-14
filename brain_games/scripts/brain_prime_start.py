from brain_games.game_logic import play_3_rounds
from brain_games.games.brain_prime import prime_game


def main():
    QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_3_rounds(QUEST, prime_game)


if __name__ == '__main__':
    main()
