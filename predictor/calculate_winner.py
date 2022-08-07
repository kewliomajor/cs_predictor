import pymongo
from predictor.individual_tests import head_to_head, rank_difference
from model import mongo_client


def get_score(winner_name, entity_name, base_score, weight_score):
    if winner_name == entity_name:
        return base_score * weight_score
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
    head_to_head_winner = head_to_head.calculate_winner(match)
    head_to_head_base_score = head_to_head.get_base_score(match)
    head_to_head_weight = head_to_head.get_weight(current_weights)
    team_score += get_score(head_to_head_winner, team_name, head_to_head_base_score, head_to_head_weight)
    opponent_score += get_score(head_to_head_winner, opponent_name, head_to_head_base_score, head_to_head_weight)

    # rank difference
    rank_difference_winner = rank_difference.calculate_winner(match)
    rank_difference_score = rank_difference.get_base_score(match)
    rank_difference_weight = rank_difference.get_weight(current_weights)
    team_score += get_score(rank_difference_winner, team_name, rank_difference_score, rank_difference_weight)
    opponent_score += get_score(rank_difference_winner, opponent_name, rank_difference_score, rank_difference_weight)

    if team_score >= opponent_score:
        winner = team_name
    else:
        winner = opponent_name

    matches_doc.update_one({"_id": match["_id"]}, {"$set": {"prediction": winner, "weights_id": current_weights["_id"]}})
