from predictor.individual_tests import head_to_head
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


head_to_head = head_to_head.HeadToHead()


def run():
    execute(head_to_head, "head_to_head")
