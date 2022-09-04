from predictor.individual_tests.history import History


class MapsPlayed(History):

    def __init__(self):
        super().__init__("maps_played_weight")

    def calculate_winner(self, match):
        super().populate_stats(match)
        if self.team_maps_played >= self.team_maps_played:
            return match["team"]["name"]
        else:
            return match["opponent"]["name"]

    def get_base_score(self, current_team, team=False):
        if team:
            return self.team_maps_played
        else:
            return self.opponent_maps_played
