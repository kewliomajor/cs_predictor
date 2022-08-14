from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class Dust2Played(NumPlayedMap):

    def __init__(self):
        super().__init__("dust2_played_weight")
        self.map_name = "Dust2"
