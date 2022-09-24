from predictor.individual_tests.recent_history import matches_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


matches_won = matches_won.MatchesWon()


def run(deep_analysis_doc, query):
    execute(matches_won, "matches_won", deep_analysis_doc, query)
