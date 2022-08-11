from predictor.individual_tests.base_test import BaseTest


class HeadToHead(BaseTest):

    def __init__(self):
        super().__init__("head_to_head_weight")

    @staticmethod
    def calculate_winner(match):
        if match["team_wins"] >= match["opponent_wins"]:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    @staticmethod
    def get_base_score(match):
        value = abs(match["team_wins"] - match["opponent_wins"])
        if value == 0:
            return 1
        return value
