from predictor.individual_tests.recent_history import matches_lost
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


matches_lost = matches_lost.MatchesLost()


def run():
    execute(matches_lost, "matches_lost")
