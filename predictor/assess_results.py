import pymongo
from predictor.individual_tests import head_to_head
import json
from model import weights_class
from model import mongo_client


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

no_assessment = matches_doc.find({"result_assessed": False})

calculated_head_to_head_weight = head_to_head.get_weight(current_weights)

for match in no_assessment:
    # TODO assess weights and adjust
    new_weights = weights_class.Weights()
    new_weights.set_head_to_head_weight(calculated_head_to_head_weight)

    # current_weights_doc.insert_one(to_dict(new_weights))
