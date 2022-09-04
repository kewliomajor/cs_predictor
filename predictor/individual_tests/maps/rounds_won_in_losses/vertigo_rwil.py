from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


class VertigoRoundsWonInLosses(RoundsWonInLossesMap):

    def __init__(self):
        super().__init__("vertigo_rwil_weight")
        self.map_name = "Vertigo"
