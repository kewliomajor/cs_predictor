from iteration_data_gathering.assess_weights_performance.assess_weights_base import assess_weights_performance,\
    get_weight

weight = get_weight()

query = {"weights_id": weight["_id"], "prediction_correct": {"$exists": True},
         "$and": [
             {"team.ranking": {"$lt": 999}},
             {"opponent.ranking": {"$lt": 999}}
         ]}

assess_weights_performance(query, "_ranked_only")
