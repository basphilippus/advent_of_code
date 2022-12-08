from typing import List


OPPONENT_MAP = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3   # Scissors
}

PLAYER_MAP = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3   # Scissors
}


def play_rock_paper_scissors(game_input: List[str]) -> int:
    total_score = 0
    for game in game_input:
        game_score = 0
        opponent_choice, player_choice = game.split(' ')

        opponent = OPPONENT_MAP[opponent_choice]
        player = PLAYER_MAP[player_choice]

        if opponent == player:
            # draw
            game_score += 3

        opponent_calculation = opponent + 1
        if opponent_calculation == 4:
            opponent_calculation = 1
        if opponent_calculation == player:
            # player wins
            game_score += 6
        else:
            # opponent wins
            game_score += 0

        game_score += player
        total_score += game_score

    return total_score


def get_correct_rock_paper_scissors_score(game_input: List[str]) -> int:
    total_score = 0
    for game in game_input:
        game_score = 0
        opponent_choice, desired_outcome = game.split(' ')

        opponent = OPPONENT_MAP[opponent_choice]
        player_choice = 0

        if desired_outcome == 'X':
            # Player needs to lose
            player_choice = opponent - 1
            if player_choice == 0:
                player_choice = 3
            game_score += 0

        if desired_outcome == 'Y':
            # The game needs to be a draw
            player_choice = opponent
            game_score += 3

        if desired_outcome == 'Z':
            # Player needs to win
            player_choice = opponent + 1
            if player_choice == 4:
                player_choice = 1
            game_score += 6

        game_score += player_choice
        total_score += game_score

    return total_score
