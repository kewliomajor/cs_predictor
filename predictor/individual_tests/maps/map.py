from predictor.individual_tests.base_test import BaseTest
from model.unrecognized_map import UnrecognizedMapException


class Map(BaseTest):

    def __init__(self, weight_name):
        super().__init__(weight_name)
        self.map_name = None

    def calculate_winner_maps_played(self, match):
        return self.generic_calculate_winner(match, "times_played")

    def calculate_winner_win_percentage(self, match):
        return self.generic_calculate_winner(match, "win_percentage")

    def generic_calculate_winner(self, match, field):
        team_name = match["team"]["name"]
        opponent_name = match["opponent"]["name"]
        try:
            team_map = super().get_map(team_name, self.map_name, match)
            opponent_map = super().get_map(opponent_name, self.map_name, match)
            if team_map[field] >= opponent_map[field]:
                return team_name
            else:
                return opponent_name
        except UnrecognizedMapException:
            # doesn't matter who wins because we will give them 0 score
            return team_name

    def get_base_score_maps_played(self, match):
        return self.generic_get_base_score(match, "times_played")

    def get_base_score_win_percentage(self, match):
        return self.generic_get_base_score(match, "win_percentage")

    def generic_get_base_score(self, match, field):
        team_name = match["team"]["name"]
        opponent_name = match["opponent"]["name"]
        try:
            team_map = super().get_map(team_name, self.map_name, match)
            opponent_map = super().get_map(opponent_name, self.map_name, match)
            team_value = team_map[field]
            opponent_value = opponent_map[field]

            score = abs(team_value - opponent_value)
            return score

        except UnrecognizedMapException:
            # shouldn't count if the map isn't there
            return 0
