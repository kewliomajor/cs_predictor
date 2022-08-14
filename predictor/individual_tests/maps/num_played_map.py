from predictor.individual_tests.maps.map import Map


class NumPlayedMap(Map):
    def __init__(self, weight_name):
        super().__init__(weight_name)

    def calculate_winner(self, match):
        return self.calculate_winner_maps_played(match)

    def get_base_score(self, match):
        return self.get_base_score_maps_played(match)
