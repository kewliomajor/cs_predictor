import pymongo


class MongoClient:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

    def get_matches_document(self):
        cs_matches_db = self.client["cs_matches"]
        return cs_matches_db["matches"]

    def get_weights_document(self):
        metadata_db = self.client["metadata"]
        return metadata_db["current_weights"]

    def get_predictor_accuracy_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["predictor_accuracy"]
