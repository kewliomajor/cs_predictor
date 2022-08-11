from predictor.individual_tests.history import History


class MapsWon(History):

    def __init__(self):
        super().__init__("maps_won_weight")

    def calculate_winner(self, match):
        super().populate_stats(match)
        if self.team_maps_won > self.opponent_maps_won:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_base_score(self, match):
        super().populate_stats(match)
        return abs(self.team_maps_won - self.opponent_maps_won)
