from predictor.individual_tests.maps.rounds_lost_in_wins import vertigo_rliw
from iteration_data_gathering.individual_deep_dive.deep_dive_base import execute


vertigo_rliw = vertigo_rliw.VertigoRoundsLostInWins()


def run(deep_analysis_doc, query):
    execute(vertigo_rliw, "vertigo_rliw", deep_analysis_doc, query)
