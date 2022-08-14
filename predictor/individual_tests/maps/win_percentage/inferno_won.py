from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class InfernoWon(WinPercentageMap):

    def __init__(self):
        super().__init__("inferno_won_weight")
        self.map_name = "Inferno"
