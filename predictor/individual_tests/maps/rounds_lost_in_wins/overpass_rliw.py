from predictor.individual_tests.maps.rounds_lost_in_wins_map import RoundsLostInWinsMap


class OverpassRoundsLostInWins(RoundsLostInWinsMap):

    def __init__(self):
        super().__init__("overpass_rliw_weight")
        self.map_name = "Overpass"
