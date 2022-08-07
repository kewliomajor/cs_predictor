import pymongo
from predictor.individual_tests import head_to_head, rank_difference
from model import mongo_client


def get_score(test, entity_name):
    test_winner = test.calculate_winner(match)
    test_score = test.get_base_score(match)
    test_weight = test.get_weight(current_weights)

    if test_winner == entity_name:
        return test_score * test_weight
    else:
        return 0


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

not_predicted = matches_doc.find({"prediction": None})

head_to_head = head_to_head.HeadToHead()
rank_difference = rank_difference.RankDifference()

for match in not_predicted:
    team_score = 0
    opponent_score = 0
    team_name = match["team"]["name"]
    opponent_name = match["opponent"]["name"]

    # head to head
    team_score += get_score(head_to_head, team_name)
    opponent_score += get_score(head_to_head, opponent_name)

    # rank difference
    team_score += get_score(rank_difference, team_name)
    opponent_score += get_score(rank_difference, opponent_name)

    if team_score >= opponent_score:
        winner = team_name
    else:
        winner = opponent_name

    matches_doc.update_one({"_id": match["_id"]}, {"$set": {"prediction": winner, "weights_id": current_weights["_id"]}})
