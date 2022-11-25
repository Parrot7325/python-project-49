#!/usr/bin/env python3
from brain_games.game_logic import start_game
from brain_games.games.brain_gcd import gcd_game


def main():
    start_game(gcd_game)


if __name__ == '__main__':
    main()
