from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class OverpassPlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("overpass_played_weight")
        self.map_name = "Overpass"
