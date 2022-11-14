from brain_games.game_logic import right_or_wrong
from brain_games.games.brain_even import even_game


def main():
    QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'
    right_or_wrong(QUEST, even_game)


if __name__ == '__main__':
    main()
