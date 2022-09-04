from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


class NukeRoundsWonInLosses(RoundsWonInLossesMap):

    def __init__(self):
        super().__init__("nuke_rwil_weight")
        self.map_name = "Nuke"
