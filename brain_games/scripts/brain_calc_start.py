from brain_games.game_logic import start_game
from brain_games.games.brain_calc import calc_game


def main():
    start_game('What is the result of the expression?', calc_game)


if __name__ == '__main__':
    main()
