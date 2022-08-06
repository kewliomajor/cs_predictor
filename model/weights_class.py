from datetime import datetime


class Weights:

    def __init__(self, head_to_head_weight):
        self.current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.head_to_head_weight = head_to_head_weight

