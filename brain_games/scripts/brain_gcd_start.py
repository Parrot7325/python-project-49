from brain_games.game_logic import right_or_wrong
from brain_games.games.brain_gcd import gcd_game


def main():
    QUEST = 'Find the greatest common divisor of given numbers.'
    right_or_wrong(QUEST, gcd_game)


if __name__ == '__main__':
    main()
