from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


class InfernoRoundsWonInLosses(RoundsWonInLossesMap):

    def __init__(self):
        super().__init__("inferno_rwil_weight")
        self.map_name = "Inferno"
