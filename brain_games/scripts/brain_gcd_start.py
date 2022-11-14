from brain_games.game_logic import play_3_rounds
from brain_games.games.brain_gcd import gcd_game


def main():
    QUEST = 'Find the greatest common divisor of given numbers.'
    play_3_rounds(QUEST, gcd_game)


if __name__ == '__main__':
    main()
