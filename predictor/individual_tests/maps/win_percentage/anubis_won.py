from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class AnubisWon(WinPercentageMap):

    def __init__(self):
        super().__init__("anubis_won_weight")
        self.map_name = "Anubis"
