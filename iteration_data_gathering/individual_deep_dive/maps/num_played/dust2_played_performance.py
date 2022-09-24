from predictor.individual_tests.maps.num_played import dust2_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


dust2_played = dust2_played.Dust2Played()


def run(deep_analysis_doc, query):
    execute(dust2_played, "dust2_played", deep_analysis_doc, query)
