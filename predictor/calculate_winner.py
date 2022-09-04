import pymongo
from model import mongo_client, all_tests
from predictor.individual_tests.head_to_head import HeadToHead
from predictor.individual_tests.history import History

print_only = False


def get_score(current_test, entity_name, current_match, current_weights):
    team = False
    if entity_name == current_match["team"]["name"]:
        current_team = current_match["team"]
        team = True
    elif entity_name == current_match["opponent"]["name"]:
        current_team = current_match["opponent"]
    else:
        raise Exception("Team " + entity_name + " is not in match " + current_match["_id"])

    if isinstance(current_test, HeadToHead):
        test_score = current_test.get_base_score(current_match, team)
    elif isinstance(current_test, History):
        current_test.populate_stats(current_match)
        test_score = current_test.get_base_score(current_team, team)
    else:
        test_score = current_test.get_base_score(current_team)
    test_weight = current_test.get_weight(current_weights)

    if test_weight is None:
        return 0

    return test_score * test_weight


def calculate_winner(current_match, test_list, current_weights, print_winner=False):
    team_score = 0
    opponent_score = 0
    team_name = current_match["team"]["name"]
    opponent_name = current_match["opponent"]["name"]

    for test in test_list:
        team_score += get_score(test, team_name, current_match, current_weights)
        opponent_score += get_score(test, opponent_name, current_match, current_weights)

    if team_score >= opponent_score:
        current_winner = team_name
    else:
        current_winner = opponent_name

    if print_winner:
        print("Predicting " + current_winner + " to win in match of " + team_name + " (" + str(
            team_score) + ") vs " + opponent_name + " (" + str(opponent_score) + ")")
    return current_winner


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

not_predicted = matches_doc.find({"prediction": None})

all_tests = all_tests.AllTests()
test_array = all_tests.get_all_tests()

for match in not_predicted:
    winner = calculate_winner(match, test_array, weights, True)

    if not print_only:
        matches_doc.update_one({"_id": match["_id"]}, {"$set": {"prediction": winner, "weights_id": weights["_id"]}})
