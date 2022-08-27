from bson.objectid import ObjectId
from model import mongo_client

# update to assess different weights
weight_id = ObjectId("63037f6978dbb16f833d8364")

client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

weight = current_weights_doc.find_one({"_id": weight_id})

predictions = matches_doc.find({"weights_id": weight_id, "prediction_correct": {"$exists": True}})

correct_count = 0
incorrect_count = 0
prediction_percentage = 0
for item in predictions:
    if item["prediction_correct"]:
        correct_count += 1
    else:
        incorrect_count += 1

prediction_percentage = (correct_count / (correct_count + incorrect_count)) * 100

print("Correct: " + str(correct_count))
print("Incorrect: " + str(incorrect_count))
print("Percentage: " + str(prediction_percentage))
current_weights_doc.update_one({"_id": weight_id}, {"$set": {"correct": correct_count, "incorrect": incorrect_count, "prediction_percentage": prediction_percentage}})
