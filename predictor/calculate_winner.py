import pymongo
from model import mongo_client, all_tests

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

all_tests = all_tests.AllTests()
test_array = all_tests.get_all_tests()

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
