from model import mongo_client

client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()

query = {"prediction_correct": {"$exists": True}}
complete_matches = matches_doc.find(query)

for match in complete_matches:
    matches_doc.update_one({"_id": match["_id"]}, {"$unset": {"result_assessed": "", "prediction_correct": "", "team_score": "", "opponent_score": ""}})

query = {"prediction": {"$exists": True}}
incomplete_matches = matches_doc.find(query)

for match in incomplete_matches:
    matches_doc.update_one({"_id": match["_id"]}, {"$unset": {"prediction": "", "weights_id": ""}})
