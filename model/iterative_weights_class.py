from model.weights_class import Weights
import random


class IterativeWeights(Weights):

    def __init__(self):
        super().__init__()
        self.iterative_tests = 0
        self.prediction_percentage = 0.0
        self.ranked_prediction_percentage = 0.0
        self.top_50_prediction_percentage = 0.0
        self.top_30_prediction_percentage = 0.0
        self.test_games = 0

    def set_weights_from_object(self, weight_object):
        for key in weight_object.keys():
            if 'weight' in key or key == 'iterative_tests':
                setattr(self, key, weight_object[key])

    def set_iterative_tests(self, num_tests):
        self.iterative_tests = num_tests

    def get_iterative_tests(self):
        return self.iterative_tests

    def randomize_weights(self):
        for item in self.__dict__:
            if 'weight' in item:
                random_number = random.randrange(-100, 100)
                new_weight = getattr(self, item) + random_number
                self.set_weight_by_name(item, new_weight)

    def get_prediction_percentage(self):
        return self.prediction_percentage

    def set_prediction_percentage(self, percentage):
        self.prediction_percentage = percentage

    def set_prediction_percentage_from_object(self, item):
        self.prediction_percentage = item["prediction_percentage"]
        self.ranked_prediction_percentage = item["ranked_prediction_percentage"]
        self.top_50_prediction_percentage = item["top_50_prediction_percentage"]
        self.top_30_prediction_percentage = item["top_30_prediction_percentage"]

    def add_iterative_tests(self, tests_ran):
        self.iterative_tests += tests_ran

    def set_test_games(self, num_games):
        self.test_games = num_games
