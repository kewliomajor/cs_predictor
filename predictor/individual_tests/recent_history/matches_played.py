from predictor.individual_tests.history import History


class MatchesPlayed(History):

    def __init__(self):
        super().__init__("matches_played_weight")

    def calculate_winner(self, match):
        super().populate_stats(match)
        if self.team_matches_played >= self.opponent_matches_played:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_base_score(self, current_team, team=False):
        if team:
            return self.team_matches_played
        else:
            return self.opponent_matches_played
