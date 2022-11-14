from brain_games.game_logic import play_3_rounds
from brain_games.games.brain_even import even_game


def main():
    QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_3_rounds(QUEST, even_game)


if __name__ == '__main__':
    main()
