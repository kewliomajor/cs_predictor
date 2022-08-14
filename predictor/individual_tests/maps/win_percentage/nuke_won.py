from predictor.individual_tests.maps.win_percentage_map import WinPercentageMap


class NukeWon(WinPercentageMap):

    def __init__(self):
        super().__init__("nuke_won_weight")
        self.map_name = "Nuke"
