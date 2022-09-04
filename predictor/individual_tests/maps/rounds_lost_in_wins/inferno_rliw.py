from predictor.individual_tests.maps.rounds_lost_in_wins_map import RoundsLostInWinsMap


class InfernoRoundsLostInWins(RoundsLostInWinsMap):

    def __init__(self):
        super().__init__("inferno_rliw_weight")
        self.map_name = "Inferno"
