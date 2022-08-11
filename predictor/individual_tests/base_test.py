
class BaseTest:

    def __init__(self, weight_name):
        self.weight_name = weight_name

    def get_map(self, team_name, map_name, match):
        if match["team"]["name"] == team_name:
            maps = match["team"]["maps"]
        else:
            maps = match["opponent"]["maps"]

        for map_entity in maps:
            if map_entity["name"] == map_name:
                return map_entity

        raise Exception("Map " + map_name + " is not a recognized map in match " + str(match["_id"]))

    def get_weight(self, current_weights):
        if self.weight_name in current_weights:
            return current_weights[self.weight_name]
        else:
            return None
