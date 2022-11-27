from predictor.individual_tests import head_to_head, rank
from predictor.individual_tests.maps.num_played import ancient_played, anubis_played, dust2_played, inferno_played, mirage_played, nuke_played, overpass_played, vertigo_played
from predictor.individual_tests.maps.win_percentage import ancient_won, anubis_won, dust2_won, inferno_won, mirage_won, nuke_won, overpass_won, vertigo_won
from predictor.individual_tests.maps.rounds_won_in_losses import ancient_rwil, anubis_rwil, dust2_rwil, inferno_rwil, mirage_rwil, nuke_rwil, overpass_rwil, vertigo_rwil
from predictor.individual_tests.maps.rounds_lost_in_wins import ancient_rliw, anubis_rliw, dust2_rliw, inferno_rliw, mirage_rliw, nuke_rliw, overpass_rliw, vertigo_rliw
from predictor.individual_tests.recent_history import maps_played, maps_won, match_win_percentage, matches_won, matches_played
from predictor.individual_tests.players import average_player, highest_player, lowest_player


class AllTests:

    def __init__(self):
        self.test_array = []
        self.tests_and_weights = []
        self.test_array.append(head_to_head.HeadToHead())
        self.test_array.append(rank.Rank())

        self.test_array.append(average_player.AveragePlayer())
        self.test_array.append(highest_player.HighestPlayer())
        self.test_array.append(lowest_player.LowestPlayer())

        self.test_array.append(ancient_played.AncientPlayed())
        self.test_array.append(anubis_played.AnubisPlayed())
        self.test_array.append(dust2_played.Dust2Played())
        self.test_array.append(inferno_played.InfernoPlayed())
        self.test_array.append(mirage_played.MiragePlayed())
        self.test_array.append(nuke_played.NukePlayed())
        self.test_array.append(overpass_played.OverpassPlayed())
        self.test_array.append(vertigo_played.VertigoPlayed())

        self.test_array.append(ancient_won.AncientWon())
        self.test_array.append(anubis_won.AnubisWon())
        self.test_array.append(dust2_won.Dust2Won())
        self.test_array.append(inferno_won.InfernoWon())
        self.test_array.append(mirage_won.MirageWon())
        self.test_array.append(nuke_won.NukeWon())
        self.test_array.append(overpass_won.OverpassWon())
        self.test_array.append(vertigo_won.VertigoWon())

        self.test_array.append(ancient_rwil.AncientRoundsWonInLosses())
        self.test_array.append(anubis_rwil.AnubisRoundsWonInLosses())
        self.test_array.append(dust2_rwil.Dust2RoundsWonInLosses())
        self.test_array.append(inferno_rwil.InfernoRoundsWonInLosses())
        self.test_array.append(mirage_rwil.MirageRoundsWonInLosses())
        self.test_array.append(nuke_rwil.NukeRoundsWonInLosses())
        self.test_array.append(overpass_rwil.OverpassRoundsWonInLosses())
        self.test_array.append(vertigo_rwil.VertigoRoundsWonInLosses())

        self.test_array.append(ancient_rliw.AncientRoundsLostInWins())
        self.test_array.append(anubis_rliw.AnubisRoundsLostInWins())
        self.test_array.append(dust2_rliw.Dust2RoundsLostInWins())
        self.test_array.append(inferno_rliw.InfernoRoundsLostInWins())
        self.test_array.append(mirage_rliw.MirageRoundsLostInWins())
        self.test_array.append(nuke_rliw.NukeRoundsLostInWins())
        self.test_array.append(overpass_rliw.OverpassRoundsLostInWins())
        self.test_array.append(vertigo_rliw.VertigoRoundsLostInWins())

        self.test_array.append(maps_played.MapsPlayed())
        self.test_array.append(maps_won.MapsWon())
        self.test_array.append(match_win_percentage.MatchesWinPercentage())
        self.test_array.append(matches_won.MatchesWon())
        self.test_array.append(matches_played.MatchesPlayed())

    def get_all_tests(self):
        return self.test_array

    def get_all_tests_and_weights(self, current_weights):
        if len(self.tests_and_weights) > 0:
            return self.tests_and_weights

        for test in self.test_array:
            self.tests_and_weights.append(
                {"test": test, "calculated_weight": test.get_weight(current_weights)})

        return self.tests_and_weights

