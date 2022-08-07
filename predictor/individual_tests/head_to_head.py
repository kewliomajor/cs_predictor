from predictor.individual_tests.base_test import BaseTest


class HeadToHead(BaseTest):

    def __init__(self):
        super().__init__("head_to_head_weight")

    @staticmethod
    def get_base_score(match):
        return 1
