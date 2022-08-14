from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class VertigoWon(WinPercentageMap):

    def __init__(self):
        super().__init__("vertigo_won_weight")
        self.map_name = "Vertigo"
