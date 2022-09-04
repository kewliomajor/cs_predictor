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

    def calculate_winner_rounds_lost_in_wins(self, match):
        return self.generic_calculate_winner(match, "rounds_lost_in_wins")

    def calculate_winner_rounds_won_in_losses(self, match):
        return self.generic_calculate_winner(match, "rounds_won_in_losses")

    def generic_calculate_winner(self, match, field):
        team_name = match["team"]["name"]
        opponent_name = match["opponent"]["name"]
        try:
            team_map = super().get_map(match["team"], self.map_name)
            opponent_map = super().get_map(match["opponent"], self.map_name)
            if field == "rounds_lost_in_wins":
                check = team_map[field] < opponent_map[field]
            else:
                check = team_map[field] >= opponent_map[field]

            if check:
                return team_name
            else:
                return opponent_name
        except UnrecognizedMapException:
            # doesn't matter who wins because we will give them 0 score
            return team_name

    def get_base_score_maps_played(self, current_team):
        return self.generic_get_base_score(current_team, "times_played")

    def get_base_score_win_percentage(self, current_team):
        return self.generic_get_base_score(current_team, "win_percentage")

    def get_base_score_rounds_lost_in_wins(self, current_team):
        return self.generic_get_base_score(current_team, "rounds_lost_in_wins")

    def get_base_score_rounds_won_in_losses(self, current_team):
        return self.generic_get_base_score(current_team, "rounds_won_in_losses")

    def generic_get_base_score(self, current_team, field):
        try:
            team_map = super().get_map(current_team, self.map_name)
            if field == "rounds_lost_in_wins":
                return abs(14 - team_map[field])
            return team_map[field]

        except UnrecognizedMapException:
            # shouldn't count if the map isn't there
            return 0
