from brain_games.game_logic import right_or_wrong
from brain_games.games.brain_progression import progression_game


def main():
    QUEST = 'What number is missing in the progression?'
    right_or_wrong(QUEST, progression_game)


if __name__ == '__main__':
    main()
