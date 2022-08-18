import pymongo
import json
from model import weights_class
from model import mongo_client, all_tests


debug = False
print_only = True


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def get_changed_weight(total_score):
    if total_score >= 2000:
        change = 6
    elif total_score >= 1000:
        change = 5
    elif total_score >= 500:
        change = 4
    elif total_score >= 200:
        change = 3
    elif total_score >= 100:
        change = 2
    elif total_score >= 0:
        change = 1
    else:
        change = 0

    return change


def get_new_score(current_match, calculated_weight, current_test):
    test_winner = current_test.calculate_winner(current_match)
    test_score = current_test.get_base_score(match)
    test_weight = current_test.get_weight(current_weights)

    if test_weight is None:
        total_score = 0
    else:
        total_score = test_score * test_weight

    if calculated_weight is None:
        return 100

    if current_match["prediction_correct"] is True:
        if test_winner == current_match["prediction"]:
            if debug:
                print("No need to add weight prediction is correct")
        else:
            if debug:
                print("subtracting " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight -= get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
    else:
        if test_winner == current_match["prediction"]:
            if debug:
                print("subtracting " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight -= get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
        else:
            if debug:
                print("adding " + current_test.weight_name + " weight based on " + str(total_score) + ", before: " + str(calculated_weight))
            calculated_weight += get_changed_weight(total_score)
            if debug:
                print("after " + str(calculated_weight))
    return calculated_weight


client = mongo_client.MongoClient()
matches_doc = client.get_matches_document()
current_weights_doc = client.get_weights_document()

current_weights = current_weights_doc.find_one(sort=[("current_time", pymongo.DESCENDING)])

query = {"result_assessed": False, "weights_id": current_weights["_id"]}
count = matches_doc.count_documents(query)
no_assessment = matches_doc.find(query)

if count == 0:
    print("No unassessed matches for current weights entry: " + str(current_weights["_id"]))
    exit()

all_tests = all_tests.AllTests()
tests_and_weights = all_tests.get_all_tests_and_weights(current_weights)

total_matches_assessed = 0

for match in no_assessment:
    for test_and_weight in tests_and_weights:
        test = test_and_weight["test"]
        old_weight = test_and_weight["calculated_weight"]
        new_weight = get_new_score(match, old_weight, test)
        test_and_weight["calculated_weight"] = new_weight

    total_matches_assessed += 1

    if not print_only:
        matches_doc.update_one({"_id": match["_id"]}, {"$set": {"result_assessed": True}})

new_weights = weights_class.Weights()
for test_and_weight in tests_and_weights:
    new_weights.set_weight(test_and_weight["test"], test_and_weight["calculated_weight"])

print("Total matches assessed: " + str(total_matches_assessed))
print(to_dict(new_weights))

if not print_only:
    current_weights_doc.insert_one(to_dict(new_weights))
