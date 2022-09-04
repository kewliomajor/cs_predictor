from predictor.individual_tests.history import History


class MatchesWon(History):

    def __init__(self):
        super().__init__("matches_won_weight")

    def calculate_winner(self, match):
        super().populate_stats(match)
        if self.team_matches_won > self.opponent_matches_won:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_base_score(self, current_team, team=False):
        if team:
            return self.team_matches_won
        else:
            return self.opponent_matches_won
