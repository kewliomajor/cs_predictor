from datetime import datetime


class Weights:

    def __init__(self):
        self.current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.head_to_head_weight = 0.0
        self.rank_difference_weight = 0.0
        self.ancient_weight = 0.0
        self.dust2_weight = 0.0
        self.inferno_weight = 0.0
        self.mirage_weight = 0.0
        self.nuke_weight = 0.0
        self.overpass_weight = 0.0
        self.vertigo_weight = 0.0
        self.maps_won = 0.0
        self.maps_lost = 0.0
        self.match_win_percentage = 0.0
        self.matches_won = 0.0
        self.matches_lost = 0.0

    def set_head_to_head_weight(self, weight):
        self.head_to_head_weight = self.get_limited_weight(weight)

    def set_rank_difference_weight(self, weight):
        self.rank_difference_weight = self.get_limited_weight(weight)

    def set_ancient_weight(self, weight):
        self.ancient_weight = self.get_limited_weight(weight)

    def set_dust2_weight(self, weight):
        self.dust2_weight = self.get_limited_weight(weight)

    def set_inferno_weight(self, weight):
        self.inferno_weight = self.get_limited_weight(weight)

    def set_mirage_weight(self, weight):
        self.mirage_weight = self.get_limited_weight(weight)

    def set_nuke_weight(self, weight):
        self.nuke_weight = self.get_limited_weight(weight)

    def set_overpass_weight(self, weight):
        self.overpass_weight = self.get_limited_weight(weight)

    def set_vertigo_weight(self, weight):
        self.vertigo_weight = self.get_limited_weight(weight)

    def set_maps_won_weight(self, weight):
        self.maps_won = self.get_limited_weight(weight)

    def set_maps_lost_weight(self, weight):
        self.maps_lost = self.get_limited_weight(weight)

    def set_match_win_percentage_weight(self, weight):
        self.match_win_percentage = self.get_limited_weight(weight)

    def set_matches_won_weight(self, weight):
        self.matches_won = self.get_limited_weight(weight)

    def set_matches_lost_weight(self, weight):
        self.matches_lost = self.get_limited_weight(weight)

    @staticmethod
    def get_limited_weight(weight):
        if weight > 100:
            return 100
        if weight < 1:
            return 1
        return weight
