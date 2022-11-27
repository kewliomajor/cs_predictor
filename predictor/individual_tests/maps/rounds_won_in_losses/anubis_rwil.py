from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


class AnubisRoundsWonInLosses(RoundsWonInLossesMap):

    def __init__(self):
        super().__init__("anubis_rwil_weight")
        self.map_name = "Anubis"
