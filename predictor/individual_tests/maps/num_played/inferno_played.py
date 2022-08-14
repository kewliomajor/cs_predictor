from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class InfernoPlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("inferno_played_weight")
        self.map_name = "Inferno"
