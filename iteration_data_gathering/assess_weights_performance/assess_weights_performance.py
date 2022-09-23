from assess_weights_base import assess_weights_performance, get_weight

weight = get_weight()

query = {"weights_id": weight["_id"], "prediction_correct": {"$exists": True}}

assess_weights_performance(query)
