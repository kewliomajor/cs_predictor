from predictor.individual_tests.history import History


class MatchesWinPercentage(History):

    def __init__(self):
        super().__init__("matches_win_percentage_weight")

    def calculate_winner(self, match):
        super().populate_stats(match)
        if self.team_win_percentage >= self.opponent_win_percentage:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_base_score(self, match):
        super().populate_stats(match)
        return abs(self.team_win_percentage - self.opponent_win_percentage)
