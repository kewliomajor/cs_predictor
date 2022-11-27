from predictor.individual_tests.maps.rounds_lost_in_wins import anubis_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


anubis_rliw = anubis_rliw.AnubisRoundsLostInWins()


def run(deep_analysis_doc, query):
    execute(anubis_rliw, "anubis_rliw", deep_analysis_doc, query)
