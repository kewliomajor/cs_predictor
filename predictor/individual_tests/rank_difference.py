from predictor.individual_tests.base_test import BaseTest


class RankDifference(BaseTest):

    def __init__(self):
        super().__init__("rank_difference_weight")

    @staticmethod
    def calculate_winner(match):
        if match["team"]["ranking"] <= match["opponent"]["ranking"]:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    @staticmethod
    def get_base_score(match, team=False):
        team_ranking = match["team"]["ranking"]
        opponent_ranking = match["opponent"]["ranking"]
        if team:
            return team_ranking - opponent_ranking
        else:
            return opponent_ranking - team_ranking
