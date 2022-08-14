from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class OverpassWon(WinPercentageMap):

    def __init__(self):
        super().__init__("overpass_won_weight")
        self.map_name = "Overpass"
