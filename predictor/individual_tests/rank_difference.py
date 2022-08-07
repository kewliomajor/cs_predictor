from predictor.individual_tests.base_test import BaseTest


class RankDifference(BaseTest):

    def __init__(self):
        super().__init__("rank_difference_weight")

    @staticmethod
    def get_base_score(match):
        return match["team"]["ranking"] - match["opponent"]["ranking"]
