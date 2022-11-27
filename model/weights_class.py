from datetime import datetime


class Weights:

    def __init__(self):
        self.current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.head_to_head_weight = 0.0
        self.rank_difference_weight = 0.0
        self.average_player_weight = 0.0
        self.highest_player_weight = 0.0
        self.lowest_player_weight = 0.0

        self.ancient_played_weight = 0.0
        self.anubis_played_weight = 0.0
        self.dust2_played_weight = 0.0
        self.inferno_played_weight = 0.0
        self.mirage_played_weight = 0.0
        self.nuke_played_weight = 0.0
        self.overpass_played_weight = 0.0
        self.vertigo_played_weight = 0.0

        self.ancient_won_weight = 0.0
        self.anubis_won_weight = 0.0
        self.dust2_won_weight = 0.0
        self.inferno_won_weight = 0.0
        self.mirage_won_weight = 0.0
        self.nuke_won_weight = 0.0
        self.overpass_won_weight = 0.0
        self.vertigo_won_weight = 0.0

        self.ancient_rliw_weight = 0.0
        self.anubis_rliw_weight = 0.0
        self.dust2_rliw_weight = 0.0
        self.inferno_rliw_weight = 0.0
        self.mirage_rliw_weight = 0.0
        self.nuke_rliw_weight = 0.0
        self.overpass_rliw_weight = 0.0
        self.vertigo_rliw_weight = 0.0

        self.ancient_rwil_weight = 0.0
        self.anubis_rwil_weight = 0.0
        self.dust2_rwil_weight = 0.0
        self.inferno_rwil_weight = 0.0
        self.mirage_rwil_weight = 0.0
        self.nuke_rwil_weight = 0.0
        self.overpass_rwil_weight = 0.0
        self.vertigo_rwil_weight = 0.0

        self.maps_won_weight = 0.0
        self.maps_played_weight = 0.0
        self.matches_win_percentage_weight = 0.0
        self.matches_won_weight = 0.0
        self.matches_played_weight = 0.0

    def set_weight(self, test, weight):
        weight_name = test.get_weight_name()
        setattr(self, weight_name, self.get_limited_weight(weight))

    def set_weight_by_name(self, name, weight):
        setattr(self, name, self.get_limited_weight(weight))

    @staticmethod
    def get_limited_weight(weight):
        if weight > 100:
            return 100
        if weight < 1:
            return 1
        return weight
