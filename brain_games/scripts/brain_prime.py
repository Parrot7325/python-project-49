#!/usr/bin/env python3
from brain_games.game_logic import game
from brain_games.games import brain_prime


def main():
    game(brain_prime.prime_game)


if __name__ == '__main__':
    main()
