from model import mongo_client, all_tests
from predictor.calculate_winner import calculate_winner


def test_weights(current_weights, output=False):
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()

    predictions = matches_doc.find({"prediction_correct": {"$exists": True}})
    test_array = all_tests.get_all_tests()

    correct_count = 0
    incorrect_count = 0
    prediction_percentage = 0
    for item in predictions:
        winner = calculate_winner(item, test_array, current_weights)
        if item["prediction_correct"]:
            if winner == item["prediction"]:
                correct_count += 1
            else:
                incorrect_count += 1
        else:
            if winner == item["prediction"]:
                incorrect_count += 1
            else:
                correct_count += 1

    prediction_percentage = (correct_count / (correct_count + incorrect_count)) * 100

    if output:
        print("Correct: " + str(correct_count))
        print("Incorrect: " + str(incorrect_count))
        print("Percentage: " + str(prediction_percentage))

    return prediction_percentage


def get_total_game_count():
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()

    return matches_doc.count_documents({"prediction_correct": {"$exists": True}})


def get_base_weights():
    return {
        "head_to_head_weight": 1,
        "rank_difference_weight": 1,
        "average_player_weight": 1,
        "highest_player_weight": 1,
        "lowest_player_weight": 1,
        "ancient_played_weight": 1,
        "dust2_played_weight": 1,
        "inferno_played_weight": 1,
        "mirage_played_weight": 1,
        "nuke_played_weight": 1,
        "overpass_played_weight": 1,
        "vertigo_played_weight": 1,
        "ancient_won_weight": 1,
        "dust2_won_weight": 1,
        "inferno_won_weight": 1,
        "mirage_won_weight": 1,
        "nuke_won_weight": 1,
        "overpass_won_weight": 1,
        "vertigo_won_weight": 1,
        "ancient_rliw_weight": 1,
        "dust2_rliw_weight": 1,
        "inferno_rliw_weight": 1,
        "mirage_rliw_weight": 1,
        "nuke_rliw_weight": 1,
        "overpass_rliw_weight": 1,
        "vertigo_rliw_weight": 1,
        "ancient_rwil_weight": 1,
        "dust2_rwil_weight": 1,
        "inferno_rwil_weight": 1,
        "mirage_rwil_weight": 1,
        "nuke_rwil_weight": 1,
        "overpass_rwil_weight": 1,
        "vertigo_rwil_weight": 1,
        "maps_won_weight": 1,
        "maps_played_weight": 1,
        "matches_win_percentage_weight": 1,
        "matches_won_weight": 1,
        "matches_played_weight": 1
    }


all_tests = all_tests.AllTests()
test_weights(get_base_weights())
