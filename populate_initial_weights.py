from model import weights_class
import json
from json import JSONEncoder
from model import mongo_client, all_tests


class CsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


client = mongo_client.MongoClient()
current_weights_doc = client.get_weights_document()

all_tests = all_tests.AllTests()
test_array = all_tests.get_all_tests()

current_weights = weights_class.Weights()
for test in test_array:
    current_weights.set_weight(test, 1)

current_weights_doc.insert_one(to_dict(current_weights))
