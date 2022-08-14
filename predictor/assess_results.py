import pymongo
from predictor.individual_tests import head_to_head, rank_difference
from predictor.individual_tests.maps.num_played import ancient_played, dust2_played, inferno_played, mirage_played, nuke_played, overpass_played, vertigo_played
from predictor.individual_tests.maps.win_percentage import ancient_won, dust2_won, inferno_won, mirage_won, nuke_won, overpass_won, vertigo_won
from predictor.individual_tests.recent_history import maps_lost, maps_won, match_win_percentage, matches_won, matches_lost
import json
from model import weights_class
from model import mongo_client


debug = False
print_only = True


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def add_test(test_list, current_test, current_weights_object):
    test_list.append({"test": current_test, "calculated_weight": current_test.get_weight(current_weights_object)})
    return test_list


def get_changed_weight(total_score):
    if total_score >= 64000:
        change = 6
    elif total_score >= 32000:
        change = 5
    elif total_score >= 16000:
        change = 4
    elif total_score >= 4000:
        change = 3
    elif total_score >= 1000:
        change = 2
    elif total_score >= 0:
        change = 1
    else:
        change = 0

    return change


def get_new_score(current_match, calculated_weight, current_winner, current_test):
    test_winner = current_test.calculate_winner(current_match)
    test_score = current_test.get_base_score(match)
    test_weight = current_test.get_weight(current_weights)

    if test_winner == current_winner:
        if test_weight is None:
            total_score = 0
        else:
            total_score = test_score * test_weight
    else:
        total_score = 0

    if calculated_weight is None:
        return 100
    if current_match["prediction_correct"] is True:
        if current_winner == current_match["prediction"]:
            if debug:
                print("adding " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight += get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
        else:
            if debug:
                print("subtracting " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight -= get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
    else:
        if current_winner == current_match["prediction"]:
            if debug:
                print("subtracting " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight -= get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
        else:
            if debug:
                print("adding " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight += get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
    return calculated_weight


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

query = {"result_assessed": False, "weights_id": current_weights["_id"]}
count = matches_doc.count_documents(query)
no_assessment = matches_doc.find(query)

if count == 0:
    print("No unassessed matches for current weights entry: " + str(current_weights["_id"]))
    exit()

tests_and_weights = []

head_to_head = head_to_head.HeadToHead()
tests_and_weights = add_test(tests_and_weights, head_to_head, current_weights)

rank_difference = rank_difference.RankDifference()
tests_and_weights = add_test(tests_and_weights, rank_difference, current_weights)

# maps
ancient_played = ancient_played.AncientPlayed()
tests_and_weights = add_test(tests_and_weights, ancient_played, current_weights)
dust2_played = dust2_played.Dust2Played()
tests_and_weights = add_test(tests_and_weights, dust2_played, current_weights)
inferno_played = inferno_played.InfernoPlayed()
tests_and_weights = add_test(tests_and_weights, inferno_played, current_weights)
mirage_played = mirage_played.MiragePlayed()
tests_and_weights = add_test(tests_and_weights, mirage_played, current_weights)
nuke_played = nuke_played.NukePlayed()
tests_and_weights = add_test(tests_and_weights, nuke_played, current_weights)
overpass_played = overpass_played.OverpassPlayed()
tests_and_weights = add_test(tests_and_weights, overpass_played, current_weights)
vertigo_played = vertigo_played.VertigoPlayed()
tests_and_weights = add_test(tests_and_weights, vertigo_played, current_weights)

ancient_won = ancient_won.AncientWon()
tests_and_weights = add_test(tests_and_weights, ancient_won, current_weights)
dust2_won = dust2_won.Dust2Won()
tests_and_weights = add_test(tests_and_weights, dust2_won, current_weights)
inferno_won = inferno_won.InfernoWon()
tests_and_weights = add_test(tests_and_weights, inferno_won, current_weights)
mirage_won = mirage_won.MirageWon()
tests_and_weights = add_test(tests_and_weights, mirage_won, current_weights)
nuke_won = nuke_won.NukeWon()
tests_and_weights = add_test(tests_and_weights, nuke_won, current_weights)
overpass_won = overpass_won.OverpassWon()
tests_and_weights = add_test(tests_and_weights, overpass_won, current_weights)
vertigo_won = vertigo_won.VertigoWon()
tests_and_weights = add_test(tests_and_weights, vertigo_won, current_weights)

# history
maps_won = maps_won.MapsWon()
tests_and_weights = add_test(tests_and_weights, maps_won, current_weights)
maps_lost = maps_lost.MapsLost()
tests_and_weights = add_test(tests_and_weights, maps_lost, current_weights)
match_win_percentage = match_win_percentage.MatchesWinPercentage()
tests_and_weights = add_test(tests_and_weights, match_win_percentage, current_weights)
matches_won = matches_won.MatchesWon()
tests_and_weights = add_test(tests_and_weights, matches_won, current_weights)
matches_lost = matches_lost.MatchesLost()
tests_and_weights = add_test(tests_and_weights, matches_lost, current_weights)

for match in no_assessment:
    for test_and_weight in tests_and_weights:
        test = test_and_weight["test"]
        old_weight = test_and_weight["calculated_weight"]
        winner = test.calculate_winner(match)
        new_weight = get_new_score(match, old_weight, winner, test)
        test_and_weight["calculated_weight"] = new_weight

    if not print_only:
        matches_doc.update_one({"_id": match["_id"]}, {"$set": {"result_assessed": True}})

new_weights = weights_class.Weights()
for test_and_weight in tests_and_weights:
    new_weights.set_weight(test_and_weight["test"], test_and_weight["calculated_weight"])

print(to_dict(new_weights))

if not print_only:
    current_weights_doc.insert_one(to_dict(new_weights))
