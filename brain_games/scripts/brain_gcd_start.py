from brain_games.game_logic import start_game
from brain_games.games.brain_gcd import gcd_game


def main():
    QUEST = 'Find the greatest common divisor of given numbers.'
    start_game(QUEST, gcd_game)


if __name__ == '__main__':
    main()
