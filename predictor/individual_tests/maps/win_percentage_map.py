from predictor.individual_tests.maps.map import Map


class WinPercentageMap(Map):
    def __init__(self, weight_name):
        super().__init__(weight_name)

    def calculate_winner(self, match):
        return self.calculate_winner_win_percentage(match)

    def get_base_score(self, current_team):
        return self.get_base_score_win_percentage(current_team)
