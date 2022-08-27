import json
from model import mongo_client
from bson.objectid import ObjectId
import collections


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def run():
    from predictor.individual_tests import rank_difference

    print_only = False
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()
    deep_analysis_doc = client.get_deep_analysis_document()

    query = {"prediction_correct": {"$exists": True}}
    predictions = matches_doc.find(query)
    predictions_count = matches_doc.count_documents(query)

    rank_difference = rank_difference.RankDifference()

    scores_and_predictors = {}

    for match in predictions:
        predicted_total_winner = match["prediction"]
        predicted_test_winner = rank_difference.calculate_winner(match)

        test_score = rank_difference.get_base_score(match)

        if test_score not in scores_and_predictors:
            scores_and_predictors[test_score] = {"total": 0, "correct": 0, "percentage": 0}

        scores_and_predictors[test_score]["total"] += 1

        if match["prediction_correct"]:
            if predicted_test_winner == predicted_total_winner:
                scores_and_predictors[test_score]["correct"] += 1
        else:
            if predicted_test_winner != predicted_total_winner:
                scores_and_predictors[test_score]["correct"] += 1

    scores_and_predictors = collections.OrderedDict(sorted(scores_and_predictors.items()))

    for score in scores_and_predictors:
        percentage = (scores_and_predictors[score]["correct"] / scores_and_predictors[score]["total"]) * 100
        scores_and_predictors[score]["percentage"] = percentage

    print("Matches analyzed: " + str(predictions_count))
    print(to_dict(scores_and_predictors))
    if not print_only:
        deep_analysis_doc.update_one({"_id": ObjectId("630a5b695bb2efda3025e048")}, {"$set": {"rank_difference": to_dict(scores_and_predictors)}})
