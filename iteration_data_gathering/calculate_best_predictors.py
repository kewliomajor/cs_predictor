from model import mongo_client

client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
predictor_accuracy_doc = client.get_predictor_accuracy_document()

predictions = matches_doc.find({"prediction_correct": {"$exists": True}})

