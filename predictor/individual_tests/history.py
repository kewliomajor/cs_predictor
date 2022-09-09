from abc import abstractmethod

from predictor.individual_tests.base_test import BaseTest


class History(BaseTest):

    def __init__(self, weight_name):
        super().__init__(weight_name)
        self.team_maps_won = 0
        self.opponent_maps_won = 0
        self.team_maps_played = 0
        self.opponent_maps_played = 0
        self.team_matches_won = 0
        self.opponent_matches_won = 0
        self.team_matches_played = 0
        self.opponent_matches_played = 0
        self.team_win_percentage = 0
        self.opponent_win_percentage = 0
        self.previous_match = None

    def clear_stats(self):
        self.team_maps_won = 0
        self.opponent_maps_won = 0
        self.team_maps_played = 0
        self.opponent_maps_played = 0
        self.team_matches_won = 0
        self.opponent_matches_won = 0
        self.team_matches_played = 0
        self.opponent_matches_played = 0
        self.team_win_percentage = 0
        self.opponent_win_percentage = 0

    def populate_stats(self, match):
        if self.previous_match is not None:
            if self.previous_match["_id"] == match["_id"]:
                return

        self.clear_stats()

        for past_match in match["team"]["match_history"]:
            if past_match["max_maps"] == 1:
                self.team_maps_played += 1
                self.team_matches_played += 1
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.team_maps_won += 1
                    self.team_matches_won += 1
            elif past_match["max_maps"] == 3 or past_match["max_maps"] == 5:
                self.team_maps_played += past_match["opponent_score"] + past_match["team_score"]
                self.team_matches_played += 1
                self.team_maps_won += past_match["team_score"]
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.team_matches_won += 1
            else:
                raise Exception("Unknown number of max maps for match " + str(match["_id"]))

        for past_match in match["opponent"]["match_history"]:
            if past_match["max_maps"] == 1:
                self.opponent_maps_played += 1
                self.opponent_matches_played += 1
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.opponent_maps_won += 1
                    self.opponent_matches_won += 1
            elif past_match["max_maps"] == 3 or past_match["max_maps"] == 5:
                self.opponent_maps_played += past_match["opponent_score"] + past_match["team_score"]
                self.opponent_matches_played += 1
                self.opponent_maps_won += past_match["team_score"]
                if past_match["team_score"] > past_match["opponent_score"]:
                    self.opponent_matches_won += 1
            else:
                raise Exception("Unknown number of max maps for match " + str(match["_id"]))

        if self.team_matches_played == 0:
            self.team_win_percentage = 0
        else:
            self.team_win_percentage = (self.team_matches_won / self.team_matches_played) * 100

        if self.opponent_matches_played == 0:
            self.opponent_win_percentage = 0
        else:
            self.opponent_win_percentage = (self.opponent_matches_won / self.opponent_matches_played) * 100
        self.previous_match = match

    @abstractmethod
    def get_base_score(self, current_team, team=False):
        pass
