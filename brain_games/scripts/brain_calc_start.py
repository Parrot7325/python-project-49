from brain_games.game_logic import right_or_wrong
from brain_games.games.brain_calc import calc_game


def main():
    right_or_wrong('What is the result of the expression?', calc_game)


if __name__ == '__main__':
    main()
