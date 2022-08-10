from predictor.individual_tests.map import Map


class Overpass(Map):

    def __init__(self):
        super().__init__("overpass_weight")
        self.map_name = "Overpass"
