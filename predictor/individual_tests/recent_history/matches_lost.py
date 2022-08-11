from predictor.individual_tests.history import History


class MatchesLost(History):

    def __init__(self):
        super().__init__("matches_lost_weight")

    def calculate_winner(self, match):
        super().populate_stats(match)
        if self.team_matches_lost < self.opponent_matches_lost:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_base_score(self, match):
        super().populate_stats(match)
        return abs(self.team_matches_lost - self.opponent_matches_lost)
