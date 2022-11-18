from brain_games.game_logic import start_game
from brain_games.games.brain_progression import progression_game


def main():
    QUEST = 'What number is missing in the progression?'
    start_game(QUEST, progression_game)


if __name__ == '__main__':
    main()
