from predictor.individual_tests.base_test import BaseTest


class History(BaseTest):

    def __init__(self, weight_name):
        super().__init__(weight_name)
        self.team_maps_won = 0
        self.opponent_maps_won = 0
        self.team_maps_lost = 0
        self.opponent_maps_lost = 0
        self.team_matches_won = 0
        self.opponent_matches_won = 0
        self.team_matches_lost = 0
        self.opponent_matches_lost = 0
        self.team_win_percentage = 0
        self.opponent_win_percentage = 0
        self.previous_match = None

    def populate_stats(self, match):
        if self.previous_match["_id"] == match["_id"]:
            return

        for past_match in match["team"]["match_history"]:
            if past_match["max_maps"] == 1:
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.team_maps_won += 1
                    self.team_matches_won += 1
                else:
                    self.team_maps_lost += 1
                    self.team_matches_lost += 1
            elif past_match["max_maps"] == 3 or past_match["max_maps"] == 5:
                self.team_maps_lost += past_match["opponent_score"]
                self.team_maps_won += past_match["team_score"]
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.team_matches_won += 1
                else:
                    self.team_matches_lost += 1
            else:
                raise Exception("Unknown number of max maps for match " + str(match["_id"]))

        for past_match in match["opponent"]["match_history"]:
            if past_match["max_maps"] == 1:
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.opponent_maps_won += 1
                    self.opponent_matches_won += 1
                else:
                    self.opponent_maps_lost += 1
                    self.opponent_matches_lost += 1
            elif past_match["max_maps"] == 3 or past_match["max_maps"] == 5:
                self.opponent_maps_lost += past_match["opponent_score"]
                self.opponent_maps_won += past_match["team_score"]
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.opponent_matches_won += 1
                else:
                    self.opponent_matches_lost += 1
            else:
                raise Exception("Unknown number of max maps for match " + str(match["_id"]))

        self.team_win_percentage = (self.team_matches_won / (self.team_matches_lost + self.team_matches_won)) * 100
        self.opponent_win_percentage = (self.opponent_matches_won / (self.opponent_matches_lost + self.opponent_matches_won)) * 100
        self.previous_match = match