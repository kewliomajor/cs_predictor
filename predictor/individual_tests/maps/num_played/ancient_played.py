from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class AncientPlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("ancient_played_weight")
        self.map_name = "Ancient"
