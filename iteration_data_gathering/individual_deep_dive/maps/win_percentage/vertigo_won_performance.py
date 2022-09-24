from predictor.individual_tests.maps.win_percentage import vertigo_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


vertigo_won = vertigo_won.VertigoWon()


def run(deep_analysis_doc, query):
    execute(vertigo_won, "vertigo_won", deep_analysis_doc, query)
