import pymongo
from predictor.individual_tests import head_to_head, rank_difference
from predictor.individual_tests.maps.num_played import ancient_played, dust2_played, inferno_played, mirage_played, nuke_played, overpass_played, vertigo_played
from predictor.individual_tests.maps.win_percentage import ancient_won, dust2_won, inferno_won, mirage_won, nuke_won, overpass_won, vertigo_won
from predictor.individual_tests.recent_history import maps_lost, maps_won, match_win_percentage, matches_won, matches_lost
from model import mongo_client

print_only = False


def get_score(current_test, entity_name, current_match):
    test_winner = current_test.calculate_winner(current_match)
    test_score = current_test.get_base_score(current_match)
    test_weight = current_test.get_weight(current_weights)

    if test_weight is None:
        return 0

    if test_winner == entity_name:
        return test_score * test_weight
    else:
        return 0


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

not_predicted = matches_doc.find({"prediction": None})

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

for match in not_predicted:
    team_score = 0
    opponent_score = 0
    team_name = match["team"]["name"]
    opponent_name = match["opponent"]["name"]

    for test in test_array:
        team_score += get_score(test, team_name, match)
        opponent_score += get_score(test, opponent_name, match)

    if team_score >= opponent_score:
        winner = team_name
    else:
        winner = opponent_name

    print("Predicting " + winner + " to win in match of " + team_name + " (" + str(team_score) + ") vs " + opponent_name + " (" + str(opponent_score) + ")")
    if not print_only:
        matches_doc.update_one({"_id": match["_id"]}, {"$set": {"prediction": winner, "weights_id": current_weights["_id"]}})
