from model import weights_class
import json
from json import JSONEncoder
from model import mongo_client


class CsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


client = mongo_client.MongoClient()
current_weights_doc = client.get_weights_document()

current_weights = weights_class.Weights()
current_weights.set_head_to_head_weight(1.0)

current_weights_doc.insert_one(to_dict(current_weights))
