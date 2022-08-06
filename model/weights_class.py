from datetime import datetime


class Weights:

    def __init__(self):
        self.current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.head_to_head_weight = 0.0

    def set_head_to_head_weight(self, weight):
        self.head_to_head_weight = weight

