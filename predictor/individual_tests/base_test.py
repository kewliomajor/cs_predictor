from model.unrecognized_map import UnrecognizedMapException
from model.iterative_weights_class import IterativeWeights


class BaseTest:

    def __init__(self, weight_name):
        self.weight_name = weight_name

    def get_map(self, current_team, map_name):
        maps = current_team["maps"]

        for map_entity in maps:
            if map_entity["name"] == map_name:
                return map_entity

        string = "Map " + map_name + " is not a recognized map in match involving team " + current_team["name"]
        # print(string)
        raise UnrecognizedMapException(string)

    def get_weight(self, current_weights):
        if isinstance(current_weights, IterativeWeights):
            return getattr(current_weights, self.weight_name)
        if self.weight_name in current_weights:
            return current_weights[self.weight_name]
        else:
            return None

    def get_weight_name(self):
        return self.weight_name
