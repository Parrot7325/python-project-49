#!/usr/bin/env python3
from brain_games.game_logic import game
from brain_games.games import brain_calc


def main():
    game(brain_calc.calc_game)


if __name__ == '__main__':
    main()
