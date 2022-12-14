import pymongo


class MongoClient:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

    def get_matches_document(self):
        cs_matches_db = self.client["cs_matches"]
        return cs_matches_db["matches_v2"]

    def get_weights_document(self):
        metadata_db = self.client["metadata"]
        return metadata_db["current_weights_v2"]

    def get_predictor_accuracy_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["predictor_accuracy_v2"]

    def get_predictor_accuracy_ranked_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["predictor_accuracy_ranked_only"]

    def get_predictor_accuracy_top_50_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["predictor_accuracy_top_50"]

    def get_predictor_accuracy_top_30_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["predictor_accuracy_top_30"]

    def get_deep_analysis_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["deep_analysis_v2"]

    def get_deep_analysis_ranked_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["deep_analysis_ranked_only"]

    def get_deep_analysis_top_50_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["deep_analysis_top_50"]

    def get_deep_analysis_top_30_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["deep_analysis_top_30"]

    def get_trial_weights_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["trial_weights_v2"]

    def get_trial_weights_ranked_document(self):
        predictor_db = self.client["metadata"]
        return predictor_db["trial_weights_ranked_only"]
