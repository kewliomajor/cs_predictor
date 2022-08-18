import json
from model import mongo_client, all_tests


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


print_only = True
client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
predictor_accuracy_doc = client.get_predictor_accuracy_document()

predictions = matches_doc.find({"prediction_correct": {"$exists": True}})

all_tests = all_tests.AllTests()
test_array = all_tests.get_all_tests()

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

print(to_dict(tests_and_predictors))
if not print_only:
    predictor_accuracy_doc.insert_one(to_dict(tests_and_predictors))
