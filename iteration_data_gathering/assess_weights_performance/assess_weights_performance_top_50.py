from assess_weights_base import get_weight, assess_weights_performance

weight = get_weight()

query = {"weights_id": weight["_id"], "prediction_correct": {"$exists": True},
         "$and": [
             {"team.ranking": {"$lte": 50}},
             {"opponent.ranking": {"$lte": 50}}
         ]}

assess_weights_performance(query, "_top_50")
