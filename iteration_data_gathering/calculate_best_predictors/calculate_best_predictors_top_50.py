from model import mongo_client, all_tests
from calculate_predictors_base import update_predictors, update_deep_dives


client = mongo_client.MongoClient()
predictor_accuracy_doc = client.get_predictor_accuracy_top_50_document()
deep_analysis_doc = client.get_deep_analysis_top_50_document()

query = {"prediction_correct": {"$exists": True},
         "$and": [
             {"team.ranking": {"$lte": 50}},
             {"opponent.ranking": {"$lte": 50}}
         ]}

all_tests = all_tests.AllTests()

update_predictors(all_tests, query, predictor_accuracy_doc)

update_deep_dives(deep_analysis_doc, query)
