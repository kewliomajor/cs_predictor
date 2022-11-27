from predictor.individual_tests.maps.rounds_lost_in_wins_map import RoundsLostInWinsMap


class AnubisRoundsLostInWins(RoundsLostInWinsMap):

    def __init__(self):
        super().__init__("anubis_rliw_weight")
        self.map_name = "Anubis"
