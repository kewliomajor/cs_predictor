from predictor.individual_tests.base_test import BaseTest


class Rank(BaseTest):

    def __init__(self):
        super().__init__("rank_difference_weight")

    @staticmethod
    def calculate_winner(match):
        if match["team"]["ranking"] <= match["opponent"]["ranking"]:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    @staticmethod
    def get_base_score(current_team):
        return 999 - current_team["ranking"]
