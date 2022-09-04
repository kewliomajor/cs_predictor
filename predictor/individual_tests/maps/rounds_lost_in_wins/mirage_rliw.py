from predictor.individual_tests.maps.rounds_lost_in_wins_map import RoundsLostInWinsMap


class MirageRoundsLostInWins(RoundsLostInWinsMap):

    def __init__(self):
        super().__init__("mirage_rliw_weight")
        self.map_name = "Mirage"
