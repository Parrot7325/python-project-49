#!/usr/bin/env python3
from brain_games.cli import welcome_user


def brain_games():
    print('Welcome to the Brain Games!')


def main():
    brain_games()
    right_or_wrong('What is the result of expression? ', gen_right)

if __name__ == '__main__':
    main()
welcome_user()
