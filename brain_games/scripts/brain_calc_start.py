from brain_games.game_logic import play_3_rounds
from brain_games.games.brain_calc import calc_game


def main():
    play_3_rounds('What is the result of the expression?', calc_game)


if __name__ == '__main__':
    main()
