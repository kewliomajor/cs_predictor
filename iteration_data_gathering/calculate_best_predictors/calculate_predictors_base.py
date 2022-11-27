import json
from iteration_data_gathering.individual_deep_dive import rank_performance, head_to_head_performance, \
    rank_difference_performance
from iteration_data_gathering.individual_deep_dive.history import matches_played_performance, matches_won_performance, \
    match_percentage_performance, maps_played_performance, maps_won_performance
from iteration_data_gathering.individual_deep_dive.players import average_player_performance, \
    highest_player_performance, lowest_player_performance
from iteration_data_gathering.individual_deep_dive.maps.num_played import ancient_played_performance, \
    anubis_played_performance, dust2_played_performance, inferno_played_performance, mirage_played_performance, \
    nuke_played_performance, overpass_played_performance, vertigo_played_performance
from iteration_data_gathering.individual_deep_dive.maps.rounds_lost_in_wins import ancient_rliw_performance, \
    anubis_rliw_performance, dust2_rliw_performance, inferno_rliw_performance, mirage_rliw_performance, \
    nuke_rliw_performance, overpass_rliw_performance, vertigo_rliw_performance
from iteration_data_gathering.individual_deep_dive.maps.rounds_won_in_losses import ancient_rwil_performance, \
    anubis_rwil_performance, dust2_rwil_performance, inferno_rwil_performance, mirage_rwil_performance, \
    nuke_rwil_performance, overpass_rwil_performance, vertigo_rwil_performance
from iteration_data_gathering.individual_deep_dive.maps.win_percentage import ancient_won_performance, \
    anubis_won_performance, dust2_won_performance, inferno_won_performance, mirage_won_performance, \
    nuke_won_performance, overpass_won_performance, vertigo_won_performance
from model import mongo_client


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def update_predictors(all_tests, query, predictor_accuracy_doc):
    print_only = False
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()

    predictions = matches_doc.find(query)
    predictions_count = matches_doc.count_documents(query)

    test_array = all_tests.get_all_tests()

    if predictor_accuracy_doc.find_one() is None:
        predictor_accuracy_doc.insert_one({"predictors": []})
        exit()

    tests_and_predictors = []

    for test in test_array:
        test_weight_name = test.get_weight_name()
        total_predictions = 0
        correct_predictions = 0

        for match in predictions:
            predicted_total_winner = match["prediction"]
            predicted_test_winner = test.calculate_winner(match)
            total_predictions += 1

            if match["prediction_correct"]:
                if predicted_test_winner == predicted_total_winner:
                    correct_predictions += 1
            else:
                if predicted_test_winner != predicted_total_winner:
                    correct_predictions += 1

        predictions.rewind()
        if total_predictions == 0:
            predictor_percent = 0
        else:
            predictor_percent = (correct_predictions / total_predictions) * 100

        tests_and_predictors.append({"weight_name": test_weight_name, "predictor_percent": predictor_percent})

    element = {"predictors": tests_and_predictors}

    print("Matches analyzed: " + str(predictions_count))
    print(to_dict(element))

    data = predictor_accuracy_doc.find_one()

    if not print_only:
        predictor_accuracy_doc.update_one({"_id": data["_id"]}, {"$set": {"predictors": tests_and_predictors}})


def update_deep_dives(deep_analysis_doc, query):
    # run the deep dive analysis
    rank_performance.run(deep_analysis_doc, query)
    head_to_head_performance.run(deep_analysis_doc, query)
    rank_difference_performance.run(deep_analysis_doc, query)

    # history
    maps_won_performance.run(deep_analysis_doc, query)
    matches_won_performance.run(deep_analysis_doc, query)
    match_percentage_performance.run(deep_analysis_doc, query)
    matches_played_performance.run(deep_analysis_doc, query)
    maps_played_performance.run(deep_analysis_doc, query)

    # players
    average_player_performance.run(deep_analysis_doc, query)
    highest_player_performance.run(deep_analysis_doc, query)
    lowest_player_performance.run(deep_analysis_doc, query)

    # maps played
    ancient_played_performance.run(deep_analysis_doc, query)
    anubis_played_performance.run(deep_analysis_doc, query)
    dust2_played_performance.run(deep_analysis_doc, query)
    inferno_played_performance.run(deep_analysis_doc, query)
    mirage_played_performance.run(deep_analysis_doc, query)
    nuke_played_performance.run(deep_analysis_doc, query)
    overpass_played_performance.run(deep_analysis_doc, query)
    vertigo_played_performance.run(deep_analysis_doc, query)

    # maps rounds lost in wins
    ancient_rliw_performance.run(deep_analysis_doc, query)
    anubis_rliw_performance.run(deep_analysis_doc, query)
    dust2_rliw_performance.run(deep_analysis_doc, query)
    inferno_rliw_performance.run(deep_analysis_doc, query)
    mirage_rliw_performance.run(deep_analysis_doc, query)
    nuke_rliw_performance.run(deep_analysis_doc, query)
    overpass_rliw_performance.run(deep_analysis_doc, query)
    vertigo_rliw_performance.run(deep_analysis_doc, query)

    # maps rounds won in losses
    ancient_rwil_performance.run(deep_analysis_doc, query)
    anubis_rwil_performance.run(deep_analysis_doc, query)
    dust2_rwil_performance.run(deep_analysis_doc, query)
    inferno_rwil_performance.run(deep_analysis_doc, query)
    mirage_rwil_performance.run(deep_analysis_doc, query)
    nuke_rwil_performance.run(deep_analysis_doc, query)
    overpass_rwil_performance.run(deep_analysis_doc, query)
    vertigo_rwil_performance.run(deep_analysis_doc, query)

    # maps win percentage
    ancient_won_performance.run(deep_analysis_doc, query)
    anubis_won_performance.run(deep_analysis_doc, query)
    dust2_won_performance.run(deep_analysis_doc, query)
    inferno_won_performance.run(deep_analysis_doc, query)
    mirage_won_performance.run(deep_analysis_doc, query)
    nuke_won_performance.run(deep_analysis_doc, query)
    overpass_won_performance.run(deep_analysis_doc, query)
    vertigo_won_performance.run(deep_analysis_doc, query)
