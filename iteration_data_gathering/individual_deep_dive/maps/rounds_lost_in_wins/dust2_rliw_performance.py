from predictor.individual_tests.maps.rounds_lost_in_wins import dust2_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


dust2_rliw = dust2_rliw.Dust2RoundsLostInWins()


def run(deep_analysis_doc, query):
    execute(dust2_rliw, "dust2_rliw", deep_analysis_doc, query)
