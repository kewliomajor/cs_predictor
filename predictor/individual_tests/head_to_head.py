
def calculate_winner(match):
    if match["team_wins"] >= match["opponent_wins"]:
        return match["team"]["name"]
    else:
        return match["opponent"]["name"]


def get_weight(current_weights):
    return current_weights["head_to_head_weight"]
