from datetime import datetime


class Weights:

    def __init__(self):
        self.current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.head_to_head_weight = 0.0
        self.rank_difference_weight = 0.0

    def set_head_to_head_weight(self, weight):
        self.head_to_head_weight = self.get_limited_weight(weight)

    def set_rank_difference_weight(self, weight):
        self.rank_difference_weight = self.get_limited_weight(weight)

    @staticmethod
    def get_limited_weight(weight):
        if weight > 100:
            return 100
        if weight < 1:
            return 1
        return weight
