from predictor.individual_tests.maps.win_percentage import dust2_won
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


dust2_won = dust2_won.Dust2Won()


def run(deep_analysis_doc, query):
    execute(dust2_won, "dust2_won", deep_analysis_doc, query)
