from predictor.individual_tests.base_test import BaseTest


class Map(BaseTest):

    def __init__(self, weight_name):
        super().__init__(weight_name)
        self.map_name = None

    def calculate_winner(self, match):
        team_name = match["team"]["name"]
        opponent_name = match["opponent"]["name"]
        team_map = super().get_map(team_name, self.map_name, match)
        opponent_map = super().get_map(opponent_name, self.map_name, match)
        if team_map["win_percentage"] >= opponent_map["win_percentage"]:
            return team_name
        else:
            return opponent_name

    def get_base_score(self, match):
        team_name = match["team"]["name"]
        opponent_name = match["opponent"]["name"]
        team_map = super().get_map(team_name, self.map_name, match)
        opponent_map = super().get_map(opponent_name, self.map_name, match)
        team_value = team_map["times_played"] * team_map["win_percentage"]
        opponent_value = opponent_map["times_played"] * opponent_map["win_percentage"]

        score = abs(team_value - opponent_value)
        return score
