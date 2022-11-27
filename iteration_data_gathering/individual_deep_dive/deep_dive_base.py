import json
from model import mongo_client
import collections
from predictor.individual_tests.rank import Rank
from predictor.individual_tests.rank_difference import RankDifference
from predictor.individual_tests.head_to_head import HeadToHead
from predictor.individual_tests.history import History
from predictor.individual_tests.players.highest_player import HighestPlayer
from predictor.individual_tests.players.average_player import AveragePlayer
from predictor.individual_tests.players.lowest_player import LowestPlayer
from predictor.individual_tests.maps.rounds_won_in_losses_map import RoundsWonInLossesMap


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def ignore_score(test, test_score):
    if isinstance(test, Rank):
        if test_score == 0:
            return True
    elif isinstance(test, HighestPlayer):
        if test_score == 0:
            return True
    elif isinstance(test, AveragePlayer):
        if test_score == 0:
            return True
    elif isinstance(test, LowestPlayer):
        if test_score == 0:
            return True
    elif isinstance(test, RoundsWonInLossesMap):
        if test_score == 0:
            return True
    elif isinstance(test, RankDifference):
        if test_score < 0:
            return True
    elif isinstance(test, HeadToHead):
        if test_score == 0:
            return True

    return False


def get_test_score(match, test, current_team, team):
    if isinstance(test, HeadToHead):
        test_score = test.get_base_score(match, team)
    elif isinstance(test, History):
        test.populate_stats(match)
        test_score = test.get_base_score(current_team, team)
    elif isinstance(test, RankDifference):
        test_score = test.get_base_score(match, team)
    else:
        test_score = float(test.get_base_score(current_team))

    test_score = round(test_score, 2)

    return test_score


def add_to_total(match, final_array, test, current_team):
    predicted_total_winner = match["prediction"]

    team = False
    if current_team["name"] == match["team"]["name"]:
        team = True

    test_score = get_test_score(match, test, current_team, team)

    if ignore_score(test, test_score):
        return final_array

    if test_score not in final_array:
        final_array[test_score] = {"total": 0, "correct": 0, "percentage": 0}

    final_array[test_score]["total"] += 1

    if match["prediction_correct"]:
        if current_team["name"] == predicted_total_winner:
            final_array[test_score]["correct"] += 1
    else:
        if current_team["name"] != predicted_total_winner:
            final_array[test_score]["correct"] += 1

    return final_array


def execute(test, test_name, deep_analysis_doc, query):
    print_only = False
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()

    if deep_analysis_doc.find_one() is None:
        deep_analysis_doc.insert_one({})
        exit()

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
    print(test_name)
    print(to_dict(scores_and_predictors))

    data = deep_analysis_doc.find_one()

    if not print_only:
        deep_analysis_doc.update_one({"_id": data["_id"]}, {"$set": {test_name: to_dict(scores_and_predictors)}})
