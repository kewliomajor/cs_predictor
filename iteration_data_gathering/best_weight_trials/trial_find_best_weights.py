import pymongo
import json
from model import mongo_client, iterative_weights_class
from iteration_data_gathering.best_weight_trials.test_custom_weights import get_base_weights, test_weights


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


client = mongo_client.MongoClient()
trial_weights_doc = client.get_trial_weights_document()

latest_weight = trial_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])
weight_object = iterative_weights_class.IterativeWeights()

if latest_weight is None:
    weight_object.set_weights_from_object(get_base_weights())
    trial_weights_doc.insert_one(to_dict(weight_object))
    exit()

weight_object.set_weights_from_object(latest_weight)
randomizer_runs = 200

for i in range(randomizer_runs):
    random_weight_object = iterative_weights_class.IterativeWeights()
    random_weight_object.set_weights_from_object(latest_weight)
    random_weight_object.randomize_weights()
    performance = test_weights(random_weight_object)
    if performance > weight_object.get_prediction_percentage():
        random_weight_object.set_prediction_percentage(performance)
        weight_object = random_weight_object

weight_object.add_iterative_tests(randomizer_runs)

if weight_object.get_prediction_percentage() <= latest_weight['prediction_percentage']:
    trial_weights_doc.update_one({"_id": latest_weight["_id"]}, {"$set": {"iterative_tests": weight_object.get_iterative_tests()}})
else:
    print(to_dict(weight_object))
    trial_weights_doc.insert_one(to_dict(weight_object))


