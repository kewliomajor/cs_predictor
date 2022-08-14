from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class AncientWon(WinPercentageMap):

    def __init__(self):
        super().__init__("ancient_won_weight")
        self.map_name = "Ancient"
