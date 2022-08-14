from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class VertigoPlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("vertigo_played_weight")
        self.map_name = "Vertigo"
