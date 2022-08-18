from predictor.individual_tests import head_to_head, rank_difference
from predictor.individual_tests.maps.num_played import ancient_played, dust2_played, inferno_played, mirage_played, nuke_played, overpass_played, vertigo_played
from predictor.individual_tests.maps.win_percentage import ancient_won, dust2_won, inferno_won, mirage_won, nuke_won, overpass_won, vertigo_won
from predictor.individual_tests.recent_history import maps_lost, maps_won, match_win_percentage, matches_won, matches_lost


class AllTests:

    def __init__(self):
        self.test_array = []
        self.tests_and_weights = []
        self.test_array.append(head_to_head.HeadToHead())
        self.test_array.append(rank_difference.RankDifference())

        self.test_array.append(ancient_played.AncientPlayed())
        self.test_array.append(dust2_played.Dust2Played())
        self.test_array.append(inferno_played.InfernoPlayed())
        self.test_array.append(mirage_played.MiragePlayed())
        self.test_array.append(nuke_played.NukePlayed())
        self.test_array.append(overpass_played.OverpassPlayed())
        self.test_array.append(vertigo_played.VertigoPlayed())

        self.test_array.append(ancient_won.AncientWon())
        self.test_array.append(dust2_won.Dust2Won())
        self.test_array.append(inferno_won.InfernoWon())
        self.test_array.append(mirage_won.MirageWon())
        self.test_array.append(nuke_won.NukeWon())
        self.test_array.append(overpass_won.OverpassWon())
        self.test_array.append(vertigo_won.VertigoWon())

        self.test_array.append(maps_lost.MapsLost())
        self.test_array.append(maps_won.MapsWon())
        self.test_array.append(match_win_percentage.MatchesWinPercentage())
        self.test_array.append(matches_won.MatchesWon())
        self.test_array.append(matches_lost.MatchesLost())

    def get_all_tests(self):
        return self.test_array

    def get_all_tests_and_weights(self, current_weights):
        if len(self.tests_and_weights) > 0:
            return self.tests_and_weights

        for test in self.test_array:
            self.tests_and_weights.append(
                {"test": test, "calculated_weight": test.get_weight(current_weights)})

        return self.tests_and_weights

