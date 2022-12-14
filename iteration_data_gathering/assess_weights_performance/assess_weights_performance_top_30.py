from iteration_data_gathering.assess_weights_performance.assess_weights_base import assess_weights_performance,\
    get_weight

weight = get_weight()

query = {"weights_id": weight["_id"], "prediction_correct": {"$exists": True},
         "$and": [
             {"team.ranking": {"$lte": 30}},
             {"opponent.ranking": {"$lte": 30}}
         ]}

assess_weights_performance(query, "_top_30")
