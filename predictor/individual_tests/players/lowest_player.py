from predictor.individual_tests.base_test import BaseTest


class LowestPlayer(BaseTest):

    def __init__(self):
        super().__init__("lowest_player_weight")

    @staticmethod
    def calculate_winner(match):
        team_max = min(match["team"]["player_ratings"])
        opponent_max = min(match["opponent"]["player_ratings"])
        if team_max <= opponent_max:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    @staticmethod
    def get_base_score(current_team):
        return min(current_team["player_ratings"])
