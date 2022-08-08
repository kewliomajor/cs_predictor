
class BaseTest:

    def __init__(self, weight_name):
        self.weight_name = weight_name

    def get_weight(self, current_weights):
        if self.weight_name in current_weights:
            return current_weights[self.weight_name]
        else:
            return None
