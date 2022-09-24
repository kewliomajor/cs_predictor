from predictor.individual_tests.recent_history import match_win_percentage
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


match_win_percentage = match_win_percentage.MatchesWinPercentage()


def run(deep_analysis_doc, query):
    execute(match_win_percentage, "match_win_percentage", deep_analysis_doc, query)
