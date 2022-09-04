from predictor.individual_tests.maps.map import Map


class RoundsWonInLossesMap(Map):
    def __init__(self, weight_name):
        super().__init__(weight_name)

    def calculate_winner(self, match):
        return self.calculate_winner_rounds_won_in_losses(match)

    def get_base_score(self, current_team):
        return self.get_base_score_rounds_won_in_losses(current_team)
