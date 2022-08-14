from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class NukePlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("nuke_played_weight")
        self.map_name = "Nuke"
