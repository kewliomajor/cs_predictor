from model import weights_class
import pymongo
import json
from json import JSONEncoder


class CsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


client = pymongo.MongoClient("mongodb://localhost:27017/")
metadata_db = client["metadata"]
current_weights_doc = metadata_db["current_weights"]

current_weights = weights_class.Weights(1.0)

current_weights_doc.insert_one(to_dict(current_weights))
