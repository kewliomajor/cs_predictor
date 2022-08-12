import pymongo
from predictor.individual_tests import head_to_head, rank_difference
from predictor.individual_tests.maps import ancient, dust2, inferno, mirage, nuke, overpass, vertigo
from predictor.individual_tests.recent_history import maps_lost, maps_won, match_win_percentage, matches_won, matches_lost
import json
from model import weights_class
from model import mongo_client


debug = False


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


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


def get_new_score(current_match, calculated_weight, winner, test):
    test_winner = test.calculate_winner(current_match)
    test_score = test.get_base_score(match)
    test_weight = test.get_weight(current_weights)

    if test_winner == winner:
        if test_weight is None:
            total_score = 0
        else:
            total_score = test_score * test_weight
    else:
        total_score = 0

    if calculated_weight is None:
        return 100
    if current_match["prediction_correct"] is True:
        if winner == current_match["prediction"]:
            if debug:
                print("adding " + test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight += get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
        else:
            if debug:
                print("subtracting " + test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight -= get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
    else:
        if winner == current_match["prediction"]:
            if debug:
                print("subtracting " + test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight -= get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
        else:
            if debug:
                print("adding " + test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
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

head_to_head = head_to_head.HeadToHead()
calculated_head_to_head_weight = head_to_head.get_weight(current_weights)

rank_difference = rank_difference.RankDifference()
calculated_rank_difference_weight = rank_difference.get_weight(current_weights)

# maps
ancient = ancient.Ancient()
calculated_ancient_weight = ancient.get_weight(current_weights)
dust2 = dust2.Dust2()
calculated_dust2_weight = dust2.get_weight(current_weights)
inferno = inferno.Inferno()
calculated_inferno_weight = inferno.get_weight(current_weights)
mirage = mirage.Mirage()
calculated_mirage_weight = mirage.get_weight(current_weights)
nuke = nuke.Nuke()
calculated_nuke_weight = nuke.get_weight(current_weights)
overpass = overpass.Overpass()
calculated_overpass_weight = overpass.get_weight(current_weights)
vertigo = vertigo.Vertigo()
calculated_vertigo_weight = vertigo.get_weight(current_weights)

# history
maps_won = maps_won.MapsWon()
calculated_maps_won_weight = maps_won.get_weight(current_weights)
maps_lost = maps_lost.MapsLost()
calculated_maps_lost_weight = maps_lost.get_weight(current_weights)
match_win_percentage = match_win_percentage.MatchesWinPercentage()
calculated_match_win_percentage_weight = match_win_percentage.get_weight(current_weights)
matches_won = matches_won.MatchesWon()
calculated_matches_won_weight = matches_won.get_weight(current_weights)
matches_lost = matches_lost.MatchesLost()
calculated_matches_lost_weight = matches_lost.get_weight(current_weights)

for match in no_assessment:
    head_to_head_winner = head_to_head.calculate_winner(match)
    calculated_head_to_head_weight = get_new_score(match, calculated_head_to_head_weight, head_to_head_winner, head_to_head)

    rank_difference_winner = rank_difference.calculate_winner(match)
    calculated_rank_difference_weight = get_new_score(match, calculated_rank_difference_weight, rank_difference_winner, rank_difference)

    # maps
    ancient_winner = ancient.calculate_winner(match)
    calculated_ancient_weight = get_new_score(match, calculated_ancient_weight, ancient_winner, ancient)

    dust2_winner = dust2.calculate_winner(match)
    calculated_dust2_weight = get_new_score(match, calculated_dust2_weight, dust2_winner, dust2)

    inferno_winner = inferno.calculate_winner(match)
    calculated_inferno_weight = get_new_score(match, calculated_inferno_weight, inferno_winner, inferno)

    mirage_winner = mirage.calculate_winner(match)
    calculated_mirage_weight = get_new_score(match, calculated_mirage_weight, mirage_winner, mirage)

    nuke_winner = nuke.calculate_winner(match)
    calculated_nuke_weight = get_new_score(match, calculated_nuke_weight, nuke_winner, nuke)

    overpass_winner = overpass.calculate_winner(match)
    calculated_overpass_weight = get_new_score(match, calculated_overpass_weight, overpass_winner, overpass)

    vertigo_winner = vertigo.calculate_winner(match)
    calculated_vertigo_weight = get_new_score(match, calculated_vertigo_weight, vertigo_winner, vertigo)

    # history
    maps_won_winner = maps_won.calculate_winner(match)
    calculated_maps_won_weight = get_new_score(match, calculated_maps_won_weight, maps_won_winner, maps_won)

    maps_lost_winner = maps_lost.calculate_winner(match)
    calculated_maps_lost_weight = get_new_score(match, calculated_maps_lost_weight, maps_lost_winner, maps_lost)

    match_win_percentage_winner = match_win_percentage.calculate_winner(match)
    calculated_match_win_percentage_weight = get_new_score(match, calculated_match_win_percentage_weight, match_win_percentage_winner, match_win_percentage)

    matches_won_winner = matches_won.calculate_winner(match)
    calculated_matches_won_weight = get_new_score(match, calculated_matches_won_weight, matches_won_winner, matches_won)

    matches_lost_winner = matches_lost.calculate_winner(match)
    calculated_matches_lost_weight = get_new_score(match, calculated_matches_lost_weight, matches_lost_winner, matches_lost)

    matches_doc.update_one({"_id": match["_id"]}, {"$set": {"result_assessed": True}})


new_weights = weights_class.Weights()
new_weights.set_head_to_head_weight(calculated_head_to_head_weight)
new_weights.set_rank_difference_weight(calculated_rank_difference_weight)
new_weights.set_ancient_weight(calculated_ancient_weight)
new_weights.set_dust2_weight(calculated_dust2_weight)
new_weights.set_inferno_weight(calculated_inferno_weight)
new_weights.set_mirage_weight(calculated_mirage_weight)
new_weights.set_nuke_weight(calculated_nuke_weight)
new_weights.set_overpass_weight(calculated_overpass_weight)
new_weights.set_vertigo_weight(calculated_vertigo_weight)
new_weights.set_maps_won_weight(calculated_maps_won_weight)
new_weights.set_maps_lost_weight(calculated_maps_lost_weight)
new_weights.set_match_win_percentage_weight(calculated_match_win_percentage_weight)
new_weights.set_matches_won_weight(calculated_matches_won_weight)
new_weights.set_matches_lost_weight(calculated_matches_lost_weight)
print(to_dict(new_weights))
current_weights_doc.insert_one(to_dict(new_weights))
