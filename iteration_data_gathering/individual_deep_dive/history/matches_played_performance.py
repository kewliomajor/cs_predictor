from predictor.individual_tests.recent_history import matches_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


matches_played = matches_played.MatchesPlayed()


def run():
    execute(matches_played, "matches_played")
