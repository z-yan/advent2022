def calculate_score(strategy):
    player_score = 0

    for opponent_shape, player_shape in strategy:
        # Add score for choice
        player_score += shape_to_score[player_shape]

        # Add score vs opponent
        # draw
        if player_shape == opponent_shape:
            player_score += 3
        # wins
        elif (
            (player_shape == "R" and opponent_shape == "S")
            or (player_shape == "P" and opponent_shape == "R")
            or (player_shape == "S" and opponent_shape == "P")
        ):
            player_score += 6

    return player_score


def round_to_player_choice(opponent_shape, outcome):
    # Rock: opp = P and outcome = lose, opp = R and outcome = draw, opp = S and outcome = win
    if (
        (opponent_shape == "P" and outcome == "X")
        or (opponent_shape == "R" and outcome == "Y")
        or (opponent_shape == "S" and outcome == "Z")
    ):
        return "R"
    # Paper: opp = S and outcome = lose, opp = P and outcome = draw, opp = R and outcome = win
    elif (
        (opponent_shape == "S" and outcome == "X")
        or (opponent_shape == "P" and outcome == "Y")
        or (opponent_shape == "R" and outcome == "Z")
    ):
        return "P"
    else:
        return "S"


if __name__ == "__main__":
    opponent_to_shape = {"A": "R", "B": "P", "C": "S"}
    player_to_shape = {"X": "R", "Y": "P", "Z": "S"}
    shape_to_score = {"R": 1, "P": 2, "S": 3}

    with open("input.txt") as f:
        strategy = [line.split() for line in f.read().splitlines()]

    # Part one
    strategy_decoded = [
        (opponent_to_shape[opponent], player_to_shape[player])
        for opponent, player in strategy
    ]
    player_score = calculate_score(strategy_decoded)

    print(f"Part one, total player score: {player_score}")

    # Part two
    strategy_decoded = [
        (
            opponent_to_shape[opponent],
            round_to_player_choice(opponent_to_shape[opponent], outcome),
        )
        for opponent, outcome in strategy
    ]
    player_score = calculate_score(strategy_decoded)

    print(f"Part two, total player score: {player_score}")
