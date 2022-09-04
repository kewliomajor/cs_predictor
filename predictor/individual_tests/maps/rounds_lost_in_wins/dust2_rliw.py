from predictor.individual_tests.maps.rounds_lost_in_wins_map import RoundsLostInWinsMap


class Dust2RoundsLostInWins(RoundsLostInWinsMap):

    def __init__(self):
        super().__init__("dust2_rliw_weight")
        self.map_name = "Dust2"
