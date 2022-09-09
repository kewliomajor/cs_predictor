import json
from model import mongo_client
from bson.objectid import ObjectId
import collections
from predictor.individual_tests.rank import Rank
from predictor.individual_tests.head_to_head import HeadToHead
from predictor.individual_tests.history import History


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def add_to_total(match, final_array, test, current_team):
    predicted_total_winner = match["prediction"]
    predicted_test_winner = test.calculate_winner(match)

    team = False
    if current_team["name"] == match["team"]["name"]:
        team = True

    if isinstance(test, HeadToHead):
        test_score = test.get_base_score(match, team)
    elif isinstance(test, History):
        test.populate_stats(match)
        test_score = test.get_base_score(current_team, team)
    else:
        test_score = float(test.get_base_score(current_team))

    test_score = round(test_score, 2)

    if isinstance(test, Rank):
        if test_score == 0:
            return final_array

    if test_score not in final_array:
        final_array[test_score] = {"total": 0, "correct": 0, "percentage": 0}

    final_array[test_score]["total"] += 1

    if match["prediction_correct"]:
        if predicted_test_winner == predicted_total_winner:
            final_array[test_score]["correct"] += 1
    else:
        if predicted_test_winner != predicted_total_winner:
            final_array[test_score]["correct"] += 1

    return final_array


def execute(test, test_name):
    print_only = False
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()
    deep_analysis_doc = client.get_deep_analysis_document()

    if deep_analysis_doc.find_one() is None:
        deep_analysis_doc.insert_one({})
        exit()

    query = {"prediction_correct": {"$exists": True}}
    predictions = matches_doc.find(query)
    predictions_count = matches_doc.count_documents(query)

    scores_and_predictors = {}

    for match in predictions:
        scores_and_predictors = add_to_total(match, scores_and_predictors, test, match["team"])
        scores_and_predictors = add_to_total(match, scores_and_predictors, test, match["opponent"])

    scores_and_predictors = collections.OrderedDict(sorted(scores_and_predictors.items()))

    for score in scores_and_predictors:
        percentage = (scores_and_predictors[score]["correct"] / scores_and_predictors[score]["total"]) * 100
        scores_and_predictors[score]["percentage"] = percentage

    print("Matches analyzed: " + str(predictions_count))
    print(to_dict(scores_and_predictors))
    if not print_only:
        deep_analysis_doc.update_one({"_id": ObjectId("6314f38c5d090032d472c258")}, {"$set": {test_name: to_dict(scores_and_predictors)}})
