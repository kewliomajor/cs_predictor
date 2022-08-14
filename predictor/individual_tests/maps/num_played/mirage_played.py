from predictor.individual_tests.maps.num_played_map import NumPlayedMap


class MiragePlayed(NumPlayedMap):

    def __init__(self):
        super().__init__("mirage_played_weight")
        self.map_name = "Mirage"
