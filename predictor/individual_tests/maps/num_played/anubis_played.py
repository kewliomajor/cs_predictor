from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class AnubisPlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("anubis_played_weight")
        self.map_name = "Anubis"
