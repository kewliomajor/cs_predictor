from predictor.individual_tests.base_test import BaseTest


class AveragePlayer(BaseTest):

    def __init__(self):
        super().__init__("average_player_weight")

    @staticmethod
    def calculate_winner(match):
        team_average = sum(match["team"]["player_ratings"]) / len(match["team"]["player_ratings"])
        opponent_average = sum(match["opponent"]["player_ratings"]) / len(match["opponent"]["player_ratings"])
        if team_average <= opponent_average:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    @staticmethod
    def get_base_score(current_team):
        trimmed_list = []
        for rating in current_team["player_ratings"]:
            if rating > 0:
                trimmed_list.append(rating)
        if len(trimmed_list) == 0:
            return 0
        return sum(trimmed_list) / len(trimmed_list)
