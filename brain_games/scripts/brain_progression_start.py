from brain_games.game_logic import play_3_rounds
from brain_games.games.brain_progression import progression_game


def main():
    QUEST = 'What number is missing in the progression?'
    play_3_rounds(QUEST, progression_game)


if __name__ == '__main__':
    main()
