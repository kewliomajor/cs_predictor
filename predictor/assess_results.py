import pymongo
from predictor.individual_tests import head_to_head, rank_difference
import json
from model import weights_class
from model import mongo_client


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def get_new_score(current_match, calculated_weight):
    if calculated_weight is None:
        return 100
    if current_match["prediction_correct"] is True:
        if head_to_head_winner == current_match["prediction"]:
            calculated_weight += 1
        else:
            calculated_weight -= 1
    else:
        if head_to_head_winner == current_match["prediction"]:
            calculated_weight -= 1
        else:
            calculated_weight += 1
    return calculated_weight


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

no_assessment = matches_doc.find({"result_assessed": False})

head_to_head = head_to_head.HeadToHead()
calculated_head_to_head_weight = head_to_head.get_weight(current_weights)

rank_difference = rank_difference.RankDifference()
calculated_rank_difference_weight = rank_difference.get_weight(current_weights)

for match in no_assessment:
    head_to_head_winner = head_to_head.calculate_winner(match)
    calculated_head_to_head_weight = get_new_score(match, calculated_head_to_head_weight)

    rank_difference_winner = rank_difference.calculate_winner(match)
    calculated_rank_difference_weight = get_new_score(match, calculated_rank_difference_weight)


new_weights = weights_class.Weights()
new_weights.set_head_to_head_weight(calculated_head_to_head_weight)
new_weights.set_rank_difference_weight(calculated_rank_difference_weight)
print(to_dict(new_weights))
# current_weights_doc.insert_one(to_dict(new_weights))
