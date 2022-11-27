from predictor.individual_tests.maps.num_played import anubis_played
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


anubis_played = anubis_played.AnubisPlayed()


def run(deep_analysis_doc, query):
    execute(anubis_played, "anubis_played", deep_analysis_doc, query)
