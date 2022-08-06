import pymongo
from predictor.individual_tests import head_to_head


def get_score(winner_name, entity_name, weight_score):
    if winner_name == entity_name:
        return 1 * weight_score
    else:
        return 0


client = pymongo.MongoClient("mongodb://localhost:27017/")
cs_matches_db = client["cs_matches"]
matches_doc = cs_matches_db["matches"]

metadata_db = client["metadata"]
current_weights_doc = metadata_db["current_weights"]

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

not_predicted = matches_doc.find({"prediction": None})

for match in not_predicted:
    team_score = 0
    opponent_score = 0
    team_name = match["team"]["name"]
    opponent_name = match["opponent"]["name"]

    # head to head
    head_to_head_winner = head_to_head.calculate_winner(match)
    team_score += get_score(head_to_head_winner, team_name, head_to_head.get_weight(current_weights))
    opponent_score += get_score(head_to_head_winner, opponent_name, head_to_head.get_weight(current_weights))

    if team_score >= opponent_score:
        winner = team_name
    else:
        winner = opponent_name

    matches_doc.update_one({"_id": match["_id"]}, {"$set": {"prediction": winner, "weights_id": current_weights["_id"]}})
