from model import mongo_client, all_tests
from predictor.calculate_winner import calculate_winner


def test_weights(current_weights, output=False):
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()

    query = {"prediction_correct": {"$exists": True},
             "$and": [
                 {"team.ranking": {"$lt": 999}},
                 {"opponent.ranking": {"$lt": 999}}
             ]}

    predictions = matches_doc.find(query)
    test_array = all_tests.get_all_tests()

    results = {
        "correct_count": 0,
        "incorrect_count": 0,
        "prediction_percentage": 0,
        "ranked_correct_count": 0,
        "ranked_incorrect_count": 0,
        "ranked_prediction_percentage": 0,
        "top_50_correct_count": 0,
        "top_50_incorrect_count": 0,
        "top_50_prediction_percentage": 0,
        "top_30_correct_count": 0,
        "top_30_incorrect_count": 0,
        "top_30_prediction_percentage": 0,
    }
    for item in predictions:
        winner = calculate_winner(item, test_array, current_weights)
        ranked = False
        top_50 = False
        top_30 = False

        if item["team"]["ranking"] < 999 and item["opponent"]["ranking"] < 999:
            ranked = True
        if item["team"]["ranking"] <= 50 and item["opponent"]["ranking"] <= 50:
            top_50 = True
        if item["team"]["ranking"] <= 30 and item["opponent"]["ranking"] <= 30:
            top_30 = True

        if item["prediction_correct"]:
            if winner == item["prediction"]:
                results["correct_count"] += 1
                if ranked:
                    results["ranked_correct_count"] += 1
                if top_50:
                    results["top_50_correct_count"] += 1
                if top_30:
                    results["top_30_correct_count"] += 1
            else:
                results["incorrect_count"] += 1
                if ranked:
                    results["ranked_incorrect_count"] += 1
                if top_50:
                    results["top_50_incorrect_count"] += 1
                if top_30:
                    results["top_30_incorrect_count"] += 1
        else:
            if winner == item["prediction"]:
                results["incorrect_count"] += 1
                if ranked:
                    results["ranked_incorrect_count"] += 1
                if top_50:
                    results["top_50_incorrect_count"] += 1
                if top_30:
                    results["top_30_incorrect_count"] += 1
            else:
                results["correct_count"] += 1
                if ranked:
                    results["ranked_correct_count"] += 1
                if top_50:
                    results["top_50_correct_count"] += 1
                if top_30:
                    results["top_30_correct_count"] += 1

    results["prediction_percentage"] = (results["correct_count"] / (
            results["correct_count"] + results["incorrect_count"])) * 100
    if results["ranked_correct_count"] + results["ranked_incorrect_count"] > 0:
        results["ranked_prediction_percentage"] = (results["ranked_correct_count"] / (
                    results["ranked_correct_count"] + results["ranked_incorrect_count"])) * 100
    if results["top_50_correct_count"] + results["top_50_incorrect_count"] > 0:
        results["top_50_prediction_percentage"] = (results["top_50_correct_count"] / (
                    results["top_50_correct_count"] + results["top_50_incorrect_count"])) * 100
    if results["top_30_correct_count"] + results["top_30_incorrect_count"] > 0:
        results["top_30_prediction_percentage"] = (results["top_30_correct_count"] / (
                    results["top_30_correct_count"] + results["top_30_incorrect_count"])) * 100

    if output:
        print("Correct: " + str(results["correct_count"]))
        print("Incorrect: " + str(results["incorrect_count"]))
        print("Percentage: " + str(results["prediction_percentage"]))

    return results


def get_total_game_count():
    client = mongo_client.MongoClient()
    matches_doc = client.get_matches_document()

    query = {"prediction_correct": {"$exists": True},
             "$and": [
                 {"team.ranking": {"$lt": 999}},
                 {"opponent.ranking": {"$lt": 999}}
             ]}

    return matches_doc.count_documents(query)


def get_base_weights():
    return {
        "head_to_head_weight": 1,
        "rank_difference_weight": 1,
        "average_player_weight": 1,
        "highest_player_weight": 1,
        "lowest_player_weight": 1,
        "ancient_played_weight": 1,
        "anubis_played_weight": 1,
        "dust2_played_weight": 1,
        "inferno_played_weight": 1,
        "mirage_played_weight": 1,
        "nuke_played_weight": 1,
        "overpass_played_weight": 1,
        "vertigo_played_weight": 1,
        "ancient_won_weight": 1,
        "anubis_won_weight": 1,
        "dust2_won_weight": 1,
        "inferno_won_weight": 1,
        "mirage_won_weight": 1,
        "nuke_won_weight": 1,
        "overpass_won_weight": 1,
        "vertigo_won_weight": 1,
        "ancient_rliw_weight": 1,
        "anubis_rliw_weight": 1,
        "dust2_rliw_weight": 1,
        "inferno_rliw_weight": 1,
        "mirage_rliw_weight": 1,
        "nuke_rliw_weight": 1,
        "overpass_rliw_weight": 1,
        "vertigo_rliw_weight": 1,
        "ancient_rwil_weight": 1,
        "anubis_rwil_weight": 1,
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
