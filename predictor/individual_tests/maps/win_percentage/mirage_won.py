from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class MirageWon(WinPercentageMap):

    def __init__(self):
        super().__init__("mirage_won_weight")
        self.map_name = "Mirage"
