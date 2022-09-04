from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


class MirageRoundsWonInLosses(RoundsWonInLossesMap):

    def __init__(self):
        super().__init__("mirage_rwil_weight")
        self.map_name = "Mirage"
