from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


class Dust2RoundsWonInLosses(RoundsWonInLossesMap):

    def __init__(self):
        super().__init__("dust2_rwil_weight")
        self.map_name = "Dust2"
