from model import weights_class
import json
from json import JSONEncoder
from model import mongo_client
from predictor.individual_tests import head_to_head, rank_difference
from predictor.individual_tests.maps.num_played import ancient_played, dust2_played, inferno_played, mirage_played, nuke_played, overpass_played, vertigo_played
from predictor.individual_tests.maps.win_percentage import ancient_won, dust2_won, inferno_won, mirage_won, nuke_won, overpass_won, vertigo_won
from predictor.individual_tests.recent_history import maps_lost, maps_won, match_win_percentage, matches_won, matches_lost


class CsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


client = mongo_client.MongoClient()
current_weights_doc = client.get_weights_document()

test_array = []

test_array.append(head_to_head.HeadToHead())
test_array.append(rank_difference.RankDifference())

test_array.append(ancient_played.AncientPlayed())
test_array.append(dust2_played.Dust2Played())
test_array.append(inferno_played.InfernoPlayed())
test_array.append(mirage_played.MiragePlayed())
test_array.append(nuke_played.NukePlayed())
test_array.append(overpass_played.OverpassPlayed())
test_array.append(vertigo_played.VertigoPlayed())

test_array.append(ancient_won.AncientWon())
test_array.append(dust2_won.Dust2Won())
test_array.append(inferno_won.InfernoWon())
test_array.append(mirage_won.MirageWon())
test_array.append(nuke_won.NukeWon())
test_array.append(overpass_won.OverpassWon())
test_array.append(vertigo_won.VertigoWon())

test_array.append(maps_lost.MapsLost())
test_array.append(maps_won.MapsWon())
test_array.append(match_win_percentage.MatchesWinPercentage())
test_array.append(matches_won.MatchesWon())
test_array.append(matches_lost.MatchesLost())

current_weights = weights_class.Weights()
for test in test_array:
    current_weights.set_weight(test, 1)

current_weights_doc.insert_one(to_dict(current_weights))
