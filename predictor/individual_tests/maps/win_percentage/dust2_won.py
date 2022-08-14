from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class Dust2Won(WinPercentageMap):

    def __init__(self):
        super().__init__("dust2_won_weight")
        self.map_name = "Dust2"
