
class BaseTest:

    def __init__(self, weight_name):
        self.weight_name = weight_name

    @staticmethod
    def calculate_winner(match):
        if match["team_wins"] >= match["opponent_wins"]:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_weight(self, current_weights):
        if self.weight_name in current_weights:
            return current_weights[self.weight_name]
        else:
            return None
