from bson.objectid import ObjectId
from model import mongo_client


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()


def get_weight():
    # update to assess different weights
    weight_id = ObjectId("6314ab04c5015ad1864abb28")
    return current_weights_doc.find_one({"_id": weight_id})


def assess_weights_performance(query, field_suffix=""):
    predictions = matches_doc.find(query)

    correct_count = 0
    incorrect_count = 0
    for item in predictions:
        if item["prediction_correct"]:
            correct_count += 1
        else:
            incorrect_count += 1

    prediction_percentage = (correct_count / (correct_count + incorrect_count)) * 100

    print("Correct: " + str(correct_count))
    print("Incorrect: " + str(incorrect_count))
    print("Percentage: " + str(prediction_percentage))
    weight_id = get_weight()["_id"]
    current_weights_doc.update_one({"_id": weight_id}, {"$set": {"correct" + field_suffix: correct_count,
                                                                 "incorrect" + field_suffix: incorrect_count,
                                                                 "prediction_percentage" + field_suffix: prediction_percentage}})
